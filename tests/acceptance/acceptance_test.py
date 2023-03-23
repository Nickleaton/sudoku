import os
import unittest
from pathlib import Path
from typing import Optional

from src.commands.bookkeeping_png_command import BookkeepingPNGCommand
from src.commands.html_command import HTMLCommand
from src.commands.lp_command import LPCommand
from src.commands.solve_command import SolveCommand
from src.commands.svg_command import SVGCommand
from src.commands.verify_command import VerifyCommand
from src.items.solution import Solution


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
    def yaml_filename(self) -> Optional[Path]:
        if self.name is None:
            return None
        return Path("problems") / Path("easy") / Path(self.name + ".yaml")

    @property
    def svg_filename(self) -> Optional[Path]:
        if self.name is None:
            return None
        return AcceptanceTest.DIRECTORY / self.name / "problem.svg"

    @property
    def html_filename(self) -> Optional[Path]:
        if self.name is None:
            return None
        return AcceptanceTest.DIRECTORY / self.name / Path("problem.html")

    @property
    def lp_filename(self) -> Optional[Path]:
        if self.name is None:
            return None
        return AcceptanceTest.DIRECTORY / self.name / Path("problem.lp")

    @property
    def solution_filename(self) -> Optional[Path]:
        if self.name is None:
            return None
        return AcceptanceTest.DIRECTORY / self.name / Path("solution.txt")

    @property
    def verify_filename(self) -> Optional[Path]:
        if self.name is None:
            return None
        return AcceptanceTest.DIRECTORY / self.name / Path("verify.txt")

    @property
    def png_problem_filename(self) -> Optional[Path]:
        if self.name is None:
            return None
        return AcceptanceTest.DIRECTORY / self.name / Path("problem.png")

    @property
    def png_solution_filename(self) -> Optional[Path]:
        if self.name is None:
            return None
        return AcceptanceTest.DIRECTORY / self.name / Path("solution.png")

    @property
    def png_bookkeeping_filename(self) -> Optional[Path]:
        if self.name is None:
            return None
        return AcceptanceTest.DIRECTORY / self.name / Path("bookkeeping.png")

    def test_svg(self) -> None:
        if self.name is None:
            return
        AcceptanceTest.check_directory(self.svg_filename)
        command = SVGCommand(self.yaml_filename)
        command.process()
        self.assertIsNotNone(command.output)

    def test_html(self) -> None:
        if self.name is None:
            return
        AcceptanceTest.check_directory(self.html_filename)
        command = HTMLCommand(self.yaml_filename)
        command.process()
        self.assertIsNotNone(command.output)

    def test_lp(self) -> None:
        if self.name is None:
            return
        AcceptanceTest.check_directory(self.lp_filename)
        command = LPCommand(self.yaml_filename)
        command.process()

    def test_solve(self) -> None:
        if self.name is None:
            return
        AcceptanceTest.check_directory(self.solution_filename)
        command = SolveCommand(self.yaml_filename)
        command.process()
        expected = None
        for item in command.config['Constraints']:
            if 'Solution' in item:
                expected = Solution.create(command.board, item)
        if expected is not None:
            print(type(expected), type(command.solution))
            self.assertEqual(expected, command.solution)

    def test_verify(self) -> None:
        if self.name is None:
            return
        AcceptanceTest.check_directory(self.verify_filename)
        command = VerifyCommand(self.yaml_filename)
        command.process()
        expected = None
        # command.dump_variables()
        for item in command.config['Constraints']:
            if 'Solution' in item:
                expected = Solution.create(command.board, item)
        if expected is not None:
            self.assertEqual(expected, command.solution)

    # def test_problem_png(self) -> None:
    #     if self.name is None:
    #         return
    #     AcceptanceTest.check_directory(self.png_problem_filename)
    #     command = ProblemPNGCommand(self.yaml_filename, self.png_problem_filename)
    #     command.process()
    #     command.write()

    # def test_solution_png(self) -> None:
    #     if self.name is None:
    #         return
    #     AcceptanceTest.check_directory(self.png_solution_filename)
    #     command = SolutionPNGCommand(self.yaml_filename, self.png_problem_filename)
    #     command.process()
    #     command.write()

    def test_bookkeeping_png(self) -> None:
        if self.name is None:
            return
        AcceptanceTest.check_directory(self.png_bookkeeping_filename)
        command = BookkeepingPNGCommand(self.yaml_filename)
        command.process()
        self.assertIsNotNone(command.output)

    def test_open_files(self) -> None:
        pass
