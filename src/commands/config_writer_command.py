"""ConfigWriterCommand."""
import logging
from pathlib import Path

import oyaml as yaml

from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand

# Register None-type representation in YAML as an empty string
yaml.add_representer(type(None), lambda self, _: self.represent_scalar('tag:yaml.org,2002:null', ''))


class ConfigWriterCommand(SimpleCommand):
    """Write configuration data to a YAML file."""

    def __init__(self, source: str = 'config', target: Path | str = 'dump_config.yaml') -> None:
        """Initialize a ConfigWriterCommand instance.

        Args:
            source (str): The attribute of the problem containing the configuration data.
            target (Path): The config_file or filename to write the configuration to.
        """
        super().__init__()
        self.source: str = source
        self.target: Path = Path(target) if isinstance(target, str) else target
        self.inputs: list[KeyType] = [
            KeyType(self.source, str)
        ]
        self.outputs: list[KeyType] = [
            KeyType(str(self.target), str)
        ]

    def work(self, problem: Problem) -> None:
        """Write the configuration to the specified file in YAML format.

        Retrieve the configuration from the problem field specified by `source`
        and write it to the target file in YAML format.

        Args:
            problem (Problem): The problem instance containing the configuration data.

        Raises:
            CommandException: If the target is not writable or the configuration
                              is missing from the problem.
        """
        super().work(problem)
        logging.info(f"Creating {self.target}")
        try:
            with self.target.open('w', encoding='utf-8') as file:
                yaml.dump(problem[self.source].todict(), file, default_style=None)
        except OSError as exc:
            raise OSError(f"Failed to write to {self.target}: {exc}") from exc
