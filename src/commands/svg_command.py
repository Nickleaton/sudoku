"""SVGCommand."""
from abc import abstractmethod

from defusedxml.minidom import parseString
from svgwrite import Drawing
from svgwrite.container import Style

from src.commands.add_constraints_command import AddConstraintsCommand
from src.commands.command import CommandError
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

    def work(self, problem: Problem) -> None:
        """Produce the SVG.

        Args:
            problem (Problem): The problem to produce the SVG for.
        """
        super().work(problem)
        self.validate_problem(problem)
        canvas = self.create_canvas(problem)
        self.add_css(canvas, problem)
        self.add_elements(canvas, problem)
        self.draw_glyphs(canvas, problem)
        self.store_result(problem, canvas)

    def validate_problem(self, problem: Problem) -> None:
        """Validate that the problem has the necessary components.

        Args:
            problem (Problem): The problem instance to validate.

        Raises:
            CommandError: If the board, constraints, or target is not set.
        """
        if problem.board is None:
            raise CommandError('Board must be created.')
        if problem.constraints is None:
            raise CommandError('Constraints must be created.')
        if self.target is None:
            raise CommandError('Target is not set.')

    def create_canvas(self, problem: Problem) -> Drawing:
        """Create the SVG canvas with the appropriate viewBox.

        Args:
            problem (Problem): The problem instance containing board size information.

        Returns:
            Drawing: The initialized SVG drawing canvas.
        """
        cell_size: int = config.graphics.cell_size
        rows: int = problem.board.size.row + 2
        columns: int = problem.board.size.column + 2
        view_box: str = f'0 0 {cell_size * rows} {cell_size * columns}'

        return Drawing(
            filename=f'{self.name}.svg',
            size=(config.graphics.size, config.graphics.size),
            viewBox=view_box,
        )

    @staticmethod
    def add_css(canvas: Drawing, problem: Problem) -> None:
        """Add CSS styles to the canvas.

        Args:
            canvas (Drawing): The SVG drawing canvas.
            problem (Problem): The problem instance containing constraint styles.
        """
        canvas.add(Style(content=f'\n{Item.css_text(problem.constraints.css())}'))

    @staticmethod
    def add_elements(canvas: Drawing, problem: Problem) -> None:
        """Add markers and symbols to the canvas.

        Args:
            canvas (Drawing): The SVG drawing canvas.
            problem (Problem): The problem instance containing constraints.
        """
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

    @staticmethod
    def draw_glyphs(canvas: Drawing, problem: Problem) -> None:
        """Draw glyphs on the canvas.

        Args:
            canvas (Drawing): The SVG drawing canvas.
            problem (Problem): The problem instance containing constraints.
        """
        canvas.add(problem.constraints.sorted_glyphs().draw())

    def store_result(self, problem: Problem, canvas: Drawing) -> None:
        """Store the generated SVG in the problem object.

        Args:
            problem (Problem): The problem instance where the SVG will be stored.
            canvas (Drawing): The SVG drawing canvas.
        """
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
