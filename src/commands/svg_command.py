"""Create an SVG drawing of the problem."""
import logging
from xml.dom.minidom import Document

from defusedxml.minidom import parseString
from svgwrite import Drawing
from svgwrite.container import Style

from src.board.board import Board
from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.glyphs.glyph import Glyph
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
            target (str): The attribute of the problem that contains the root item to be drawn.
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
            KeyType(target, Document)
        ]

    def select(self, item: Item | None) -> bool:
        """Select whether the given item is to be drawn.

        This method should be overridden in subclasses. The default behavior
        is to draw a Cell, Boxes, Rows, or Columns.

        Args:
            item (Item | None): The item to be checked.

        Returns:
            bool: True if the item is to be drawn, False otherwise.
        """
        if item is None:
            return True
        return False

    def work(self, problem: Problem) -> None:
        """Produce the SVG.

        Args:
            problem (Problem): The problem to produce the SVG for.
        """
        super().work(problem)
        logging.info(f'Creating {self.target}')

        # Get the glyphs to draw
        glyphs: Glyph = problem.constraints.sorted_glyphs()

        # Create the canvas for the SVG
        cell_size: int = config.drawing.cell_size
        rows: int = problem.board.board_rows + 2
        columns: int = problem.board.board_columns + 2
        canvas = Drawing(
            filename=f"{self.name}.svg",
            size=(config.drawing.size, config.drawing.size),
            viewBox=f"0 0 {cell_size * rows} {cell_size * columns}"
        )
        # Add in the CSS
        canvas.add(Style(content="\n" + Item.css_text(problem.constraints.css(), 0)))

        # Add all the elements
        for clz in glyphs.used_classes:
            if (element := clz.start_marker()) is not None:
                canvas.defs.add(element)
            if (element := clz.end_marker()) is not None:
                canvas.defs.add(element)
            if (element := clz.symbol()) is not None:
                canvas.add(element)

        # Draw the glyphs
        canvas.add(glyphs.draw())

        # Convert to xml
        elements = parseString(canvas.tostring())
        problem[self.target] = elements
