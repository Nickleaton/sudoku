import unittest

from src.commands.simple_command import SimpleCommand
from tests.commands.test_command import TestCommand


class TestComposedCommand(TestCommand):

    def setUp(self) -> None:
        super().setUp()
        self.command = SimpleCommand() | SimpleCommand() | SimpleCommand()

    @property
    def representation(self) -> str:
        return "ComposedCommand([SimpleCommand(), SimpleCommand(), SimpleCommand()])"

    def test_len(self):
        self.assertEqual(3, len(self.command))

    def test_iteration(self):
        count = 0
        for _ in self.command:
            count += 1
        self.assertEqual(3, count)

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
