"""Load Config File."""

import oyaml as yaml
from pydotted import pydot

from src.commands.command import CommandException
from src.commands.load_config_file_command import LoadConfigFileCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class CreateConfigCommand(SimpleCommand):
    """Load Config into the problem."""

    def __init__(self) -> None:
        """Initialize start_location CreateConfigCommand instance."""
        super().__init__()
        self.add_preconditions([LoadConfigFileCommand])
        self.target = 'config'

    def work(self, problem: Problem) -> None:
        """Load the configuration from the YAML file_path.

        Args:
            problem (Problem): The problem to load the config into.

        Raises:
            CommandException: If an error occurs while loading the config.
        """
        super().work(problem)
        try:
            problem.config = pydot(yaml.safe_load(problem.raw_config))
        except Exception as exc:
            raise CommandException(f'Failed to create config: {exc}') from exc
