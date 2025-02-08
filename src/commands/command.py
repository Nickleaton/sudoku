"""Command."""
import logging
from typing import ClassVar

from src.commands.problem import Problem
from src.utils.sudoku_exception import SudokuError


class CommandError(SudokuError):
    """Represents an error occurring within a command.

    Attributes:
        attribute (str): The attribute of the problem that caused the error.
    """

    def __init__(self, attribute: str) -> None:
        """Initialize a CommandError.

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
    classes: ClassVar[dict[str, type['Command']]] = {}

    def __init_subclass__(cls, **kwargs):
        """Register the subclass to the `Item` class hierarchy.

        Args:
            kwargs: Any additional keyword arguments passed to the method (not used).
        """
        super().__init_subclass__(**kwargs)
        Command.classes[cls.__name__] = cls
        Command.classes['Command'] = Command

    def __init__(self) -> None:
        """Initialize a Command instance."""
        self.preconditions: list[type[Command]] = []  # Forward reference without quotes
        self.target: str | None = None

    def add_preconditions(self, preconditions: list[type['Command']]) -> None:
        """Add a list of precondition classes to this command.

        Args:
            preconditions (list[type[Command]]): The precondition classes to add.
        """
        self.preconditions.extend(preconditions)

    def check_preconditions(self, problem: Problem) -> None:
        """Check if the command's preconditions are met.

        Args:
            problem (Problem): The problem instance to check the preconditions on.

        Raises:
            CommandError: If any precondition is not met.
        """
        for precondition_class in self.preconditions:
            precondition: Command = precondition_class()
            if precondition.target is None:
                continue
            if precondition.target not in problem.__dict__:
                raise CommandError(f'{precondition.target} not found in problem for {self.name}')

    def work(self, problem: Problem) -> None:
        """Perform the work of the command.

        This method should be overridden by subclasses to implement specific logic.

        Args:
            problem (Problem): The problem instance to operate on.
        """
        logging.info(f'Running {self.name} {problem.problem_file_name}')

    def execute(self, problem: Problem) -> None:
        """Execute the command, performing validation and the main action.

        This method validates the line, inputs, and outputs, performs the core work of the command,
        and performs post-execution validation.

        Args:
            problem (Problem): The problem instance to execute the command on.

        Raises:
            CommandError: If any validation step or the execution itself fails.
        """
        for precondition in self.preconditions:
            precondition().execute(problem)
        try:
            self.check_preconditions(problem)
        except CommandError as preconditions_exp:
            logging.error(f'Error in {self.__class__.__name__} - {preconditions_exp}', exc_info=True)
            raise
        try:
            self.work(problem)
        except Exception as work_exp:
            logging.error(
                f'Error execution of work in {self.__class__.__name__}: '
                f'{type(work_exp).__name__} - {work_exp}',
                exc_info=True,
            )
            raise CommandError(f'Error in {self.__class__.__name__}.work') from work_exp

    @property
    def name(self) -> str:
        """Retrieve a readable name for the command class.

        Returns:
            str: The class name with 'Command' removed, if present.
        """
        if self.__class__.__name__ == 'Command':
            return 'Command'
        return self.__class__.__name__.replace('Command', '')

    def __repr__(self) -> str:
        """Return a string representation of the command.

        Returns:
            str: String representation of the object.
        """
        return f'{self.__class__.__name__}()'
