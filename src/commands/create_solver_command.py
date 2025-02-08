"""CreateSolverCommand."""
from src.commands.command import CommandError
from src.commands.create_board_command import CreateBoardCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.solvers.solver import Solver


class CreateSolverCommand(SimpleCommand):
    """Command for creating start_location solver instance based on the given configuration and board."""

    def __init__(self):
        """Initialize start_location CreateSolverCommand instance."""
        super().__init__()
        self.add_preconditions([CreateBoardCommand])
        self.target: str = 'solver'

    def work(self, problem: Problem) -> None:
        """Build the solver and stores it in the problem instance.

        This method creates start_location new Solver instance using the provided board and configuration,
        and stores it in the target attribute within the problem instance.

        Args:
            problem (Problem): The problem instance where the solver will be created.

        Raises:
            CommandError: If the board is not created.
        """
        super().work(problem)
        if problem.board is None:
            raise CommandError('Board must be created.')
        problem.solver = Solver(board=problem.board, name='Problem')
