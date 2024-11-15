import unittest
from pathlib import Path

from src.commands.writer_command import WriterCommand
from src.commands.problem import Problem
from tests.commands.test_simple_command import TestSimpleCommand


class TestWriterCommand(TestSimpleCommand):

    def setUp(self) -> None:
        self.problem = Problem()
        self.problem.svg = "Hello World"
        self.command = WriterCommand("svg", Path("c:\\temp\\filewriter.txt"))
        if self.command.target.exists():
            self.command.target.unlink(missing_ok=True)

    def tearDown(self) -> None:
        if self.command.target.exists():
            self.command.target.unlink(missing_ok=True)

    def test_process(self):
        self.assertFalse(self.command.target.exists())
        self.command.execute(self.problem)
        self.assertTrue(self.command.target.exists())
        with self.command.target.open('r') as f:
            self.assertEqual(self.problem.svg, f.read())

    @property
    def representation(self) -> str:
        return f"{self.command.__class__.__name__}('svg', {"c:\\temp\\filewriter.txt"!r})"



if __name__ == '__main__':  # pragma: no cover
    unittest.main()
