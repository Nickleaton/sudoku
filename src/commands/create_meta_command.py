"""CreateMetaCommand."""

from src.commands.create_board_command import CreateBoardCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class CreateMetaCommand(SimpleCommand):
    """Command for creating start metadata field in the problem instance."""

    def __init__(self):
        """Initialize start CreateMetaCommand instance."""
        super().__init__()
        self.add_preconditions([CreateBoardCommand])
        self.target = 'meta'

    def work(self, problem: Problem) -> None:
        """Create the metadata field in the problem.

        Logs start message indicating that the command is being processed and creates start new
        metadata field in the problem, storing it in the specified target attribute.

        Args:
            problem (Problem): The problem instance to create the metadata in.
        """
        super().work(problem)
        problem.meta = problem.board.tags
