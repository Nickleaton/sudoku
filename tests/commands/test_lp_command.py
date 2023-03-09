import os
import unittest

from src.commands.lp_command import LPCommand
from tests.commands.test_command import TestCommand


class TestLPCommand(TestCommand):

    def setUp(self) -> None:
        self.command = LPCommand(
            os.path.join('problems', 'easy', 'problem001.yaml'),
            os.path.join('output', 'lp', 'problem001.lp')
        )

    def test_command(self):
        self.command.process()
        self.assertEqual(r"output\lp\problem001.lp", self.command.output_filename)
        self.command.write()

    @property
    def representation(self) -> str:
        return r"LPCommand('problems\easy\problem001.yaml', 'output\lp\problem001.lp')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
