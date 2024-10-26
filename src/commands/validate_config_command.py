"""
Validate Config File.
"""

import logging
from pathlib import Path

from strictyaml import YAMLValidationError, dirty_load

from config_schema import problem_schema
from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.file_handling import is_readable_file


class ValidateConfigCommand(SimpleCommand):
    """Command to validate a configuration file against a schema."""

    def __init__(self, source: Path | str, target: str = 'config_validation'):
        """Initializes the ValidateConfigCommand.

        Args:
            source (Path | str): The path to the configuration file to validate.
            target (str): The target name to store validation results in the problem.
                          Defaults to 'config_validation'.
        """
        super().__init__()
        self.source: Path = Path(source) if isinstance(source, str) else source
        self.target: str = target

    def precondition_check(self, problem: Problem) -> None:
        """Checks preconditions before executing the command.

        Validates that the source file is readable and that the target does not already exist
        in the problem.

        Args:
            problem (Problem): The problem instance to check against.

        Raises:
            CommandException: If the source file is not readable or the target already exists.
        """
        if not is_readable_file(self.source):
            raise CommandException(f'{self.__class__.__name__} - {self.source} does not exist or is not readable ')
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already exists')

    def execute(self, problem: Problem) -> None:
        """Executes the validation of the configuration file.

        Loads the configuration file and validates it against the schema. If the validation
        is successful, it sets the target in the problem to None. Otherwise, it stores the
        error encountered during validation.

        Args:
            problem (Problem): The problem instance to validate against.
        """
        super().execute(problem)
        logging.info(f"Loading {self.source}")
        logging.info(f"Validating {self.target}")
        with open(self.source, 'r', encoding='utf-8') as file:
            yaml_data = file.read()
            try:
                _ = dirty_load(yaml_data, problem_schema)
                problem[self.target] = None
            except YAMLValidationError as e:
                print("YAML data is invalid:", e)
                problem[self.target] = str(e)

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({str(self.source)!r}, {self.target!r})"
