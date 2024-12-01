"""TestCreateConstraintsCommand."""
import unittest
from pathlib import Path


from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.file_reader_command import FileReaderCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateConstraintsCommand(TestSimpleCommand):
    """Test suite for the CreateConstraintsCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.prerequisites = FileReaderCommand(file_name='config_file_name',
                                               target='config_text',
                                               file_path=Path('problems\\easy\\problem001.yaml')) \
                             | LoadConfigCommand() \
                             | CreateBoardCommand()
        self.prerequisites.execute(self.problem)
        self.command = CreateConstraintsCommand()
        self.representation = "CreateConstraintsCommand('config', 'board', 'constraints')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
