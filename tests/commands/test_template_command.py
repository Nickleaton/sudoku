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

    def setUp(self) -> None:
        super().setUp()
        setup_command = LoadConfigCommand(self.path) \
            | CreateMetaCommand() \
            | CreateBoardCommand() \
            | CreateConstraintsCommand() \
            | CreateRulesCommand() \
            | SVGProblemCommand('problem_svg')
        setup_command.execute(self.problem)
        self.command = TemplateCommand(template=Path('src\\html\\problem.html'), target='html')


    def test_command(self):
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.html)
        print(self.problem.html)


    @property
    def representation(self) -> str:
        return "TemplateCommand('src\\html\\problem.html', 'html')"


    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
