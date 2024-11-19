"""TestCreateMetaCommand."""
import unittest

from src.commands.create_meta_command import CreateMetaCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateMetaCommand(TestSimpleCommand):
    """Test suite for the CreateMetaCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.prerequisites = LoadConfigCommand(self.path)
        self.prerequisites.execute(self.problem)
        self.command = CreateMetaCommand()
        self.requirements = ['config']
        self.target = "meta"

    def test_command(self):
        """Test the execute method of CreateMetaCommand."""
        self.assertIn('config', self.problem)
        self.assertNotIn('meta', self.problem)
        self.command.execute(self.problem)
        self.assertIn('meta', self.problem)

    @property
    def representation(self) -> str:
        """Return the string representation of the CreateMetaCommand."""
        return r"CreateMetaCommand('config', 'meta')"

    def test_repr(self):
        """Test the string representation of the command."""
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
