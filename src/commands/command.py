"""Command."""
import logging
from pathlib import Path
from typing import Any

from src.commands.key_type import KeyType
from src.commands.parameter_value_type import ParameterValueType
from src.commands.problem import Problem
from src.utils.sudoku_exception import SudokuException


class CommandException(SudokuException):
    """Represents an error occurring within a command.

    Attributes:
        attribute (str): The attribute of the problem that caused the error.
    """

    def __init__(self, attribute: str) -> None:
        """Initialize a CommandException.

        Args:
            attribute (str): The attribute of the problem that caused the error.
        """
        super().__init__(f'Error in {attribute}')
        self.attribute = attribute


class Command:
    """Base class for all commands implementing the Command pattern.

    Commands define specific behaviors through their `work` method and manage
    inputs, outputs, and line dynamically.
    """

    # Class Variables
    classes: dict[str, Type['Command']] = {}

    def __init_subclass__(cls, **kwargs):
        """Register the subclass to the `Item` class hierarchy.

        Args:
            kwargs: Any additional keyword arguments passed to the method (not used).
        """
        super().__init_subclass__(**kwargs)
        Command.classes[cls.__name__] = cls
        Command.classes['Command'] = Item

    def __init__(self) -> None:
        """Initialize a Command instance."""
        self.parameters_list: list[ParameterValueType] = []
        self.input_types: list[KeyType] = []
        self.output_types: list[KeyType] = []

    def apply_parameters(self, problem: Problem) -> None:
        """Set line in the problem instance.

        Args:
            problem (Problem): The problem where line are being set.
        """
        for parameter_item in self.parameters_list:
            problem[parameter_item.key] = parameter_item.parameter_value

    @staticmethod
    def validate_single_parameter(problem: Problem, parameter_item: ParameterValueType, check_exists: bool) -> None:
        """Validate a single parameter based on its existence and type in the problem.

        Args:
            problem (Problem): The problem instance to validate.
            parameter_item (ParameterValueType): The parameter to validate.
            check_exists (bool): If True, ensures the parameter exists; if False, ensures it does not.

        Raises:
            CommandException: If the parameter is missing or already exists in the problem,
                              or if its type does not match the expected type.
        """
        exists: bool = parameter_item.key in problem
        if check_exists and not exists:
            raise CommandException(f"'{parameter_item.key}' is missing from the problem.")
        if not check_exists and exists:
            raise CommandException(f"'{parameter_item.key}' already exists in the problem.")
        if check_exists and not isinstance(problem[parameter_item.key], parameter_item.type):
            raise CommandException(
                f'"{parameter_item.key}" is of the wrong type. '
                f'Expected {parameter_item.type}, got {type(problem[parameter_item.key])}.',
            )

    @staticmethod
    def validate_parameters(problem: Problem, parameters_list: list[ParameterValueType], check_exists: bool) -> None:
        """Validate a list of line based on their existence and type in the problem.

        Args:
            problem (Problem): The problem instance to validate.
            parameters_list (list[ParameterValueType]): The list of line to validate.
            check_exists (bool): If True, ensures the line exist; if False, ensures they do not.
        """
        for parameter_item in parameters_list:
            Command.validate_single_parameter(problem, parameter_item, check_exists)

    @staticmethod
    def validate_single_value(problem: Problem, value_item: KeyType, check_exists: bool) -> None:
        """Validate a single input_value based on its existence and type in the problem.

        Args:
            problem (Problem): The problem instance to validate.
            value_item (KeyType): The input_value to validate.
            check_exists (bool): If True, ensures the input_value exists; if False, ensures it does not.

        Raises:
            CommandException: If the input_value is missing or already exists in the problem,
                              or if its type does not match the expected type.
        """
        exists: bool = value_item.key in problem
        if check_exists and not exists:
            raise CommandException(f"'{value_item.key}' is missing from the problem.")
        if not check_exists and exists:
            raise CommandException(f"'{value_item.key}' already exists in the problem.")
        if check_exists and not isinstance(problem[value_item.key], value_item.type):
            raise CommandException(
                f'"{value_item.key!r}" is of the wrong type. '
                f'Expected {value_item.type!r}, got {type(problem[value_item.key])}.',
            )

    @staticmethod
    def validate_values(problem: Problem, value_list: list[KeyType], check_exists: bool) -> None:
        """Validate a list of value_variables based on their existence and type in the problem.

        Args:
            problem (Problem): The problem instance to validate.
            value_list (list[KeyType]): The list of value_variables to validate.
            check_exists (bool): If True, ensures the value_variables exist; if False, ensures they do not.
        """
        for value_item in value_list:
            Command.validate_single_value(problem, value_item, check_exists)

    def work(self, problem: Problem) -> None:
        """Perform the work of the command.

        This method should be overridden by subclasses to implement specific logic.

        Args:
            problem (Problem): The problem instance to operate on.
        """

    def validate_and_setup(self, problem: Problem) -> None:
        """Perform validation and setup before command execution.

        Args:
            problem (Problem): The problem instance where line and inputs are validated and applied.
        """
        self.validate_parameters(problem, self.parameters_list, check_exists=False)
        self.apply_parameters(problem)
        self.validate_parameters(problem, self.parameters_list, check_exists=True)
        self.validate_values(problem, self.input_types, check_exists=True)
        self.validate_values(problem, self.output_types, check_exists=False)

    def post_validate(self, problem: Problem) -> None:
        """Perform validation of outputs after command execution.

        Args:
            problem (Problem): The problem instance where output validation is performed.
        """
        self.validate_values(problem, self.output_types, check_exists=True)

    def execute(self, problem: Problem) -> None:
        """Execute the command, performing validation and the main action.

        This method validates the line, inputs, and outputs, performs the core work of the command,
        and performs post-execution validation.

        Args:
            problem (Problem): The problem instance to execute the command on.

        Raises:
            Exception: If any validation step or the execution itself fails.
        """
        logging.info(f'{self.__class__.__name__} executing command.')

        # try:
        #     self.validate_and_setup(problem)
        # except Exception as validation_exp:
        #     logging.error(
        #         f'Error validation and setup in {self.__class__.__name__}: '
        #         f'{type(validation_exp).__name__} - {validation_exp}',
        #         exc_info=True,
        #     )
        #     raise

        try:
            self.work(problem)
        except Exception as work_exp:
            logging.error(
                f'Error execution of work in {self.__class__.__name__}: '
                f'{type(work_exp).__name__} - {work_exp}',
                exc_info=True,
            )
            raise

        try:
            self.post_validate(problem)
        except Exception as post_validation_exp:
            logging.error(
                f'Error post-validation in {self.__class__.__name__}: '
                f'{type(post_validation_exp).__name__} - {post_validation_exp}',
                exc_info=True,
            )
            raise

    @property
    def name(self) -> str:
        """Retrieve a readable name for the command class.

        Returns:
            str: The class name with 'Command' removed, if present.
        """
        if self.__class__.__name__ == 'Command':
            return 'Command'
        return self.__class__.__name__.replace('Command', '')

    @staticmethod
    def get_string_representation(input_value: Any) -> str:
        """Convert a input_value to its string representation.

        Args:
            input_value (Any): The input_value to be converted. Can be a string, a `Path` object, or another type.

        Returns:
            str: The string representation of the input_value.
        """
        if isinstance(input_value, str):
            return repr(input_value)
        if isinstance(input_value, Path):
            return repr(str(input_value))
        return repr(str(input_value))

    def __repr__(self) -> str:
        """Return a string representation of the command.

        Returns:
            str: String representation of the object.
        """
        # names: list[str] = []
        # for parameter_item in self.parameters_list:
        #     names.append(self.get_string_representation(parameter_item.key))
        #     names.append(self.get_string_representation(parameter_item.parameter_value))
        # names.extend([self.get_string_representation(key_type.key) for key_type in self.input_types])
        # names.extend([self.get_string_representation(key_type.key) for key_type in self.output_types])

        # return f"{self.__class__.__name__}({', '.join(names)})"
        return f"{self.__class__.__name__}()"
