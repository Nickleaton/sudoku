"""TestConfigWriterCommand."""
import logging
import unittest
from pathlib import Path

from src.commands.config_writer_command import ConfigWriterCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.problem import Problem
from tests.commands.test_simple_command import TestSimpleCommand


class TestConfigWriterCommand(TestSimpleCommand):
    """Test suite for the ConfigWriterCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.prerequisites = LoadConfigCommand(self.path)
        self.prerequisites.execute(self.problem)
        self.output_path = Path("output/tests/test.yaml")
        self.command = ConfigWriterCommand(source='config', target=self.output_path)
        self.requirements = ['config']
        self.target = self.output_path
        self.representation = r"ConfigWriterCommand('config', 'output\\tests\\test.yaml')"

    def tearDown(self):
        """Clean up the test environment."""
        super().tearDown()
        if self.output_path.exists() and self.output_path.is_file():
            logging.info(f"Deleting file {self.output_path}")
            self.output_path.unlink()

    def test_execute(self):
        """Test the execute method of the ConfigWriterCommand."""
        if not self.output_path.parent.exists():
            logging.info(f"Creating directory {self.output_path.parent}")
            self.output_path.parent.mkdir(parents=True, exist_ok=True)

        self.command.execute(self.problem)
        self.assertTrue(self.output_path.exists())

        # Read back the output and compare that what was written matches
        # The writer adds quotes. Nulls have been removed
        problem2 = Problem()
        loader = LoadConfigCommand(self.output_path)
        loader.execute(problem2)
        self.assertEqual(self.problem.config, problem2.config)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
