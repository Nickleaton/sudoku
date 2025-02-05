"""TestComposedCommand."""
import unittest

from src.commands.null_command import NullCommand
from tests.commands.test_command import TestCommand


class TestComposedCommand(TestCommand):
    """Test suite for the ComposedCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = NullCommand() | NullCommand() | NullCommand()
        self.representation = "ComposedCommand([NullCommand(), NullCommand(), NullCommand()])"

    def test_len(self):
        """Test the length of the ComposedCommand."""
        self.assertEqual(3, len(self.command))

    def test_iteration(self):
        """Test the iteration over the ComposedCommand."""
        count = 0
        for _ in self.command:
            count += 1
        self.assertEqual(3, count)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
