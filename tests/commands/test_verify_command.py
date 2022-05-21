import os
import unittest

from src.commands.verify_command import VerifyCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestVerifycommand(TestSimpleCommand):

    def setUp(self) -> None:
        self.command = VerifyCommand(
            os.path.join('problems', 'problem001.yaml'),
            os.path.join('output', 'solution', 'problem001.txt')
        )

    @property
    def representation(self) -> str:
        return r"VerifyCommand('problems\problem001.yaml', 'output\solution\problem001.txt')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
