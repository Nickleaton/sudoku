"""ExtractLogCommand."""
from src.commands.command import Command, CommandException
from src.commands.problem import Problem


class ExtractLogCommand(Command):
    """Command for extracting the log from the solver's results."""

    def __init__(self, solver: str = 'solver', target: str = 'log'):
        """Initialize an ExtractLogCommand instance.

        Args:
            solver (str): The attribute in the problem containing the solver.
            target (str): The attribute name in the problem where the log will be stored.
        """
        super().__init__()
        self.solver = solver
        self.target = target

    def precondition_check(self, problem: Problem) -> None:
        """Check preconditions before executing the command.

        Ensures that the specified solver exists in the problem and that
        the target attribute does not already exist.

        Args:
            problem (Problem): The problem instance to check.

        Raises:
            CommandException: If the solver is not found or if the target
                              attribute already exists in the problem.
        """
        if self.solver not in problem:
            raise CommandException(f"{self.__class__.__name__} - {self.solver} not in problem")
        if self.target in problem:
            raise CommandException(f"{self.__class__.__name__} - {self.target} already in problem")

    def execute(self, problem: Problem) -> None:
        """Extract the log from the solver and stores it in the problem.

        Args:
            problem (Problem): The problem instance from which to extract the log.

        Returns:
            None
        """
        problem[self.target] = {
            'application_name': problem[self.solver].application_name,
            'log_contents': problem[self.solver].log
        }

    def __repr__(self) -> str:
        """Return a string representation of the ExtractLogCommand instance.

        Returns:
            str: A string representation of the object.
        """
        return f"ExtractLogCommand({self.solver!r}, {self.target!r})"
