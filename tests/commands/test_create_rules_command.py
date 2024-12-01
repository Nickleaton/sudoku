"""TestCreateRulesCommand."""
import unittest
from pathlib import Path

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_rules_command import CreateRulesCommand
from src.commands.file_reader_command import FileReaderCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateRulesCommand(TestSimpleCommand):
    """Test suite for the CreateRulesCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.prerequisites = FileReaderCommand(file_name='config_file_name',
                                               target='config_text',
                                               file_path=Path('problems\\easy\\problem001.yaml')) \
                             | LoadConfigCommand() \
                             | CreateBoardCommand() \
                             | CreateConstraintsCommand()
        self.prerequisites.execute(self.problem)
        self.command = CreateRulesCommand()
        self.representation = "CreateRulesCommand('constraints', 'rules')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
