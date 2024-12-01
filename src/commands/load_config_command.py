"""Load Config File."""
from pathlib import Path

import oyaml as yaml
from pydotted import pydot

from src.commands.command import CommandException
from src.commands.parameter_value_type import ParameterValueType
from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class LoadConfigCommand(SimpleCommand):
    """Load Config into the problem."""

    def __init__(self,
                 source: str = 'config_text',
                 target: str = 'config',
                 ):
        """Initialize LoadConfigCommand.

        Args:
            config_text (str): Name of string containing the config in the problem.
            config_name (str): The name of the variable to store the parsed config in the problem.
        """
        super().__init__()
        self.source: str = source
        self.target: str = target

        self.input_types: list[KeyType] = [
            KeyType(source, str)
        ]
        self.output_types: list[KeyType] = [
            KeyType(target, pydot)
        ]


    def work(self, problem: Problem) -> None:
        """Load the configuration from the YAML file.

        Args:
            problem (Problem): The problem to load the config into.

        Raises:
            CommandException: If an error occurs while loading the config.
        """
        super().work(problem)
        try:
            config_data = yaml.safe_load(problem[self.source])
            problem[self.target] = pydot(config_data)
        except Exception as exc:
            raise CommandException(f"Failed to load {self.source}: {exc}") from exc
