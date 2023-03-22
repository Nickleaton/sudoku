import unittest
from pathlib import Path

from src.commands.solve_command import SolveCommand
from tests.commands.test_solver_command import TestSolverCommand


class TestSolveCommand(TestSolverCommand):

    def setUp(self) -> None:
        self.command = SolveCommand(Path('problems\\easy\\problem001.yaml'))

    @property
    def representation(self) -> str:
        return r"SolveCommand('problems\easy\problem001.yaml')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
