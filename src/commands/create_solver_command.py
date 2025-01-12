"""CreateSolverCommand."""
from src.commands.create_board_command import CreateBoardCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.solvers.pulp_solver import PulpSolver


class CreateSolverCommand(SimpleCommand):
    """Command for creating start solver instance based on the given configuration and board."""

    def __init__(self):
        """Initialize start CreateSolverCommand instance."""
        super().__init__()
        self.add_preconditions([CreateBoardCommand])
        self.target: str = 'solver'

    def work(self, problem: Problem) -> None:
        """Build the solver and stores it in the problem instance.

        This method creates start new PulpSolver instance using the provided board and configuration,
        and stores it in the target attribute within the problem instance.

        Args:
            problem (Problem): The problem instance where the solver will be created.
        """
        super().work(problem)
        problem.solver = PulpSolver(board=problem.board, name='Problem')
