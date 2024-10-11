import unittest
from pathlib import Path

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.img_command import IMGCommand, ImageFormat
from src.commands.load_config_command import LoadConfigCommand
from src.commands.problem import Problem
from src.commands.svg_command import SVGCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestIMGCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        self.problem = Problem()
        load_config_command = LoadConfigCommand(self.path)
        create_board_command = CreateBoardCommand()
        create_constraints_command = CreateConstraintsCommand()
        svg_command = SVGCommand('svg')
        load_config_command.execute(self.problem)
        create_board_command.execute(self.problem)
        create_constraints_command.execute(self.problem)
        svg_command.execute(self.problem)

        self.command = IMGCommand("svg", Path('test.svg'))

    @property
    def representation(self) -> str:
        return "IMGCommand('svg', WindowsPath('test.svg'))"

    def test_execute(self):
        self.assertIsNotNone(self.problem.svg)
        if self.command.target.exists():
            self.command.target.unlink(missing_ok=True)
        self.command.execute(self.problem)
        self.assertTrue(self.command.target.exists())
        # if self.command.file_name.exists():
        #     self.command.file_name.unlink(missing_ok=True)

    def xtest_formats(self):
        for fmt in ImageFormat:
            self.command.image_format = fmt
            self.command.target = Path(f"test.{fmt.name.lower()}")
            print (self.command.target)
            if self.command.target.exists():
                self.command.target.unlink(missing_ok=True)
            self.command.execute(self.problem)
            self.assertTrue(self.command.target.exists())
            if self.command.target.exists():
                self.command.target.unlink(missing_ok=True)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
