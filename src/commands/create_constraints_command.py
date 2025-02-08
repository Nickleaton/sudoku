"""CreateConstraintsCommand."""
from src.commands.command import CommandError
from src.commands.create_board_command import CreateBoardCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.constraints import Constraints


class CreateConstraintsCommand(SimpleCommand):
    """Build the constraints for the problem."""

    def __init__(self):
        """Initialize the command."""
        super().__init__()
        self.add_preconditions([CreateBoardCommand])
        self.target = 'constraints'

    def work(self, problem: Problem) -> None:
        """Execute the command to create constraints.

        Args:
            problem (Problem): The problem instance where constraints will be created and added.

        Raises:
            CommandError: If the board is not created.
            CommandError: If the config is not set.
        """
        super().work(problem)
        if problem.board is None:
            raise CommandError('Board must be created.')
        if problem.config is None:
            raise CommandError('Config must be set.')
        problem.constraints = Constraints.create(
            problem.board,
            {'Constraints': problem.config['Constraints']},
        )
