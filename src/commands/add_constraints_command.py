"""AddConstraintsCommand."""
from typing import cast

from src.commands.command import CommandError
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_solver_command import CreateSolverCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.solvers.solver import Solver


class AddConstraintsCommand(SimpleCommand):
    """Command to add constraints."""

    def __init__(self):
        """Construct a AddConstraintsCommand."""
        super().__init__()
        self.add_preconditions([CreateSolverCommand, CreateConstraintsCommand])
        self.target = 'answer'

    def work(self, problem: Problem) -> None:
        """Solve the puzzle.

        Args:
            problem (Problem): The problem to solve.

        Raises:
            CommandError: If the solver is not created.
            CommandError: If the constraints are not created.
        """
        super().work(problem)
        if problem.solver is None:
            raise CommandError(f'Solver must be created before {self.name}.')
        if problem.constraints is None:
            raise CommandError(f'Constraints must be created before {self.name}.')
        solver = cast(Solver, problem.solver)
        problem.constraints.add_constraint(solver)
        solver.save_lp('constraints.lp')
