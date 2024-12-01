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
        self.command = TemplateCommand(template_file=Path('src\\html\\problem.html'), target='html')
        self.requirements = ['config', 'meta', 'board', 'constraints', 'rules', 'problem_svg']
        self.target = "html"
        self.representation = r"TemplateCommand('problem.html', 'html')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
