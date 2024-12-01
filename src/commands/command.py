"""Command base class.

Commands are used to perform specific actions following the Command pattern
from the Gang of Four book.
For more information, see https://en.wikipedia.org/wiki/Command_pattern
"""
import logging
from pathlib import Path
from typing import Any

from src.commands.key_type import KeyType
from src.commands.parameter_value_type import ParameterValueType
from src.commands.problem import Problem
from src.utils.sudoku_exception import SudokuException


class CommandException(SudokuException):
    """Raise when an error occurs in a command.

    Attributes:
        attribute (str): The attribute of the problem that caused the error.
    """

    def __init__(self, attribute: str):
        """Initialize a CommandException.

        Args:
            attribute (str): The attribute of the problem that caused the error.
        """
        super().__init__(f"Error in {attribute}")
        self.attribute = attribute


class Command:
    """Define a base class for all commands implementing the Command pattern.

    Commands inheriting from this base class should define specific behavior
    in their `work` method and parameter setup.
    """

    def __init__(self):
        """Initialize a Command instance."""
        self.parameters: list[ParameterValueType] = []
        self.input_types: list[KeyType] = []
        self.output_types: list[KeyType] = []

    def set_parameters(self, problem: Problem) -> None:
        """Set the required parameter_types in the problem.

        Args:
            problem (Problem): The problem where parameter_types are being set.
        """
        for param in self.parameters:
            problem[param.key] = param.value

    @staticmethod
    def validate_parameters(problem: Problem, parameters: list[ParameterValueType], check_exists: bool) -> None:
        """Validate parameters based on their existence in the problem.

        Args:
            problem (Problem): A dictionary-like object representing the problem.
            parameters (list[ParameterValueType]): A list of ParameterValueType objects to validate.
            check_exists (bool): If True, checks that parameters exist. If False, checks they do not.

        Raises:
            CommandException: If a parameter fails the validation based on existence.
        """
        for param in parameters:
            exists = param.key in problem
            if check_exists and not exists:
                raise CommandException(f"'{param.key}' is missing from the problem.")
            if not check_exists and exists:
                raise CommandException(f"'{param.key}' already exists in the problem.")
            if check_exists and not isinstance(problem[param.key], param.type):
                raise CommandException(
                    f"'{param.key}' is of the wrong type. Expected {param.type}, got {type(problem[param.key])}."
                )

    @staticmethod
    def validate_values(problem: Problem, values: list[KeyType], check_exists: bool) -> None:
        """Validate values based on their existence in the problem.

        Args:
            problem (Problem): A dictionary-like object representing the problem.
            values (list[KeyType]): A list of KeyType objects to validate.
            check_exists (bool): If True, checks that values exist. If False, checks they do not.

        Raises:
            CommandException: If a value fails the validation based on existence.
        """
        for value in values:
            exists = value.key in problem
            if check_exists and not exists:
                raise CommandException(f"'{value.key}' is missing from the problem.")
            if not check_exists and exists:
                raise CommandException(f"'{value.key}' already exists in the problem.")
            if check_exists and not isinstance(problem[value.key], value.type):
                print(f"value.key: {value.key}, value.type: {value.type}, problem: {problem}")
                raise CommandException(
                    f"{value.key!r} is of the wrong type. Expected {value.type!r}, got {type(problem[value.key])}."
                )

    def work(self, problem: Problem) -> None:
        """Perform the work of the command.

        This method should be overridden in child classes to implement specific logic.

        Args:
            problem (Problem): The problem instance to operate on.

        Raises:
            NotImplementedError: If the method is not overridden in a child class.
        """
        pass

    def execute(self, problem: Problem) -> None:
        """Execute the command, performing the specified action.

        This method validates inputs, outputs, and parameter_types, then performs the work of the command.
        If an error occurs during validation or execution, it is logged and re-raised.

        Args:
            problem (Problem): The problem instance to execute the command on.

        Raises:
            ValueError: If any validation step fails or an issue occurs during execution.
        """
        logging.info(f"{self.__class__.__name__} executing command.")

        try:
            # Validate parameter_types and input/output states
            self.validate_parameters(problem, self.parameters, False)
            self.set_parameters(problem)
            self.validate_parameters(problem, self.parameters, True)

            self.validate_values(problem, self.input_types, True)
            self.validate_values(problem, self.output_types, False)

            # Execute the core work
            self.work(problem)

            # Post-execution validation
            self.validate_values(problem, self.output_types, True)

        except Exception as e:
            # Log the exception with its type and message
            logging.error(
                f"Error occurred in {self.__class__.__name__}: {type(e).__name__} - {e}",
                exc_info=True,  # Logs the traceback as well
            )
            # Re-raise the exception to allow the caller to handle it further
            raise

    @property
    def name(self) -> str:
        """Return a readable name for the command class.

        Returns:
            str: The name of the class, with "Command" removed if present.
        """
        return self.__class__.__name__.replace("Command", "") if self.__class__.__name__ != 'Command' else 'Command'

    @staticmethod
    def get_string_representation(value: Any) -> str:
        if isinstance(value, str):
            return repr(value)
        if isinstance(value, Path):
            return repr(str(value))
        return repr(str(value))

    def __repr__(self) -> str:
        """Return a string representation of the command

        Returns:
            str: String representation of the object.
        """
        names: list[str] = []
        for param in self.parameters:
            names.append(self.get_string_representation(param.key))
            names.append(self.get_string_representation(param.value))
        names.extend([self.get_string_representation(key_type.key) for key_type in self.input_types])
        names.extend([self.get_string_representation(key_type.key) for key_type in self.output_types])

        result: str = self.__class__.__name__
        result += "("
        result += ", ".join(names)
        result += ")"
        return result
