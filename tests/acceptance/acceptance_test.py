import logging
import os
import unittest
from pathlib import Path
from typing import Optional

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_linear_program_command import CreateLinearProgramCommand
from src.commands.create_rules_command import CreateRulesCommand
from src.commands.create_solver_command import CreateSolverCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.problem import Problem
from src.commands.solve_command import SolveCommand
from src.utils.config import Config

config = Config()
logging.basicConfig(level=logging.DEBUG, format='%(name)s %(levelname)s %(message)s')


class AcceptanceTest(unittest.TestCase):
    DIRECTORY = Path("test_results")

    def setUp(self):
        self.name = self._testMethodName.replace("test_", "")
        self.check_directory(str(self.DIRECTORY / self.name))

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

    def run_acceptance_test(self):
        if self.name is None:
            return
        # remove to make sure we generate
        self.svg_file_name.unlink(missing_ok=True)
        self.html_file_name.unlink(missing_ok=True)
        problem = Problem()
        print(self.config_file_name)
        command = LoadConfigCommand(source=self.config_file_name) \
                  | CreateBoardCommand() \
                  | CreateConstraintsCommand() \
                  | CreateRulesCommand() \
                  | CreateSolverCommand() \
                  | CreateLinearProgramCommand() \
                  | SolveCommand()

        command.execute(problem)

        self.assertIsNotNone(problem.config, 'Config not loaded')
        self.assertIsNotNone(problem.board, 'Board not created')
        self.assertIsNotNone(problem.constraints, 'Constraints not created')
        self.assertIsNotNone(problem.linear_program, 'Linear Program not created')
        self.assertIsNotNone(problem.rules, 'Rules not created')
        self.assertIsNotNone(problem.solver, 'Solver not created')


def generate_test_cases():
    """Dynamically create test cases for each YAML file in the problems/easy directory."""
    for problem_file in Path("problems/easy").glob("*89.yaml"):
        problem_name = problem_file.stem
        test_name = f"test_{problem_name}"

        def test_method(self, name=problem_name):
            self.name = name
            self.run_acceptance_test()

        setattr(AcceptanceTest, test_name, test_method)

# Generate all test cases before running unittest
generate_test_cases()

if __name__ == '__main__':
    unittest.main()
