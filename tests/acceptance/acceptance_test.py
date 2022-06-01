import os
import unittest
from typing import Optional

from src.commands.html_command import HTMLCommand
from src.commands.lp_command import LPCommand
from src.commands.solve_command import SolveCommand
from src.commands.svg_command import SVGCommand
from src.commands.verify_command import VerifyCommand
from src.items.solution import Solution


class AcceptanceTest(unittest.TestCase):

    DIRECTORY = "test_results"

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
    def yaml_filename(self) -> Optional[str]:
        if self.name is None:
            return None
        return os.path.join("problems", self.name + ".yaml")

    @property
    def svg_filename(self) -> Optional[str]:
        if self.name is None:
            return None
        return os.path.join(AcceptanceTest.DIRECTORY, self.name, "problem.svg")

    @property
    def html_filename(self) -> Optional[str]:
        if self.name is None:
            return None
        return os.path.join(AcceptanceTest.DIRECTORY, self.name, "problem.html")

    @property
    def lp_filename(self) -> Optional[str]:
        if self.name is None:
            return None
        return os.path.join(AcceptanceTest.DIRECTORY, self.name, "problem.lp")

    @property
    def solution_filename(self) -> Optional[str]:
        if self.name is None:
            return None
        return os.path.join(AcceptanceTest.DIRECTORY, self.name, "solution.txt")

    @property
    def verify_filename(self) -> Optional[str]:
        if self.name is None:
            return None
        return os.path.join(AcceptanceTest.DIRECTORY, self.name, "verify.txt")

    def test_svg(self) -> None:
        if self.name is None:
            return
        AcceptanceTest.check_directory(self.svg_filename)
        command = SVGCommand(self.yaml_filename, self.svg_filename)
        command.process()
        self.assertIsNotNone(command.output)
        command.write()

    def test_html(self) -> None:
        if self.name is None:
            return
        AcceptanceTest.check_directory(self.html_filename)
        command = HTMLCommand(self.yaml_filename, self.html_filename)
        command.process()
        self.assertIsNotNone(command.output)
        command.write()

    def test_lp(self) -> None:
        if self.name is None:
            return
        AcceptanceTest.check_directory(self.lp_filename)
        command = LPCommand(self.yaml_filename, self.lp_filename)
        command.process()
        command.write()

    def test_solve(self) -> None:
        if self.name is None:
            return
        AcceptanceTest.check_directory(self.solution_filename)
        command = SolveCommand(self.yaml_filename, self.solution_filename)
        command.process()
        command.write()
        expected = None
        for item in command.config['Constraints']:
            if 'Solution' in item:
                expected = Solution.create(command.board, item)
        if expected is not None:
            self.assertEqual(expected, command.solution)

    def test_verify(self) -> None:
        if self.name is None:
            return
        AcceptanceTest.check_directory(self.verify_filename)
        command = VerifyCommand(self.yaml_filename, self.verify_filename)
        command.process()
        command.write()
        expected = None
        for item in command.config['Constraints']:
            if 'Solution' in item:
                expected = Solution.create(command.board, item)
        if expected is not None:
            self.assertEqual(expected, command.solution)
