"""Small, ungated Qwen2.5 checkpoints for native MLX and PyTorch training."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Preset:
    title: str
    mlx_repo: str
    hf_repo: str
    size: str
    iterations: int
    layers: int
    description: str


PRESETS = (
    Preset("Coder Mini (default)", "mlx-community/Qwen2.5-Coder-0.5B-Instruct-4bit",
           "Qwen/Qwen2.5-Coder-0.5B-Instruct", "0.5B", 100, 8,
           "Smallest; code-related questions; suited to lower-memory Apple Silicon systems"),
    Preset("Coder Balanced", "mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit",
           "Qwen/Qwen2.5-Coder-1.5B-Instruct", "1.5B", 120, 8,
           "Better code reasoning; more memory is recommended"),
    Preset("General Mini", "mlx-community/Qwen2.5-0.5B-Instruct-4bit",
           "Qwen/Qwen2.5-0.5B-Instruct", "0.5B", 100, 8,
           "Small general knowledge assistant"),
    Preset("General Balanced", "mlx-community/Qwen2.5-1.5B-Instruct-4bit",
           "Qwen/Qwen2.5-1.5B-Instruct", "1.5B", 120, 8,
           "More capable general assistant; more memory is recommended"),
)
