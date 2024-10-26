from src.commands.command import CommandException, Command
from src.commands.problem import Problem
from src.solvers.answer import Answer
from src.solvers.pulp_solver import Status


class ExtractAnswerCommand(Command):
    """
    Command for extracting the answer from the solver's results.
    """

    def __init__(self, solver: str = 'solver', target: str = 'answer'):
        """
        Initializes an ExtractAnswerCommand instance.

        Args:
            solver (str): The attribute in the problem containing the solver.
            target (str): The attribute name in the problem where the answer will be stored.
        """
        super().__init__()
        self.solver = solver
        self.target = target

    def precondition_check(self, problem: Problem) -> None:
        """
        Checks preconditions before executing the command.

        Ensures that a solver has been set in the problem and that the target
        attribute does not already exist.

        Args:
            problem (Problem): The problem instance to check.

        Raises:
            CommandException: If no solver is set or if the target attribute
                              already exists in the problem.
        """
        if problem[self.solver] is None:
            raise CommandException("No solver has been set.")
        if self.target in problem:
            raise CommandException(f"{self.__class__.__name__} - {self.target} already in problem")

    def execute(self, problem: Problem) -> None:
        """
        Extracts the answer from the solver's results and stores it in the problem.

        If the solver's status is not optimal, the command will not store an answer.

        Args:
            problem (Problem): The problem instance from which to extract the answer.

        Raises:
            CommandException: If no solver is set.
        """
        if problem[self.solver] is None:
            raise CommandException("No solver has been set.")

        if problem[self.solver].status != Status.OPTIMAL:
            return

        problem[self.target] = Answer(problem[self.solver].board)
        for row in problem[self.solver].board.row_range:
            for column in problem[self.solver].board.column_range:
                problem[self.target].set_value(row, column, int(problem[self.solver].values[row][column].varValue))

    def __repr__(self) -> str:
        """
        Returns a string representation of the ExtractAnswerCommand instance.

        Returns:
            str: A string representation of the object.
        """
        return f"ExtractAnswerCommand({self.solver!r}, {self.target!r})"
