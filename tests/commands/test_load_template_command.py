"""TestCreateTemplateCommand."""
import unittest
from pathlib import Path

from src.commands.create_template_command import CreateTemplateCommand
from src.commands.file_reader_command import FileReaderCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateTemplateCommand(TestSimpleCommand):
    """Test suite for the CreateTemplateCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.prerequisites = FileReaderCommand(file_name='problem_raw_file_name',
                                               target='raw_template_text',
                                               file_path=Path('src/html/problem.html'))

        self.prerequisites.execute(self.problem)
        self.command = CreateTemplateCommand(source='raw_template_text', target='problem_raw_template')
        self.representation = r"CreateTemplateCommand('raw_template_text', 'problem_raw_template')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
