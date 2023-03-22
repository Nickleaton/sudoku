import unittest
from pathlib import Path

from src.commands.verify_command import VerifyCommand
from tests.commands.test_solver_command import TestSolverCommand


class TestVerifyCommand(TestSolverCommand):

    def setUp(self) -> None:
        self.command = VerifyCommand(Path('problems\\easy\\problem001.yaml'))

    @property
    def representation(self) -> str:
        return "VerifyCommand('problems\\easy\\problem001.yaml')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
