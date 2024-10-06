import unittest
from pathlib import Path

from src.commands.file_writer_command import FileWriterCommand
from src.commands.problem import Problem
from tests.commands.test_simple_command import TestSimpleCommand


class TestFileWriterCommand(TestSimpleCommand):

    def setUp(self) -> None:
        self.problem = Problem()
        self.problem.svg = "Hello World"
        self.command = FileWriterCommand("svg", Path("c:\\temp\\filewriter.txt"))
        if self.command.file_name.exists():
            self.command.file_name.unlink(missing_ok=True)

    def tearDown(self) -> None:
        if self.command.file_name.exists():
            self.command.file_name.unlink(missing_ok=True)

    def test_process(self):
        self.assertFalse(self.command.file_name.exists())
        self.command.execute(self.problem)
        self.assertTrue(self.command.file_name.exists())
        with self.command.file_name.open('r') as f:
            self.assertEqual(self.problem.svg, f.read())

    @property
    def representation(self) -> str:
        return f"{self.command.__class__.__name__}('svg', {repr(Path("c:\\temp\\filewriter.txt"))})"



if __name__ == '__main__':  # pragma: no cover
    unittest.main()
