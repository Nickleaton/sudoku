import os
import unittest

from src.commands.img_command import IMGCommand
from src.commands.svg_command import SVGCommand
from tests.commands.test_command import TestCommand


class TestIMGCommand(TestCommand):

    def setUp(self) -> None:
        self.command = IMGCommand(
            os.path.join('output', 'jpg', 'problem001.jpg'),
            SVGCommand(os.path.join('problems', 'problem001.yaml'))
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
