"""TestSvgProblemCommand."""
import unittest

from src.commands.svg_problem_command import SVGProblemCommand
from tests.commands.test_svg_command import TestSVGCommand


class TestSVGProblemCommand(TestSVGCommand):
    """Test suite for SVGProblemCommand class."""

    def setUp(self) -> None:
        """Set up the test environment for SVGProblemCommand."""
        super().setUp()
        self.command = SVGProblemCommand()
        self.representation = r"SVGProblemCommand('board', 'constraints', 'svg')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
