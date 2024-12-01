"""TestFileReaderCommand."""
import unittest
from pathlib import Path

from src.commands.file_reader_command import FileReaderCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestFileReaderCommand(TestSimpleCommand):
    """Test suite for the FileReaderCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = FileReaderCommand(file_path=Path('problems\\easy\\problem001.yaml'))
        self.representation = r"FileReaderCommand('file_name', 'problems\\easy\\problem001.yaml', 'file_data')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
