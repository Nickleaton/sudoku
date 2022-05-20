import os
import unittest

from src.commands.solve import Solve
from tests.commands.test_simple_command import TestSimpleCommand


class TestLPcommand(TestSimpleCommand):

    def setUp(self) -> None:
        self.command = Solve(
            os.path.join('problems', 'problem001.yaml'),
            os.path.join('output', 'solution', 'problem001.txt')
        )

    @property
    def representation(self) -> str:
        return r"Solve('problems\problem001.yaml', 'output\solution\problem001.txt')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
