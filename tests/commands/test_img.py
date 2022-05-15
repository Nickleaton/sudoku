import os
import unittest

from src.commands.img import IMG
from tests.commands.test_command import TestCommand


class TestLPcommand(TestCommand):

    def setUp(self) -> None:
        self.command = IMG(
            os.path.join('problems', 'problem001.yaml'),
            os.path.join('output', 'jpg', 'problem001.jpg')
        )


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
