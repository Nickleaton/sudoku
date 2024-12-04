"""YamlToStringCommand."""
import logging
from pathlib import Path

import oyaml as yaml
import pydotted

from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand

# Register None-type representation in YAML as an empty string
yaml.add_representer(type(None), lambda self, _: self.represent_scalar('tag:yaml.org,2002:null', ''))


class YamlToStringCommand(SimpleCommand):
    """Write configuration data to a YAML file."""

    def __init__(self, source: str = 'config', target: str = 'config_out') -> None:
        """Initialize a YamlToStringCommand instance.

        Args:
            source (str): The attribute of the problem containing the configuration data.
            target (str): The part of problem to write the yaml string to.
        """
        super().__init__()
        self.source: str = source
        self.target: str = target
        self.input_types: list[KeyType] = [
            KeyType(self.source, pydotted.pydot)
        ]
        self.output_types: list[KeyType] = [
            KeyType(str(self.target), str)
        ]

    def work(self, problem: Problem) -> None:
        """Write the configuration to the target string.

        Args:
            problem (Problem): The problem instance containing the configuration data.

        Raises:
            CommandException: If the target is not writable or the configuration
                              is missing from the problem.
        """
        super().work(problem)
        logging.info(f"Creating {self.target}")
        problem[self.target] = yaml.dump(problem[self.source],  default_style=None)
