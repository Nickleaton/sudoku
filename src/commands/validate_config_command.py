"""Validate Config File."""

from strictyaml import dirty_load, YAMLValidationError

from src.commands.create_config_command import CreateConfigCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.schema.config_schema import problem_schema


class ValidateConfigCommand(SimpleCommand):
    """Command to validate start_location configuration file_path against start_location schema."""

    def __init__(self) -> None:
        """Initialize start_location ValidateConfigCommand instance."""
        super().__init__()
        self.add_preconditions([CreateConfigCommand])
        self.target = 'validation'

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
            dirty_load(problem.raw_config, problem_schema)
        except YAMLValidationError as exp:
            problem.validation = str(exp)
            return
        problem.validation = 'OK'
