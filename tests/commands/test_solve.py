import os
import unittest

from src.commands.solve import Solve
from tests.commands.test_command import TestCommand


class TestLPcommand(TestCommand):

    def setUp(self) -> None:
        self.command = Solve(
            os.path.join('problems', 'problem001.yaml'),
            os.path.join('output', 'solution', 'problem001.txt')
        )


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
