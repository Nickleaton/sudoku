"""TestFileReaderCommand."""
import unittest
from pathlib import Path

from tests.commands.test_simple_command import TestSimpleCommand


class TestFileWriterCommand(TestSimpleCommand):
    """Test suite for the FileWriterCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.problem.file_data = 'Hello World'
        self.command = None
        self.representation = 'FileWriterCommand()'
        if self.command is None:
            self.skipTest('Base test class skipped because self.digit is not defined.')

    def tearDown(self):
        """Clean up the test environment."""
        target_file: Path = self.problem.output_directory / self.command.target
        if target_file.exists():
            target_file.unlink()

    def test_contents(self):
        """Test the contents of the file_path."""
        target_file: Path = self.problem.output_directory / self.command.target
        self.command.execute(self.problem)
        self.assertTrue(target_file.exists())
        with target_file.open('r') as f:
            self.assertEqual(f.read(), 'Hello World')


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
