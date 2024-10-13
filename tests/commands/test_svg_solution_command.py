import unittest

from src.commands.svg_solution_command import SVGSolutionCommand
from src.items.battenburg import Battenburg
from src.items.item import Item
from src.items.solution import Solution
from src.utils.coord import Coord
from tests.commands.test_svg_command import TestSVGCommand


class SVGTestSolutionCommand(TestSVGCommand):

    def setUp(self) -> None:
        super().setUp()
        self.command = SVGSolutionCommand('svg')

    @property
    def in_select(self) -> Item | None:
        return Solution(self.problem.board, ["123456789", "123456789", "123456789", "123456789", "123456789", "123456789", "123456789", "123456789", "123456789"])

    @property
    def out_select(self) -> Item | None:
        return Battenburg(self.problem.board, Coord(2, 2))

if __name__ == '__main__':  # pragma: no cover
    unittest.main()
