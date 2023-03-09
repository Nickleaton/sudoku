import os
import unittest

from src.commands.solve_command import SolveCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestSolveCommand(TestSimpleCommand):

    def setUp(self) -> None:
        self.command = SolveCommand(
            os.path.join('problems', 'easy', 'problem001.yaml'),
            os.path.join('output', 'solution', 'problem001.txt')
        )

    @property
    def representation(self) -> str:
        return r"SolveCommand('problems\easy\problem001.yaml', 'output\solution\problem001.txt')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
