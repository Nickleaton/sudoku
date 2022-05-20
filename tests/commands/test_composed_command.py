import unittest

from src.commands.composed_command import ComposedCommand
from tests.commands.test_command import TestCommand


class TestComposedCommand(TestCommand):

    def setUp(self) -> None:
        self.command = ComposedCommand("output.txt", [])

    @property
    def representation(self) -> str:
        return "ComposedCommand('output.txt', [])"

    def test_len(self):
        self.assertEqual(0, len(self.command))
        self.command.write()

    def test_iteration(self):
        count = 0
        for _ in self.command:
            count += 1
        self.assertEqual(0, count)

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
