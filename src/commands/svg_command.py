"""SVGCommand."""
from xml.dom.minidom import Document

from defusedxml.minidom import parseString
from svgwrite import Drawing
from svgwrite.container import Style

from src.board.board import Board
from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.item import Item
from src.utils.config import Config

config = Config()


class SVGCommand(SimpleCommand):
    """Base class for SVG output commands."""

    def __init__(self, board: str = 'board', constraints: str = 'constraints', target: str = 'svg'):
        """Initialize the SVGCommand.

        Args:
            board (str): The attribute for the board
            constraints (str): The attribute for the constraints
            target (str): The attribute of the problem that contains the root constraint to be drawn.
        """
        super().__init__()
        self.board = board
        self.constraints = constraints
        self.target = target
        self.input_types: list[KeyType] = [
            KeyType(board, Board),
            KeyType(constraints, Item),
        ]
        self.output_types: list[KeyType] = [
            KeyType(target, Document),
        ]

    def select(self, constraint: Item | None) -> bool:
        """Select whether the given constraint is to be drawn.

        This method should be overridden in subclasses. The default behavior
        is to draw start Cell, Boxes, Rows, or Columns.

        Args:
            constraint (Item | None): The constraint to be checked.

        Returns:
            bool: True if the constraint is to be drawn, False otherwise.
        """
        return bool(constraint)

    # pylint: disable=WPS210
    def work(self, problem: Problem) -> None:
        """Produce the SVG.

        Args:
            problem (Problem): The problem to produce the SVG for.
        """
        super().work(problem)

        # Build the viewBox string first
        cell_size: int = config.drawing.cell_size
        rows: int = problem.board.board_rows + 2
        columns: int = problem.board.board_columns + 2
        view_box: str = f'0 0 {cell_size * rows} {cell_size * columns}'

        # Directly use problem attributes and create canvas
        canvas: Drawing = Drawing(
            filename=f'{self.name}.svg',
            size=(config.drawing.size, config.drawing.size),
            viewBox=view_box,
        )

        # Add CSS
        canvas.add(Style(content=f'\n{Item.css_text(problem.constraints.css(), 0)}'))

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
        problem[self.target] = parseString(canvas.tostring())
