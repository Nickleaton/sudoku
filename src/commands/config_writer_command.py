import logging
from pathlib import Path

import oyaml as yaml

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.file_handling import is_writeable_file


def represent_none(self, _):
    """
    A YAML representer that converts None to an empty string.

    This is needed because the default YAML representer for None is
    `~` which is not what we want.
    """
    return self.represent_scalar('tag:yaml.org,2002:null', '')


# Register the representer with the YAML dumper
yaml.add_representer(type(None), represent_none)


class ConfigWriterCommand(SimpleCommand):
    def __init__(self,
                 source: str = 'config',
                 target: Path | str = 'dump_config.yaml') -> None:

        """
        Construct a ConfigWriterCommand

        :param source: The attribute of the problem to store the configuration in
        :param target: The name of the file to write the configuration to
        """
        super().__init__()
        self.source: str = source
        self.target: Path = Path(target) if isinstance(target, str) else target

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        This method checks that the source attribute specified by
        `source` exists in the problem and that the target file
        specified by `target` is writeable.

        :param problem: The problem to check
        :raises CommandException: If the preconditions are not met
        """
        if self.source not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.source} does not exist in the problem')
        if not is_writeable_file(self.target):
            raise CommandException(f'{self.__class__.__name__} - {self.target} is not writeable')

    def execute(self, problem: Problem) -> None:
        """
        Write the configuration to the specified file.

        The configuration is written in YAML format to the file specified
        by `target`. The configuration is obtained from the problem field
        specified by `source`.

        Parameters:
            problem (Problem): The problem to obtain the configuration from.

        Raises:
            CommandException: If the target is not writeable or if the
                configuration is not present in the problem.

        Returns:
            None
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        with open(self.target, 'w', encoding='utf-8') as file:
            yaml.dump(problem[self.source].todict(), file, default_style=None)

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({self.source!r}, {str(self.target)!r})"
