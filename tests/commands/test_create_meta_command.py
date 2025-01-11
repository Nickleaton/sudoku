"""TestCreateMetaCommand."""
import unittest

from src.commands.create_meta_command import CreateMetaCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateMetaCommand(TestSimpleCommand):
    """Test suite for the CreateMetaCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = CreateMetaCommand()
        self.representation = 'CreateMetaCommand()'


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
