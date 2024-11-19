"""TestCreateRulesCommand."""
import unittest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_rules_command import CreateRulesCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateRulesCommand(TestSimpleCommand):
    """Test suite for the CreateRulesCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.prerequisites = LoadConfigCommand(self.path) \
                       | CreateBoardCommand() \
                       | CreateConstraintsCommand()
        self.prerequisites.execute(self.problem)
        self.command = CreateRulesCommand()
        self.requirements = ['config', 'board', 'constraints']
        self.target = "rules"

    def test_command(self):
        """Test the execute method of CreateRulesCommand."""
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.rules)

    @property
    def representation(self) -> str:
        """Return the string representation of the CreateRulesCommand."""
        return "CreateRulesCommand('constraints', 'rules')"

    def test_repr(self):
        """Test the string representation of the command."""
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
