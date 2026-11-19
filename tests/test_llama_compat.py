"""Test real command building without running a large model."""
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from local_knowledge_trainer.demo import llama_command, run_question, supported_llama_flags
from local_knowledge_trainer.index import create_index
from local_knowledge_trainer.prepare import Chunk


class LlamaCliCompatTests(unittest.TestCase):
    def test_drops_removed_flag_and_only_uses_supported_optional_flags(self):
        with patch('local_knowledge_trainer.demo.subprocess.run') as run:
            run.return_value.stdout = '--single-turn --offline --simple-io'
            run.return_value.stderr = ''
            supported_llama_flags.cache_clear()
            cmd = llama_command('/example/llama-cli', Path('model.gguf'), 'Hello', 64)
            self.assertNotIn('--no-conversation', cmd)
            self.assertNotIn('--no-display-prompt', cmd)
            self.assertIn('--single-turn', cmd)
            self.assertIn('--offline', cmd)
            self.assertIn('--simple-io', cmd)

    @unittest.skipIf(os.name == 'nt', 'Shell script simulation is POSIX-only')
    def test_ask_command_executable_smoke_test(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            release = root / 'release'
            release.mkdir()
            (release / 'assistant.gguf').write_bytes(b'GGUFplaceholder')
            create_index([Chunk('https://github.com/example/Scatterplot',
                                'README.md', 'document',
                                'Scatterplot is a library for drawing points.', 1, 1)],
                         release / 'knowledge.db')
            executable = root / 'llama-cli'
            executable.write_text('#!/bin/sh\n'
                                  'if [ "$1" = "--help" ]; then echo "--single-turn --offline"; exit 0; fi\n'
                                  'for arg in "$@"; do if [ "$arg" = "--no-conversation" ]; then exit 44; fi; done\n'
                                  'echo "This is the mocked local answer."\n')
            executable.chmod(0o755)
            supported_llama_flags.cache_clear()
            self.assertGreaterEqual(run_question(release, 'What does Scatterplot do?',
                                                 cli_path=str(executable)), 1)
