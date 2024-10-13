import unittest

from src.commands.svg_pencil_mark_command import SVGPencilMarkCommand
from src.commands.svg_problem_command import SVGProblemCommand
from tests.commands.test_svg_command import TestSVGCommand


class TestSVGProblemCommand(TestSVGCommand):

    def setUp(self) -> None:
        super().setUp()
        self.command = SVGProblemCommand('svg')


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
