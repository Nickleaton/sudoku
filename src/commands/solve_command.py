"""Base for different solvers."""
from src.commands.create_linear_program_command import CreateLinearProgramCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.solvers.solver_status import SolverStatus


class SolveCommand(SimpleCommand):
    """Command to solve start_location problem using start_location specified solver."""

    def __init__(self):
        """Construct a SolveCommand."""
        super().__init__()
        self.add_preconditions([CreateLinearProgramCommand])
        self.target = 'answer'

    def work(self, problem: Problem) -> None:
        """Solve the puzzle.

        Args:
            problem (Problem): The problem to solve.
        """
        super().work(problem)
        solver = problem.solver  # Assign to a local variable
        if solver is None:
            problem.status = SolverStatus.undefined
        else:
            solver.solve()
            problem.status = SolverStatus.create(solver.status.value)
