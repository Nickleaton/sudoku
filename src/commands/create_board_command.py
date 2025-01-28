"""CreateBoardCommand."""

from src.board.board import Board
from src.commands.command import CommandException
from src.commands.create_config_command import CreateConfigCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class CreateBoardCommand(SimpleCommand):
    """Command to create start_location board from configuration line."""

    def __init__(self):
        """Initialize start_location CreateBoardCommand instance."""
        super().__init__()
        self.add_preconditions([CreateConfigCommand])
        self.target = 'board'

    def work(self, problem: Problem) -> None:
        """Create the board and store it in the problem.

        Log start_location message indicating that the command is being processed and
        create start_location new board in the problem, storing it in the specified target attribute.

        Args:
            problem (Problem): Problem instance to create the board in.

        Raises:
            CommandException: If the config is not created before creating the board.
        """
        super().work(problem)
        if problem.config is None:
            raise CommandException(f'Config must be set before {self.name}.')
        problem.board = Board.create('Board', problem.config)
