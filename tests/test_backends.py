import unittest
from unittest.mock import patch

from local_knowledge_trainer.cli import select_backend
from local_knowledge_trainer.torch_backend import _tokenize_row
from local_knowledge_trainer.models import PRESETS


class DummyTokenizer:
    def apply_chat_template(self, messages, tokenize, add_generation_prompt):
        if add_generation_prompt:
            return [1, 2, 3]
        return [1, 2, 3, 4, 5, 6]


class BackendTests(unittest.TestCase):
    def test_auto_uses_mlx_on_apple_silicon(self):
        with patch('local_knowledge_trainer.cli.platform.system', return_value='Darwin'), patch(
            'local_knowledge_trainer.cli.platform.machine', return_value='arm64'
        ):
            self.assertEqual(select_backend('auto'), 'mlx')

    def test_auto_uses_torch_on_windows(self):
        with patch('local_knowledge_trainer.cli.platform.system', return_value='Windows'), patch(
            'local_knowledge_trainer.cli.platform.machine', return_value='AMD64'
        ):
            self.assertEqual(select_backend('auto'), 'torch')
            with self.assertRaises(RuntimeError):
                select_backend('mlx')

    def test_presets_have_compatible_backend_repositories(self):
        self.assertEqual(len(PRESETS), 4)
        for preset in PRESETS:
            self.assertIn('mlx-community/', preset.mlx_repo)
            self.assertIn('Qwen/', preset.hf_repo)

    def test_pytorch_training_masks_prompt_tokens(self):
        row = _tokenize_row(DummyTokenizer(), [
            {'role': 'user', 'content': 'Why?'},
            {'role': 'assistant', 'content': 'Because.'}
        ])
        self.assertEqual(row['labels'], [-100, -100, -100, 4, 5, 6])
        self.assertEqual(row['input_ids'], [1, 2, 3, 4, 5, 6])

    def test_mask_survives_truncation(self):
        row = _tokenize_row(DummyTokenizer(), [
            {'role': 'user', 'content': 'Why?'}, {'role': 'assistant', 'content': 'Because.'}
        ], max_length=4)
        self.assertEqual(row['labels'], [-100, 4, 5, 6])

    def test_answer_filling_context_does_not_retain_prompt(self):
        row = _tokenize_row(DummyTokenizer(), [
            {'role': 'user', 'content': 'Why?'}, {'role': 'assistant', 'content': 'Because.'}
        ], max_length=3)
        self.assertEqual(row['input_ids'], [4, 5, 6])
        self.assertEqual(row['labels'], [4, 5, 6])
