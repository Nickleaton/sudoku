import logging
from pathlib import Path

import oyaml as yaml

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.file_handling import is_writeable_file


def represent_none(self, _):
    """
    Custom YAML representer to convert None to an empty string.

    This ensures that None values in YAML are represented as empty strings
    rather than the default '~'.

    Args:
        self: The representer instance.
        _: The value to represent (unused).
    """
    return self.represent_scalar('tag:yaml.org,2002:null', '')


# Register the representer with the YAML dumper
yaml.add_representer(type(None), represent_none)


class ConfigWriterCommand(SimpleCommand):
    """
    Command for writing configuration data to a YAML file.
    """

    def __init__(self, source: str = 'config', target: Path | str = 'dump_config.yaml') -> None:
        """
        Initializes a ConfigWriterCommand instance.

        Args:
            source (str): The attribute of the problem containing the configuration data.
            target (Path | str): The path or filename to write the configuration to.
        """
        super().__init__()
        self.source: str = source
        self.target: Path = Path(target) if isinstance(target, str) else target

    def precondition_check(self, problem: Problem) -> None:
        """
        Checks preconditions for the command execution.

        Verifies that the configuration source exists in the problem and
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
        """
        Writes the configuration to the specified file in YAML format.

        The configuration is obtained from the problem field specified by `source`
        and written to the target file in YAML format.

        Args:
            problem (Problem): The problem instance containing the configuration data.

        Raises:
            CommandException: If the target is not writable or the configuration
                              is missing from the problem.
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        with open(self.target, 'w', encoding='utf-8') as file:
            yaml.dump(problem[self.source].todict(), file, default_style=None)

    def __repr__(self) -> str:
        """
        Returns a string representation of the ConfigWriterCommand instance.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({self.source!r}, {str(self.target)!r})"
