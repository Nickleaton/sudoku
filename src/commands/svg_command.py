"""SVGCommand."""
from abc import abstractmethod

from defusedxml.minidom import parseString
from svgwrite import Drawing
from svgwrite.container import Style

from src.commands.add_constraints_command import AddConstraintsCommand
from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.item import Item
from src.utils.config import Config

config = Config()


class SVGCommand(SimpleCommand):
    """Base class for SVG output commands."""

    def __init__(self):
        """Create the command."""
        super().__init__()
        self.add_preconditions([AddConstraintsCommand])
        self.target = 'svg'

    def work(self, problem: Problem) -> None:  # noqa: WPS231
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
            raise CommandException('Board must be created.')
        if problem.constraints is None:
            raise CommandException('Constraints must be created.')
        if self.target is None:
            raise CommandException('Target is not set.')

        # Build the viewBox string first
        cell_size: int = config.graphics.cell_size
        rows: int = problem.board.size.row + 2
        columns: int = problem.board.size.column + 2
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
            start_element = clz.start_marker()
            if start_element:
                canvas.defs.add(start_element)
            end_element = clz.end_marker()
            if end_element:
                canvas.defs.add(end_element)
            symbol_element = clz.symbol()
            if symbol_element:
                canvas.add(symbol_element)

        # Draw glyphs
        canvas.add(problem.constraints.sorted_glyphs().draw())

        # Convert to XML and store in the problem
        setattr(problem, self.target, parseString(canvas.tostring()))

    @abstractmethod
    def select(self, constraint: Item | None) -> bool:
        """Select whether the given constraint is to be drawn.

        This method should be overridden in subclasses. The default behavior
        is to draw start_location Cell, Boxes, Rows, or Columns.

        Args:
            constraint (Item | None): The constraint to be checked.

        Returns:
            bool: True if the constraint is to be drawn, False otherwise.
        """
