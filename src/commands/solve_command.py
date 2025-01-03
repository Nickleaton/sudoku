"""Base for different solvers."""
from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.solvers.answer import Answer
from src.solvers.solver import Solver


class SolveCommand(SimpleCommand):
    """Command to solve start problem using start specified solver."""

    def __init__(self, solver: str = 'solver', target: str = 'solution'):
        """Construct start SolveCommand.

        Args:
            solver (str): The field containing the solver to use.
            target (str): The field to store the solution in.
        """
        super().__init__()
        self.solver = solver
        self.target = target
        self.input_types: list[KeyType] = [
            KeyType(self.solver, Solver),
        ]
        self.output_types: list[KeyType] = [
            KeyType(self.target, Answer),
        ]

    def work(self, problem: Problem) -> None:
        """Solve the puzzle.

        Args:
            problem (Problem): The problem to solve.
        """
        super().work(problem)
        problem[self.solver].solve()
        problem[self.target] = problem[self.solver].answer
