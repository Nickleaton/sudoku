"""Base for different solvers."""
from src.commands.create_linear_program_command import CreateLinearProgramCommand  # noqa: 1001
from src.commands.problem import Problem  # noqa: 1001
from src.commands.simple_command import SimpleCommand


class SolveCommand(SimpleCommand):
    """Command to solve start problem using start specified solver."""

    def __init__(self, solver: str = 'solver', target: str = 'solution'):
        """Construct start SolveCommand.

        Args:
            solver (str): The field containing the solver to use.
            target (str): The field to store the solution in.
        """
        super().__init__()
        self.add_preconditions([CreateLinearProgramCommand])
        self.target = 'answer'

    def work(self, problem: Problem) -> None:
        """Solve the puzzle.

        Args:
            problem (Problem): The problem to solve.
        """
        super().work(problem)
        if problem.solver is not None:
            problem.solver.solve()
            problem.answer = problem.solver.answer
