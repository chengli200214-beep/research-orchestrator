import importlib.util
import shutil
import unittest
from pathlib import Path
from uuid import uuid4


class InitResearchRunTests(unittest.TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).resolve().parent.parent
        self.script_path = self.repo_root / "scripts" / "init_research_run.py"
        self.temp_dir = self.repo_root / ".tmp-tests" / f"run-{uuid4().hex}"
        self.temp_dir.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def load_module(self):
        self.assertTrue(self.script_path.exists(), f"Missing script: {self.script_path}")
        spec = importlib.util.spec_from_file_location("init_research_run", self.script_path)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_create_run_generates_default_workspace(self):
        module = self.load_module()

        run_dir = module.create_run("Graph neural network baseline", root=self.temp_dir)

        self.assertTrue((run_dir / "brief.md").exists())
        self.assertTrue((run_dir / "experiment.md").exists())
        self.assertTrue((run_dir / "results.md").exists())
        self.assertTrue((run_dir / "paper-outline.md").exists())
        self.assertTrue((run_dir / "memory" / "ideation.md").exists())
        self.assertTrue((run_dir / "memory" / "experimentation.md").exists())


if __name__ == "__main__":
    unittest.main()
