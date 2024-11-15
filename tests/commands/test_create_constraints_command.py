"""TestCreateConstraintsCommand."""
import unittest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.load_config_command import LoadConfigCommand
from src.items.item import Item
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateConstraintsCommand(TestSimpleCommand):
    """Test suite for the CreateConstraintsCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        requirements = LoadConfigCommand(self.path) \
                       | CreateBoardCommand()
        requirements.execute(self.problem)
        self.command = CreateConstraintsCommand()

    @property
    def representation(self) -> str:
        """Return the string representation of the CreateConstraintsCommand."""
        return "CreateConstraintsCommand('config', 'board', 'constraints')"

    def test_repr(self):
        """Test the __repr__ method of the CreateConstraintsCommand."""
        self.assertEqual(self.representation, repr(self.command))

    def test_execute(self):
        """Test the execute method of the CreateConstraintsCommand."""
        self.assertIsNotNone(self.problem.config)
        self.assertIsNotNone(self.problem.board)
        self.assertIsNone(self.problem.constraints)

        self.command.execute(self.problem)

        self.assertIsNotNone(self.problem.constraints)
        self.assertIsInstance(self.problem.constraints, Item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
