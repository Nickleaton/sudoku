import unittest
from pathlib import Path

from src.commands.lp_command import LPCommand
from tests.commands.test_command import TestCommand


class TestLPCommand(TestCommand):

    def setUp(self) -> None:
        self.command = LPCommand(Path('problems\\easy\\problem001.yaml'))

    def test_command(self):
        self.command.execute()
        self.assertIsNotNone(self.command.output)

    @property
    def representation(self) -> str:
        return r"LPCommand('problems\easy\problem001.yaml')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
