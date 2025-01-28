"""TestImageCommand."""
import unittest

from postponed.src.commands.image_command import ImageCommand, ImageFormat
from tests.commands.test_simple_command import TestSimpleCommand


class TestImageCommand(TestSimpleCommand):
    """Test suite for the ImageCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = ImageCommand(image_format_name="format",
                                    image_format=ImageFormat.SVG,
                                    source="svg",
                                    target="svg_text")
        self.representation = "ImageCommand()"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
