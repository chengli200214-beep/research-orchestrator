import importlib.util
import shutil
import unittest
from pathlib import Path
from uuid import uuid4


class InstallSkillTests(unittest.TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).resolve().parent.parent
        self.script_path = self.repo_root / "scripts" / "install_skill.py"
        self.temp_home = self.repo_root / ".tmp-tests" / f"install-{uuid4().hex}"
        self.temp_home.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.temp_home, ignore_errors=True)

    def load_module(self):
        self.assertTrue(self.script_path.exists(), f"Missing script: {self.script_path}")
        spec = importlib.util.spec_from_file_location("install_skill", self.script_path)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_install_skill_places_copy_in_runtime_specific_directory(self):
        module = self.load_module()

        codex_dir = module.install_skill(
            source=self.repo_root,
            runtime="codex",
            home=self.temp_home,
            force=True,
        )
        claude_dir = module.install_skill(
            source=self.repo_root,
            runtime="claude",
            home=self.temp_home,
            force=True,
        )
        agents_dir = module.install_skill(
            source=self.repo_root,
            runtime="agents",
            home=self.temp_home,
            force=True,
        )

        self.assertEqual(
            codex_dir,
            self.temp_home / ".codex" / "skills" / "research-orchestrator",
        )
        self.assertEqual(
            claude_dir,
            self.temp_home / ".claude" / "skills" / "research-orchestrator",
        )
        self.assertEqual(
            agents_dir,
            self.temp_home / ".agents" / "skills" / "research-orchestrator",
        )

        self.assertTrue((codex_dir / "SKILL.md").exists())
        self.assertTrue((claude_dir / "SKILL.md").exists())
        self.assertTrue((agents_dir / "SKILL.md").exists())


if __name__ == "__main__":
    unittest.main()
