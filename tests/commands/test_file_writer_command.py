"""TestFileReaderCommand."""
import unittest
from pathlib import Path

from src.commands.file_writer_command import FileWriterCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestFileWriterCommand(TestSimpleCommand):
    """Test suite for the FileWriterCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.problem.file_data = 'Hello World'
        self.command = FileWriterCommand(file_path=Path(r'output/tests/output.txt'))
        self.representation = r"FileWriterCommand('file_name', 'output\\tests\\output.txt', 'file_data')"

    def tearDown(self):
        """Clean up the test environment."""
        if self.command.file_path.exists():
            self.command.file_path.unlink()

    def test_contents(self):
        """Test the contents of the file."""
        self.command.execute(self.problem)
        self.assertTrue(self.command.file_path.exists())
        with self.command.file_path.open('r') as f:
            self.assertEqual(f.read(), 'Hello World')


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
