"""Validate Config File."""

from strictyaml import YAMLValidationError, dirty_load

from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.schema.config_schema import problem_schema


class ValidateConfigCommand(SimpleCommand):
    """Command to validate start configuration file_path against start schema."""

    def __init__(self, source: str = 'config_text', target: str = 'config_validation'):
        """Initialize the ValidateConfigCommand.

        Args:
            source (str): The name of the string in the problem to validate. Defaults to 'config'.
            target (str): The target name to store validation results in the problem.
        """
        super().__init__()
        self.source: str = source
        self.target: str = target
        self.input_types: list[KeyType] = [
            KeyType(source, str),
        ]
        self.output_types: list[KeyType] = [
            KeyType(self.target, str),
        ]

    def work(self, problem: Problem) -> None:
        """Execute the validation of the configuration file_path.

        Loads the configuration file_path and validates it against the schema. If the validation
        is successful, it sets the target in the problem to None. Otherwise, it stores the
        error encountered during validation.

        Args:
            problem (Problem): The problem instance to validate against.
        """
        super().work(problem)
        try:
            dirty_load(problem[self.source], problem_schema)
        except YAMLValidationError as exp:
            problem[self.target] = str(exp)
            return
        problem[self.target] = 'Passed validation'
