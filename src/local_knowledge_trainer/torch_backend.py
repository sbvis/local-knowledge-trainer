"""Portable PyTorch/PEFT supervised LoRA backend (CPU or NVIDIA CUDA).

This module is imported only when --backend torch is selected. The normal
indexing, SQLite query, and CLI workflows need no PyTorch installation.
"""
from __future__ import annotations

import json
import math
import random
from pathlib import Path

from .common import dump_json, info

MAX_TOKENS = 768
SEED = 42


def _tokenize_row(tokenizer, messages: list[dict], max_length: int = MAX_TOKENS) -> dict:
    """Train on the assistant answer only, never on instruction/prompt tokens."""
    if not messages or messages[-1].get("role") != "assistant":
        raise ValueError("Each sample must end with an assistant answer")
    prefix = tokenizer.apply_chat_template(messages[:-1], tokenize=True, add_generation_prompt=True)
    full = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=False)
    if full[:len(prefix)] != prefix:
        raise ValueError("Chat template prompt was not a prefix of the full training example")
    answer = full[len(prefix):][:max_length]
    if not answer:
        raise ValueError("Empty answer tokens")
    prompt_budget = max_length - len(answer)
    prefix = prefix[-prompt_budget:] if prompt_budget else []
    tokens = prefix + answer
    return {"input_ids": tokens, "attention_mask": [1] * len(tokens),
            "labels": [-100] * len(prefix) + answer}


def _read_rows(filename: Path) -> list[list[dict]]:
    with Path(filename).open(encoding="utf-8") as handle:
        rows = [json.loads(line)["messages"] for line in handle if line.strip()]
    if not rows:
        raise ValueError(f"Empty dataset: {filename}")
    return rows


def _collate(batch: list[dict], tokenizer, torch):
    length = max(len(example["input_ids"]) for example in batch)
    pad = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id
    return {key: torch.tensor([
        row[key] + ([pad] if key == "input_ids" else [0] if key == "attention_mask" else [-100])
        * (length - len(row[key])) for row in batch
    ], dtype=torch.long) for key in ("input_ids", "attention_mask", "labels")}


def train_torch(model_path: str, data_dir: str, adapter_dir: str, preset, mode: str) -> int:
    """LoRA training with only PyTorch, Transformers and PEFT; no online trainer."""
    import torch
    from peft import (LoraConfig, TaskType, get_peft_model,
                      get_peft_model_state_dict, set_peft_model_state_dict)
    from transformers import AutoModelForCausalLM, AutoTokenizer

    random.seed(SEED)
    torch.manual_seed(SEED)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dtype = (torch.bfloat16 if device.type == 'cuda' and torch.cuda.get_device_capability()[0] >= 8
             else torch.float16 if device.type == "cuda" else torch.float32)
    if device.type == "cpu":
        info("WARNING: CPU-only fine-tuning is supported but can be extremely slow. Start with 0.5B.")
    info(f"Loading model for PyTorch LoRA: {device} / {dtype}")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=False)
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=dtype,
                                                 trust_remote_code=False)
    model.config.use_cache = False
    model = get_peft_model(model, LoraConfig(
        r=8, lora_alpha=16, lora_dropout=0.05, bias="none", task_type=TaskType.CAUSAL_LM,
        target_modules=["q_proj", "v_proj"],
    ))
    model.enable_input_require_grads()
    model.gradient_checkpointing_enable()
    model.to(device)
    model.train()

    rows = _read_rows(Path(data_dir) / "train.jsonl")
    examples = [_tokenize_row(tokenizer, row, max_length=1024) for row in rows]
    validation = [_tokenize_row(tokenizer, row, max_length=1024) for row in _read_rows(Path(data_dir) / "valid.jsonl")]
    from .training_plan import make_training_plan
    plan = make_training_plan(data_dir, preset, mode, backend="torch")
    iterations = plan.iterations
    info(f"Training plan: {plan.examples} examples, {iterations} optimizer steps "
         f"(4 accumulated samples per step); context {plan.max_sequence_length}")
    opt = torch.optim.AdamW((p for p in model.parameters() if p.requires_grad), lr=plan.learning_rate)
    use_scaler = device.type == "cuda" and dtype == torch.float16
    scaler = torch.amp.GradScaler("cuda", enabled=use_scaler)
    batch_count = 0
    running_loss = 0.0
    best_validation_loss = float('inf')
    best_adapter = None
    best_step = 0
    validation_history = []
    accumulation = 4
    opt.zero_grad(set_to_none=True)
    for step in range(iterations):
        # Each optimizer step uses a small accumulated batch to reduce memory.
        for _ in range(accumulation):
            sample = examples[batch_count % len(examples)]
            if batch_count and batch_count % len(examples) == 0:
                random.shuffle(examples)
            batch_count += 1
            batch = {k: v.to(device) for k, v in _collate([sample], tokenizer, torch).items()}
            with torch.autocast(device_type="cuda", dtype=dtype, enabled=device.type == "cuda"):
                loss = model(**batch).loss / accumulation
            if not torch.isfinite(loss):
                raise RuntimeError(f'Nonfinite training loss at step {step + 1}; refusing to export invalid weights')
            scaler.scale(loss).backward()
            running_loss += loss.item()
        scaler.unscale_(opt)
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        scaler.step(opt)
        scaler.update()
        opt.zero_grad(set_to_none=True)
        if (step + 1) % 10 == 0 or step == iterations - 1:
            info(f"Torch LoRA step {step + 1}/{iterations}, average train loss {running_loss / (step + 1):.4f}")
        if (step + 1) % plan.validation_interval == 0 or step == iterations - 1:
            model.eval()
            with torch.no_grad():
                losses = []
                for sample in validation[:plan.validation_batches]:
                    batch = {k: v.to(device) for k, v in _collate([sample], tokenizer, torch).items()}
                    with torch.autocast(device_type='cuda', dtype=dtype, enabled=device.type == 'cuda'):
                        losses.append(model(**batch).loss.float().item())
            validation_loss = sum(losses) / len(losses)
            if not math.isfinite(validation_loss):
                raise RuntimeError('Nonfinite validation loss; refusing to export invalid weights')
            validation_history.append({'step': step + 1, 'loss': validation_loss})
            info(f'Validation loss at step {step + 1}: {validation_loss:.4f}')
            if validation_loss < best_validation_loss:
                best_validation_loss = validation_loss
                best_step = step + 1
                best_adapter = {key: tensor.detach().cpu().clone()
                                for key, tensor in get_peft_model_state_dict(model).items()}
            model.train()

    set_peft_model_state_dict(model, best_adapter)
    info(f'Selected adapter from step {best_step} with the lowest held-out validation loss')
    model.eval()
    losses = []
    with torch.no_grad():
        for sample in validation[:min(len(validation), 10)]:
            batch = {k: v.to(device) for k, v in _collate([sample], tokenizer, torch).items()}
            with torch.autocast(device_type="cuda", dtype=dtype, enabled=device.type == "cuda"):
                losses.append(model(**batch).loss.float().item())
    adapter_dir = Path(adapter_dir)
    adapter_dir.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(adapter_dir, safe_serialization=True)
    dump_json(adapter_dir / "training_plan.json", plan.as_dict())
    dump_json(adapter_dir / "training_metrics.json", {
        "backend": "torch", "device": str(device), "steps": iterations,
        "mean_train_loss": round(running_loss / iterations, 5),
        "mean_validation_loss": round(sum(losses) / len(losses), 5) if losses else None,
        "validation_samples": len(losses),
        "selected_step": best_step,
        "validation_history": validation_history,
        "note": "Loss measurements are NOT a factual correctness or question-answering benchmark."
    })
    if not (adapter_dir / "adapter_model.safetensors").is_file():
        raise RuntimeError("PyTorch/PEFT did not save a LoRA adapter")
    return iterations


def fuse_torch(model_path: str, adapter_dir: str, fused_dir: str) -> None:
    """Merge adapter on CPU, saving ordinary Hugging Face safetensors."""
    import gc
    import torch
    from peft import PeftModel
    from transformers import AutoModelForCausalLM, AutoTokenizer

    info("Merging PyTorch adapter on CPU (requires enough system RAM and disk space)")
    base = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float32,
                                                trust_remote_code=False, low_cpu_mem_usage=False)
    model = PeftModel.from_pretrained(base, adapter_dir)
    merged = model.merge_and_unload()
    fused_dir = Path(fused_dir)
    merged.save_pretrained(fused_dir, safe_serialization=True, max_shard_size="2GB")
    AutoTokenizer.from_pretrained(model_path, trust_remote_code=False).save_pretrained(fused_dir)
    if not list(fused_dir.glob("*.safetensors")):
        raise RuntimeError("PEFT did not produce merged safetensors")
    del base, model, merged
    gc.collect()
