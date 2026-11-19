"""Portable environment diagnostics and self-healing NumPy installation tests."""
import subprocess
import unittest
from pathlib import Path
from unittest.mock import patch

import bootstrap


def result(code, stdout="", stderr=""):
    return subprocess.CompletedProcess(["python", "-c", "test"], code, stdout, stderr)


class EnvironmentChecks(unittest.TestCase):
    def test_utility_reuses_launcher_environment(self):
        with patch.object(bootstrap.sys, 'argv', ['bootstrap.py', 'inspect-training', 'runs/check']), \
             patch.object(bootstrap, '_venv_python', return_value=Path(__file__)), \
             patch.object(bootstrap.subprocess, 'run', return_value=result(0)) as run:
            self.assertEqual(bootstrap.main(), 0)
            self.assertEqual(run.call_args.args[0][0], str(Path(__file__)))
            self.assertEqual(run.call_args.kwargs['env']['PYTHONUTF8'], '1')

    def test_valid_numpy_and_mlx_need_no_pip(self):
        with patch.object(bootstrap, "_import_check", side_effect=[result(0, "NumPy 2.5.4 OK\n"), result(0, "MLX backend OK\n")]), \
             patch.object(bootstrap.subprocess, "run") as run:
            bootstrap.verify_training_environment(Path("/fake/python"), "mlx", {})
            run.assert_not_called()

    def test_broken_numpy_is_repaired_before_mlx_import(self):
        failed = result(1, stderr="ModuleNotFoundError: No module named 'numpy._core._multiarray_umath'")
        with patch.object(bootstrap, "_import_check", side_effect=[failed, result(0), result(0)]), \
             patch.object(bootstrap.subprocess, "run", return_value=result(0)) as run:
            bootstrap.verify_training_environment(Path("/fake/python"), "mlx", {})
            command = run.call_args.args[0]
            self.assertIn("--force-reinstall", command)
            self.assertIn("--no-cache-dir", command)
            self.assertIn("--no-deps", command)
            self.assertIn("numpy>=1.26,<3", command)
            self.assertEqual(run.call_count, 1)

    def test_unrecoverable_import_fails_cleanly(self):
        failed = result(1, stderr="ModuleNotFoundError: No module named 'numpy._core._multiarray_umath'")
        with patch.object(bootstrap, "_import_check", side_effect=[failed, failed]), \
             patch.object(bootstrap.subprocess, "run", return_value=result(0)):
            with self.assertRaisesRegex(RuntimeError, "NumPy repair did not succeed"):
                bootstrap.verify_training_environment(Path("/fake/python"), "mlx", {})

    def test_backend_import_failure_is_reported(self):
        with patch.object(bootstrap, "_import_check", side_effect=[result(0), result(1, stderr="ModuleNotFoundError: mlx_lm")]), \
             patch.object(bootstrap.subprocess, "run") as run:
            with self.assertRaisesRegex(RuntimeError, "mlx backend cannot load"):
                bootstrap.verify_training_environment(Path("/fake/python"), "mlx", {})
            run.assert_not_called()

    def test_requirements_signature_changes_with_dependencies(self):
        with patch.object(bootstrap, "ROOT", Path(__file__).resolve().parents[1]):
            self.assertNotEqual(bootstrap._requirements_signature("mlx", False),
                                bootstrap._requirements_signature("torch", False))
            self.assertNotEqual(bootstrap._requirements_signature("mlx", False),
                                bootstrap._requirements_signature("mlx", True))


if __name__ == "__main__":
    unittest.main()
