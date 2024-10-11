import unittest

from src.commands.null_command import NullCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestNullCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        self.command = NullCommand()


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
