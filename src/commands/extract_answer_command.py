from src.commands.command import CommandException, Command
from src.commands.problem import Problem
from src.solvers.answer import Answer
from src.solvers.pulp_solver import Status


class ExtractAnswerCommand(Command):
    """
    Extract the answer from the solver's results.
    """

    def __init__(self, solver: str = 'solver', target: str = 'answer'):
        super().__init__()
        self.solver = solver
        self.target = target

    def precondition_check(self, problem: Problem):
        if problem.solver is None:
            raise CommandException("No solver has been set.")
        if self.target in problem:
            raise CommandException(f"{self.__class__.__name__} - {self.target} already in problem")

    def execute(self, problem: Problem):
        if problem.solver is None:
            raise CommandException("No solver has been set.")

        if problem[self.solver].status != Status.OPTIMAL:
            return
        problem[self.target] = Answer(problem[self.solver].board)
        for row in problem[self.solver].board.row_range:
            for column in problem[self.solver].board.column_range:
                problem[self.target].set_value(row, column, int(problem[self.solver].values[row][column].varValue))

    def __repr__(self) -> str:
        return f"ExtractAnswerCommand({self.solver!r}, {self.target!r})"
