"""ConfigWriterCommand."""
import logging
from pathlib import Path

import oyaml as yaml

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.file_handling import is_writeable_file

# Register None-type representation in YAML as an empty string
yaml.add_representer(type(None), lambda self, _: self.represent_scalar('tag:yaml.org,2002:null', ''))


class ConfigWriterCommand(SimpleCommand):
    """Write configuration data to a YAML file."""

    def __init__(self, source: str = 'config', target: Path | str = 'dump_config.yaml') -> None:
        """Initialize a ConfigWriterCommand instance.

        Args:
            source (str): The attribute of the problem containing the configuration data.
            target (Path): The path or filename to write the configuration to.
        """
        super().__init__()
        self.source: str = source
        self.target: Path = Path(target) if isinstance(target, str) else target

    def precondition_check(self, problem: Problem) -> None:
        """Check preconditions for the command execution.

        Verify that the configuration source exists in the problem and
        that the target file is writable.

        Args:
            problem (Problem): The problem instance to check.

        Raises:
            CommandException: If the source attribute is missing from the problem or
                              if the target file is not writable.
        """
        if self.source not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.source} does not exist in the problem')
        if not is_writeable_file(self.target):
            raise CommandException(f'{self.__class__.__name__} - {self.target} is not writeable')

    def execute(self, problem: Problem) -> None:
        """Write the configuration to the specified file in YAML format.

        Retrieve the configuration from the problem field specified by `source`
        and write it to the target file in YAML format.

        Args:
            problem (Problem): The problem instance containing the configuration data.

        Raises:
            CommandException: If the target is not writable or the configuration
                              is missing from the problem.
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        try:
            with self.target.open('w', encoding='utf-8') as file:
                yaml.dump(problem[self.source].todict(), file, default_style=None)
        except OSError as exc:
            raise OSError(f"Failed to write to {self.target}: {exc}") from exc


    def __repr__(self) -> str:
        """Return a string representation of the ConfigWriterCommand instance.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({self.source!r}, {str(self.target)!r})"
