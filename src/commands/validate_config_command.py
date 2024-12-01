"""Validate Config File."""

from strictyaml import YAMLValidationError, dirty_load

from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.parsers.config_schema import problem_schema


class ValidateConfigCommand(SimpleCommand):
    """Command to validate a configuration file against a schema."""

    def __init__(self, source: str = 'config_text', target: str = 'config_validation'):
        """Initialize the ValidateConfigCommand.

        Args:
            source (str): The name of the string in the problem to validate. Defaults to 'config'.
            target (str): The target name to store validation results in the problem.
                          Defaults to 'config_validation'.
        """
        super().__init__()
        self.source: str = source
        self.target: str = target
        self.input_types: list[KeyType] = [
            KeyType(source, str)
        ]
        self.output_types: list[KeyType] = [
            KeyType(self.target, str)
        ]

    def work(self, problem: Problem) -> None:
        """Execute the validation of the configuration file.

        Loads the configuration file and validates it against the schema. If the validation
        is successful, it sets the target in the problem to None. Otherwise, it stores the
        error encountered during validation.

        Args:
            problem (Problem): The problem instance to validate against.
        """
        super().work(problem)
        try:
            _ = dirty_load(problem[self.source], problem_schema)
            problem[self.target] = "Passed validation"
        except YAMLValidationError as e:
            problem[self.target] = str(e)
