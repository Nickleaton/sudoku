"""SVGCommand."""
from abc import abstractmethod

from defusedxml.minidom import parseString
from svgwrite import Drawing
from svgwrite.container import Style

from src.commands.command import CommandException
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.extract_answer_command import ExtractAnswerCommand
from src.commands.null_command import NullCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.commands.solve_command import SolveCommand
from src.items.item import Item
from src.items.solution import Solution
from src.solvers.answer import Answer
from src.utils.config import Config

config = Config()


class SVGCommand(SimpleCommand):
    """Base class for SVG output commands."""

    def work(self, problem: Problem) -> None:
        """Produce the SVG.

        Args:
            problem (Problem): The problem to produce the SVG for.

        Raises:
            CommandException: If the board is not created.
            CommandException: If the constraints are not created.
            CommandException: If the target is not set.
        """
        super().work(problem)
        if problem.board is None:
            raise CommandException(f'Board must be created.')
        if problem.constraints is None:
            raise CommandException(f'Constraints must be created.')
        if self.target is None:
            raise CommandException(f'Target is not set.')

        # Build the viewBox string first
        cell_size: int = config.graphics.cell_size
        rows: int = problem.board.board_rows + 2
        columns: int = problem.board.board_columns + 2
        view_box: str = f'0 0 {cell_size * rows} {cell_size * columns}'

        # Directly use problem attributes and create canvas
        canvas: Drawing = Drawing(
            filename=f'{self.name}.svg',
            size=(config.graphics.size, config.graphics.size),
            viewBox=view_box,
        )

        # Add CSS
        canvas.add(Style(content=f'\n{Item.css_text(problem.constraints.css())}'))

        # Add elements
        for clz in problem.constraints.sorted_glyphs().used_classes:
            if start_element := clz.start_marker():
                canvas.defs.add(start_element)
            if end_element := clz.end_marker():
                canvas.defs.add(end_element)
            if symbol_element := clz.symbol():
                canvas.add(symbol_element)

        # Draw glyphs
        canvas.add(problem.constraints.sorted_glyphs().draw())

        # Convert to XML and store in the problem
        setattr(problem, self.target, parseString(canvas.tostring()))

    @abstractmethod
    def select(self, constraint: Item | None) -> bool:
        """Select whether the given constraint is to be drawn.

        This method should be overridden in subclasses. The default behavior
        is to draw start Cell, Boxes, Rows, or Columns.

        Args:
            constraint (Item | None): The constraint to be checked.

        Returns:
            bool: True if the constraint is to be drawn, False otherwise.
        """


class SVGPencilMarkCommand(SVGCommand):
    """Create an SVG drawing of the problem."""

    def __init__(self):
        """Create the command."""
        super().__init__()
        self.add_preconditions([NullCommand])
        self.target = 'svg_pencil_mark'

    def select(self, constraint: Item | None) -> bool:
        """Selector to determine if the constraint should be displayed.

        This method is start placeholder for future implementation.

        Args:
            constraint (Item | None): The constraint to check if it's included in the output.

        Returns:
            bool: True if the constraint is to be displayed, False otherwise.
        """
        return not isinstance(constraint, Solution)


class SVGProblemCommand(SVGCommand):
    """Create an SVG drawing of the problem."""

    def __init__(self):
        """Create the command."""
        super().__init__()
        self.add_preconditions([CreateConstraintsCommand])
        self.target = 'svg_problem'

    def select(self, constraint: Item | None) -> bool:
        """Selector to determine if the constraint should be displayed.

        Args:
            constraint (Item | None): The constraint to check if it's included in the output.

        Returns:
            bool: True if the constraint is to be displayed, False otherwise.
        """
        return not isinstance(constraint, Solution) and not isinstance(constraint, Answer)


class SVGSolutionCommand(SVGCommand):
    """Create an SVG drawing of the solution."""

    def __init__(self):
        """Create the command."""
        super().__init__()
        self.add_preconditions([SolveCommand])
        self.target = 'svg_solution'

    def select(self, constraint: Item | None) -> bool:
        """Selector to determine if the constraint should be displayed.

        Args:
            constraint (Item | None): The constraint to check if it's included in the output.

        Returns:
            bool: True if the constraint is to be displayed, False otherwise.
        """
        return isinstance(constraint, Solution)


class SVGAnswerCommand(SVGCommand):
    """Command to create an SVG drawing of the line."""

    def __init__(self):
        """Create the command."""
        super().__init__()
        self.add_preconditions([ExtractAnswerCommand])
        self.target = 'answer'

    def select(self, constraint: Item | None) -> bool:
        """Determine if the constraint should be included in the output.

        Args:
            constraint (Item | None): The constraint to check for inclusion.

        Returns:
            bool: True if the constraint is to be displayed; otherwise, False.
        """
        return isinstance(constraint, Answer)
