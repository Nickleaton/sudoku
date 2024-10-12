import os
import unittest
from pathlib import Path
from typing import Optional

from src.commands.composed_command import ComposedCommand
from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_problem_command import CreateProblemCommand
from src.commands.file_writer_command import FileWriterCommand
from src.commands.html_command import HTMLCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.lp_command import CreateLPCommand
from src.commands.solver_command import SolveCommand
from src.commands.svg_command import SVGCommand
from src.utils.config import Config

config = Config()


class AcceptanceTest(unittest.TestCase):
    DIRECTORY = Path("test_results")

    def setUp(self) -> None:
        self.name = None

    @staticmethod
    def check_directory(filename: Optional[str]) -> None:
        if filename is None:
            return
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

    @property
    def config_file_name(self) -> Optional[Path]:
        return Path("problems") / Path("easy") / Path(self.name + ".yaml")

    @property
    def log_file_name(self) -> Optional[Path]:
        return AcceptanceTest.DIRECTORY / self.name / "problem.log"

    @property
    def svg_file_name(self) -> Optional[Path]:
        return AcceptanceTest.DIRECTORY / self.name / "problem.svg"

    @property
    def html_file_name(self) -> Optional[Path]:
        return AcceptanceTest.DIRECTORY / self.name / Path("problem.html")

    @property
    def lp_file_name(self) -> Optional[Path]:
        return AcceptanceTest.DIRECTORY / self.name / Path("problem.lp")

    @property
    def solution_file_name(self) -> Optional[Path]:
        return AcceptanceTest.DIRECTORY / self.name / Path("solution.txt")

    @property
    def verify_filename(self) -> Optional[Path]:
        return AcceptanceTest.DIRECTORY / self.name / Path("verify.txt")

    @property
    def png_problem_filename(self) -> Optional[Path]:
        return AcceptanceTest.DIRECTORY / self.name / Path("problem.png")

    @property
    def png_solution_filename(self) -> Optional[Path]:
        return AcceptanceTest.DIRECTORY / self.name / Path("solution.png")

    @property
    def png_bookkeeping_filename(self) -> Optional[Path]:
        return AcceptanceTest.DIRECTORY / self.name / Path("bookkeeping.png")

    def test_all(self):
        if self.name is None:
            return
        # remove to make sure we generate
        self.svg_file_name.unlink(missing_ok=True)
        self.html_file_name.unlink(missing_ok=True)
        command = ComposedCommand()
        command.add_with_name('config', LoadConfigCommand(self.config_file_name))
        command.add_with_name('board', CreateBoardCommand())
        command.add_with_name('problem', CreateProblemCommand())
        command.add_with_name('svg', SVGCommand())
        command.add_with_name("html", HTMLCommand(Path(config.templates.html)))
        command.add_with_name("lp", CreateLPCommand())
        command.add_with_name("solver", SolveCommand())
        command.add_with_name("svg_writer", FileWriterCommand(self.svg_file_name, ['svg.output']))
        command.add_with_name("html_writer", FileWriterCommand(self.html_file_name, ['html.output']))
        command.add_with_name("lp_writer", FileWriterCommand(self.lp_file_name, ['lp.output']))
        command.add_with_name("log_writer", FileWriterCommand(self.log_file_name, ['solver.log']))
        command.add_with_name("solution_writer", FileWriterCommand(self.solution_file_name, ['solver.solution_text']))
        command.execute()
        # Check file exists
        self.assertTrue(self.svg_file_name.exists())
        self.assertTrue(self.html_file_name.exists())
        self.assertTrue(self.lp_file_name.exists())
        self.assertTrue(self.log_file_name.exists())
        self.assertTrue(self.solution_file_name.exists())
        self.assertNotEqual('None', str(getattr(command, 'solver').solution))

    # def test_lp(self) -> None:
    #     if self.name is None:
    #         return
    #     AcceptanceTest.check_directory(self.lp_filename)
    #     command = LPCommand(self.yaml_filename)
    #     command.execute()
    #
    # def test_solve(self) -> None:
    #     if self.name is None:
    #         return
    #     AcceptanceTest.check_directory(self.solution_filename)
    #     command = SolveCommand(self.yaml_filename)
    #     command.execute()
    #     expected = None
    #     for item in command.config['Constraints']:
    #         if 'Solution' in item:
    #             expected = Solution.create(command.board, item)
    #     if expected is not None:
    #         print(type(expected), type(command.solution))
    #         self.assertEqual(expected, command.solution)
    #
    # def test_bookkeeping_png(self) -> None:
    #     if self.name is None:
    #         return
    #     AcceptanceTest.check_directory(self.png_bookkeeping_filename)
    #     command = BookkeepingPNGCommand(self.yaml_filename)
    #     command.execute()
    #     self.assertIsNotNone(command.output)
    #
    # def test_open_files(self) -> None:
    #     pass


import logging

logging.basicConfig(level=logging.DEBUG, format='%(name)s %(levelname)s %(message)s')
