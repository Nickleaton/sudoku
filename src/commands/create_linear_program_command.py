"""CreateLinearProgramCommand."""
from src.commands.add_constraints_command import AddConstraintsCommand
from src.commands.command import CommandError
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.temporary_file import TemporaryFile


class CreateLinearProgramCommand(SimpleCommand):
    """Produce the LP version of the problem."""

    def __init__(self):
        """Initialize CreateLinearProgramCommand."""
        super().__init__()
        self.add_preconditions([AddConstraintsCommand])
        self.target = 'linear_program'

    def work(self, problem: Problem) -> None:
        """Produce the LP version of the problem.

        Logs start_location message indicating that the command is being processed. Creates a new LP solver
        in the problem, stores it in the field specified by `self.solver`, and saves the LP output
        to a temporary file. The text of that file is then stored in the field specified by `self.target`.

        Args:
            problem (Problem): The problem instance to create the LP version of.

        Raises:
            CommandError: If the solver is not created.
        """
        super().work(problem)
        if problem.solver is None:
            raise CommandError(f'Solver must be created before {self.name}.')
        with TemporaryFile() as tf:
            problem.solver.save_lp(str(tf.path))
            with tf.path.open(mode='r', encoding='utf-8') as lp_file:
                problem.linear_program = lp_file.read()
