# Model presets and conversion

All four presets use the Qwen2.5 Instruct family. The code/model licenses and permitted redistribution of your *input sources* must be checked separately. The project does not include pretrained model weights.

| Profile | Apple Silicon MLX (4-bit training checkpoint) | PyTorch checkpoint (original model) |
|---|---|---|
| Coder Mini | `mlx-community/Qwen2.5-Coder-0.5B-Instruct-4bit` | `Qwen/Qwen2.5-Coder-0.5B-Instruct` |
| Coder Balanced | `mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit` | `Qwen/Qwen2.5-Coder-1.5B-Instruct` |
| General Mini | `mlx-community/Qwen2.5-0.5B-Instruct-4bit` | `Qwen/Qwen2.5-0.5B-Instruct` |
| General Balanced | `mlx-community/Qwen2.5-1.5B-Instruct-4bit` | `Qwen/Qwen2.5-1.5B-Instruct` |

## Training and export

On Apple Silicon, `mlx_lm lora` trains an adapter on a 4-bit MLX checkpoint and `mlx_lm fuse --dequantize` merges it. On Windows/Linux, PyTorch/PEFT trains a LoRA adapter on the original checkpoint and merges it in FP32 on CPU. Both merged models are converted with `llama.cpp/convert_hf_to_gguf.py` and quantized with `llama-quantize Q4_K_M`.

MLX's direct GGUF export is limited in supported architectures; the separate llama.cpp conversion pipeline deliberately handles Qwen. Conversion/quantization can use substantial temporary disk. No model format is magically smaller because it is split into shards. The Q4 model is smaller for inference; the training stage is materially more demanding.

## Engineering considerations

- 0.5B is designed as the default on limited-memory hardware but remains weak at complex multi-file reasoning.
- 1.5B generally offers better answers but needs more RAM and computation; there is no guaranteed accuracy improvement on a particular dataset.
- The fixed LoRA training schedule is a useful baseline, **not** an optimization validated on every dataset. Hyperparameters, data quality, holdout strategy and actual performance should be recorded for a meaningful comparison.
- The export pipeline checks the file signature and runs one local generation. A completed smoke test is *not* equivalent to a model accuracy evaluation.

Resources: [MLX LoRA](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md), [Hugging Face PEFT](https://huggingface.co/docs/peft/index), [llama.cpp converter](https://github.com/ggml-org/llama.cpp/blob/master/convert_hf_to_gguf.py), [GGUF sharding](https://github.com/ggml-org/llama.cpp/tree/master/tools/gguf-split).
