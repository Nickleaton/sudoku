import os
import unittest

from src.commands.html import HTML
from tests.commands.test_command import TestCommand


class TestLPcommand(TestCommand):

    def setUp(self) -> None:
        self.command = HTML(
            os.path.join('problems', 'problem001.yaml'),
            os.path.join('output', 'svg', 'problem001.html')
        )


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
