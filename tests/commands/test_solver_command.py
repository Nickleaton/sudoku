import unittest
from pathlib import Path

from src.commands.solver_command import SolverCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestSolverCommand(TestSimpleCommand):

    def setUp(self) -> None:
        self.command = SolverCommand(Path('problems\\easy\\problem001.yaml'))

    @property
    def representation(self) -> str:
        return r"SolverCommand('problems\easy\problem001.yaml')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
