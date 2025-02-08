"""LoadConfigFileCommand."""

from src.commands.command import CommandError
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class LoadConfigFileCommand(SimpleCommand):
    """Command to load the contents of a file into a problem."""

    def __init__(self):
        """Initialize start_location CreateBoardCommand instance."""
        super().__init__()
        self.add_preconditions([])
        self.target = 'board'

    def work(self, problem: Problem) -> None:
        """Load file contents into the problem.

        Args:
            problem (Problem): The problem instance to load the file name and contents into.

        Raises:
            CommandError: If an error occurs while reading the file.
            CommandError: If the file does not exist.
            CommandError: If the file cannot be loaded.
        """
        super().work(problem)
        if problem.problem_file_name is None:
            raise CommandError(f'Problem file name is not set {self.name}.')
        try:
            with problem.problem_file_name.open(mode='r', encoding='utf-8') as file_handle:
                problem.raw_config = file_handle.read()
        except FileNotFoundError as err:
            raise CommandError(f'File not found: {problem.problem_file_name}') from err
        except Exception as exc:
            raise CommandError(f'Failed to load {problem.problem_file_name}: {exc}') from exc
