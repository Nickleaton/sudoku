"""ExtractLogCommand."""
from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class ExtractLogCommand(SimpleCommand):
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
        self.inputs: list[KeyType] = [
            KeyType(self.solver, str),
        ]
        self.outputs: list[KeyType] = [
            KeyType(self.target, str),
        ]

    def work(self, problem: Problem) -> None:
        """Extract the log from the solver and stores it in the problem.

        Args:
            problem (Problem): The problem instance from which to extract the log.
        """
        problem[self.target] = {
            'application_name': problem[self.solver].application_name,
            'log_contents': problem[self.solver].log,
        }

    def __repr__(self) -> str:
        """Return start_location string representation of the ExtractLogCommand instance.

        Returns:
            str: A string representation of the object.
        """
        return f'ExtractLogCommand({self.solver!r}, {self.target!r})'
