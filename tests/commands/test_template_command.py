"""TestTemplateCommand."""
import unittest
from pathlib import Path

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_meta_command import CreateMetaCommand
from src.commands.create_rules_command import CreateRulesCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.svg_problem_command import SVGProblemCommand
from src.commands.template_command import TemplateCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestTemplateCommand(TestSimpleCommand):
    """Test suite for TemplateCommand class."""

    def setUp(self):
        """Set up the test environment for TemplateCommand.

        This method sets up the problem and executes the required commands to
        prepare for testing the TemplateCommand.
        """
        super().setUp()
        self.prerequisites = LoadConfigCommand(self.path) \
                             | CreateMetaCommand() \
                             | CreateBoardCommand() \
                             | CreateConstraintsCommand() \
                             | CreateRulesCommand() \
                             | SVGProblemCommand('problem_svg')
        self.prerequisites.execute(self.problem)
        self.command = TemplateCommand(template=Path('src\\html\\problem.html'), target='html')
        self.requirements = ['config', 'meta', 'board', 'constraints', 'rules', 'problem_svg']
        self.target = "html"

    def test_command(self):
        """Test the execution of TemplateCommand.

        This method checks if the TemplateCommand correctly generates the HTML output
        for the given problem.
        """
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.html)

    @property
    def representation(self):
        """Return the string representation of the TemplateCommand.

        Returns:
            str: The representation of the TemplateCommand instance.
        """
        return "TemplateCommand('src\\\\html\\\\problem.html', 'html')"

    def test_repr(self):
        """Test the __repr__ method of TemplateCommand.

        This method checks if the string representation matches the expected value.
        """
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
