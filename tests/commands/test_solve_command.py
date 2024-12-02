"""TestSolveCommand."""
import unittest
from pathlib import Path

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_linear_program_command import CreateLinearProgramCommand
from src.commands.create_solver_command import CreateSolverCommand
from src.commands.file_reader_command import FileReaderCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.solve_command import SolveCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestSolveCommand(TestSimpleCommand):
    """Test suite for SolveCommand class."""

    def setUp(self) -> None:
        """Set up the test environment for SolveCommand."""
        super().setUp()
        self.prerequisites = FileReaderCommand(file_name='config_file_name',
                                               target='config_text',
                                               file_path=Path('problems\\easy\\problem001.yaml')) \
                             | LoadConfigCommand() \
                             | CreateBoardCommand() \
                             | CreateConstraintsCommand() \
                             | CreateSolverCommand() \
                             | CreateLinearProgramCommand()
        self.prerequisites.execute(self.problem)
        self.command = SolveCommand()
        self.requirements = ['solver']
        self.target = "solution"
        self.representation = "SolveCommand('solver', 'solution')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
