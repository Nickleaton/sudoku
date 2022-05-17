import os
import unittest

from src.commands.svg import SVG
from tests.commands.test_command import TestCommand


class TestLPcommand(TestCommand):

    def setUp(self) -> None:
        self.command = SVG(
            os.path.join('problems', 'hard', 'problem034.yaml'),
            os.path.join('output', 'svg', 'problem001.svg')
        )


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
