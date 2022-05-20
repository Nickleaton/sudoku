import os
import unittest

from src.commands.img import IMG
from src.commands.svg import SVG
from tests.commands.test_command import TestCommand


class TestIMGCommand(TestCommand):

    def setUp(self) -> None:
        self.command = IMG(
            os.path.join('output', 'jpg', 'problem001.jpg'),
            SVG(os.path.join('problems', 'problem001.yaml'))
        )

    @property
    def output(self) -> str:
        return r"output\jpg\problem001.jpg"

    @property
    def representation(self) -> str:
        return r"IMG('output\jpg\problem001.jpg', SVG('problems\problem001.yaml'))"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
