"""CreateConstraintsCommand."""
from src.commands.command import CommandException
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

    def work(self, problem: Problem) -> None:
        """Execute the command to create constraints.

        Args:
            problem (Problem): The problem instance where constraints will be created and added.

        Raises:
            CommandException: If the board is not created.
            CommandException: If the config is not set.
        """
        super().work(problem)
        if problem.board is None:
            raise CommandException('Board must be created.')
        if problem.config is None:
            raise CommandException('Config must be set.')
        problem.constraints = Constraints.create(
            problem.board,
            {'Constraints': problem.config['Constraints']},
        )
