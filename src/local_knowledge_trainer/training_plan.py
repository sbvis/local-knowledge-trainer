"""Training budget based on dataset coverage, not a fixed 100-iteration ritual."""
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TrainingPlan:
    examples: int
    validation_examples: int
    iterations: int
    effective_passes: float
    max_sequence_length: int
    learning_rate: float
    validation_interval: int
    validation_batches: int
    target_passes: int

    def as_dict(self) -> dict:
        return self.__dict__.copy()


def make_training_plan(data_dir: str | Path, preset, mode: str, *, backend: str = "mlx") -> TrainingPlan:
    """Cover training data at least once (quick) or ~3 times (standard).

    MLX-LM and torch use distinct batch handling, so effective passes are
    an *approximate sample exposure budget*, not a guarantee of exact epochs.
    """
    if mode not in ('quick', 'standard'):
        raise ValueError('Training mode must be quick or standard')
    if backend not in ('mlx', 'torch'):
        raise ValueError('Backend must be mlx or torch')
    directory = Path(data_dir)
    counts = []
    for filename in ('train.jsonl', 'valid.jsonl'):
        path = directory / filename
        if not path.is_file():
            raise FileNotFoundError(f'Training file missing: {path}')
        n = 0
        with path.open(encoding='utf-8') as stream:
            for line in stream:
                if line.strip():
                    doc = json.loads(line)
                    if not isinstance(doc, dict) or len(doc.get('messages', [])) < 2:
                        raise ValueError(f'Invalid conversational dataset row in {path}')
                    n += 1
        if n < 1:
            raise ValueError(f'Empty training/validation file: {path}')
        counts.append(n)
    train, val = counts
    target = 3 if mode == 'standard' else 1
    # An upper bound protects 16 GB Macs. Avoid an arbitrary minimum of 100
    # updates on a tiny dataset: it can overfit a handful of responses.
    samples_per_update = 4 if backend == 'torch' else 1
    iterations = min(1800, max(1, math.ceil(target * train / samples_per_update)))
    lr = 2e-5 if preset.size == '1.5B' else 3e-5
    return TrainingPlan(
        examples=train, validation_examples=val, iterations=iterations,
        effective_passes=round(iterations * samples_per_update / train, 2),
        max_sequence_length=1024, learning_rate=lr,
        validation_interval=min(200, max(25, iterations // 8)),
        validation_batches=min(4, val), target_passes=target,
    )
