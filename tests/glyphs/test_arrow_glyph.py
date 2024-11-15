"""TestWriterCommand."""
import unittest
from pathlib import Path

from src.commands.writer_command import WriterCommand
from src.commands.problem import Problem
from tests.commands.test_simple_command import TestSimpleCommand


class TestWriterCommand(TestSimpleCommand):
    """Test suite for WriterCommand class."""

    def setUp(self) -> None:
        """Set up the test environment for WriterCommand.

        This method initializes the problem and prepares the WriterCommand
        with a target file path for testing.
        """
        self.problem = Problem()
        self.problem.svg = "Hello World"
        self.command = WriterCommand("svg", Path("c:\\temp\\filewriter.txt"))
        if self.command.target.exists():
            self.command.target.unlink(missing_ok=True)

    def tearDown(self) -> None:
        """Clean up after each test.

        This method deletes the target file if it exists after the test has run.
        """
        if self.command.target.exists():
            self.command.target.unlink(missing_ok=True)

    def test_process(self):
        """Test the execute method of WriterCommand.

        This method checks if the target file is created and contains the
        expected content after execution.
        """
        self.assertFalse(self.command.target.exists())
        self.command.execute(self.problem)
        self.assertTrue(self.command.target.exists())
        with self.command.target.open('r') as f:
            self.assertEqual(self.problem.svg, f.read())

    @property
    def representation(self) -> str:
        """Return the string representation of WriterCommand.

        Returns:
            str: The representation of the WriterCommand instance with file path.
        """
        return f"{self.command.__class__.__name__}('svg', {'c:\\temp\\filewriter.txt'!r})"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
