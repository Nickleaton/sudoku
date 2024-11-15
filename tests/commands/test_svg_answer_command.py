"""TestSvgAnswerCommand."""
import unittest

from src.commands.svg_answer_command import SVGAnswerCommand
from src.items.battenburg import Battenburg
from src.items.item import Item
from src.solvers.answer import Answer
from src.utils.coord import Coord
from tests.commands.test_svg_command import TestSVGCommand


class SVGTestAnswerCommand(TestSVGCommand):
    """Test suite for SVGAnswerCommand class."""

    def setUp(self) -> None:
        """Set up the test environment for SVGAnswerCommand."""
        super().setUp()
        self.problem.answer = Answer(
            self.problem.board,
            [
                "123456789",
                "123456789",
                "123456789",
                "123456789",
                "123456789",
                "123456789",
                "123456789",
                "123456789",
                "123456789"
            ]
        )
        self.command = SVGAnswerCommand('svg')

    @property
    def in_select(self) -> Answer | None:
        """Return the input answer for the command."""
        return self.problem.answer

    @property
    def out_select(self) -> Item | None:
        """Return the expected output item for the command."""
        return Battenburg(self.problem.board, Coord(2, 2))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
