import os
import unittest

from src.commands.lp import LP
from tests.commands.test_command import TestCommand


class TestLPcommand(TestCommand):

    def setUp(self) -> None:
        self.command = LP(os.path.join('problems', 'problem001.yaml'), os.path.join('output', 'lp', 'problem001.lp'))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
