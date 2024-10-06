import logging
import unittest
from pathlib import Path

from src.commands.config_writer_command import ConfigWriterCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.problem import Problem
from tests.commands.test_simple_command import TestSimpleCommand


class TestConfigWriterCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        self.reader = LoadConfigCommand(self.path)
        self.problem = Problem()
        self.reader.execute(self.problem)
        self.output_path = Path("c:\\temp\\test.yaml")
        self.command = ConfigWriterCommand(self.output_path)

    @property
    def representation(self) -> str:
        return f"ConfigWriterCommand('{self.output_path}')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))

    def test_execute(self):
        if not self.output_path.parent.exists():
            logging.info(f"Creating directory {self.output_path.parent}")
            self.output_path.parent.mkdir(parents=True, exist_ok=True)

        self.command.execute(self.problem)
        self.assertTrue(self.output_path.exists())

        # read the back the output and compare that what was written matches
        # The writer adds quotes. Nulls have been removed

        problem2 = Problem()
        loader = LoadConfigCommand(self.output_path)
        loader.execute(problem2)
        self.assertEqual(self.problem.config, problem2.config)

    def tearDown(self):
        if self.output_path.exists() and self.output_path.is_file():
            logging.info(f"Deleting file {self.output_path}")
            self.output_path.unlink()


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
