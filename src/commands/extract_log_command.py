from src.commands.command import Command, CommandException
from src.commands.problem import Problem


class ExtractLogCommand(Command):

    def __init__(self, solver: str = 'solver', target: str = 'log'):
        """Extract the log from the problem."""
        super().__init__()
        self.solver = solver
        self.target = target

    def precondition_check(self, problem: Problem) -> None:
        if self.solver not in problem:
            raise CommandException(f"{self.__class__.__name__} - {self.solver} not in problem")
        if self.target in problem:
            raise CommandException(f"{self.__class__.__name__} - {self.target} already in problem")

    def execute(self, problem: 'Problem') -> None:
        """Extract the log from the problem."""
        problem[self.target] = \
            {
                'application_name': problem[self.solver].application_name,
                'log_contents': problem[self.solver].log
            }

    def __repr__(self) -> str:
        return f"ExtractLogCommand({self.solver!r}, {self.target!r})"
