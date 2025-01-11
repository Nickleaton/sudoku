"""TestTemplateCommand."""
import unittest

from src.commands.render_template_command import RenderTemplateCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestRenderTemplateCommand(TestSimpleCommand):
    """Test suite for TemplateCommand class."""

    def setUp(self):
        """Set up the test environment for TemplateCommand.

        This method sets up the problem and executes the required commands to
        prepare for testing the TemplateCommand.
        """
        super().setUp()
        self.command = RenderTemplateCommand()
        self.representation = r"RenderTemplateCommand()"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
