"""TestTemplateCommand."""
import unittest
from pathlib import Path

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_meta_command import CreateMetaCommand
from src.commands.create_rules_command import CreateRulesCommand
from src.commands.create_template_command import CreateTemplateCommand
from src.commands.file_reader_command import FileReaderCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.render_template_command import RenderTemplateCommand
from src.commands.svg_problem_command import SVGProblemCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestRenderTemplateCommand(TestSimpleCommand):
    """Test suite for TemplateCommand class."""

    def setUp(self):
        """Set up the test environment for TemplateCommand.

        This method sets up the problem and executes the required commands to
        prepare for testing the TemplateCommand.
        """
        super().setUp()
        self.prerequisites = FileReaderCommand(file_name='config_file_name',
                                               target='config_text',
                                               file_path=Path('problems\\easy\\problem001.yaml')) \
                             | LoadConfigCommand() \
                             | CreateBoardCommand() \
                             | CreateMetaCommand() \
                             | CreateConstraintsCommand() \
                             | CreateRulesCommand() \
                             | SVGProblemCommand(target='problem_svg') \
                             | FileReaderCommand(file_name='problem_raw_file_name',
                                                 target='raw_template_text',
                                                 file_path=Path('src/html/problem.html')) \
                             | CreateTemplateCommand(source='raw_template_text', target='problem_raw_template')

        self.prerequisites.execute(self.problem)
        self.command = RenderTemplateCommand(template_name="problem_raw_template", target="html")
        self.representation = r"RenderTemplateCommand('problem_raw_template', 'html')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
