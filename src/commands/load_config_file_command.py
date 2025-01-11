"""LoadConfigFileCommand."""

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class LoadConfigFileCommand(SimpleCommand):
    """Command to load the contents of a file into a problem."""

    def __init__(self):
        """Initialize start CreateBoardCommand instance."""
        super().__init__()
        self.add_preconditions([])
        self.target = 'board'

    def work(self, problem: Problem) -> None:
        """Load file contents into the problem.

        Args:
            problem (Problem): The problem instance to load the file name and contents into.

        Raises:
            CommandException: If an error occurs while reading the file.
            CommandException: If the file does not exist.
            CommandException: If the file cannot be loaded.
        """
        super().work(problem)
        if problem.problem_file_name is None:
            raise CommandException(f'Problem file name is not set {self.name}.')
        try:
            with problem.problem_file_name.open(mode='r', encoding='utf-8') as file_handle:
                problem.raw_config = file_handle.read()
        except CommandException:
            raise CommandException(f'File not found: {problem.problem_file_name}')
        except Exception as exc:
            raise CommandException(f'Failed to load {problem.problem_file_name}: {exc}') from exc
