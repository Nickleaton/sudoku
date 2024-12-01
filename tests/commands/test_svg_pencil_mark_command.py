"""TestSvgPencilMarkCommand."""
import unittest

from src.commands.svg_pencil_mark_command import SVGPencilMarkCommand
from tests.commands.test_svg_command import TestSVGCommand


class TestSVGPencilMarkCommand(TestSVGCommand):
    """Test suite for SVGPencilMarkCommand class."""

    def setUp(self) -> None:
        """Set up the test environment for SVGPencilMarkCommand."""
        super().setUp()
        self.command = SVGPencilMarkCommand('svg')
        self.representation = r"SVGPencilMarkCommand('svg', 'constraints', 'svg')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
