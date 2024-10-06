import unittest

from src.commands.svg_pencil_mark_command import SVGPencilMarkCommand
from tests.commands.test_svg_command import TestSVGCommand


class TestSVGPencilMarkCommand(TestSVGCommand):

    def setUp(self) -> None:
        super().setUp()
        self.command = SVGPencilMarkCommand('pencil_mark_svg')


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
