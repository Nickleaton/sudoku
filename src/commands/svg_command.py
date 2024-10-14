"""
Create an SVG drawing of the problem.
"""
import logging
import xml.dom.minidom

from svgwrite import Drawing
from svgwrite.container import Style

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.glyphs.glyph import Glyph
from src.items.item import Item
from src.utils.config import Config

config = Config()


class SVGCommand(SimpleCommand):
    """
    Base class for SVG output commands.
    """

    def __init__(self, problem_field: str):
        """
        Initialize the SVGCommand.

        Parameters:
            problem_field (str): The attribute of the problem that contains the root item to be drawn
        """
        super().__init__()
        self.problem_field = problem_field

    def select(self, item: Item | None) -> bool:
        """
        Selects whether the given item is to be drawn.

        To be over writen in subclasses
        Default behavior is to draw a Cell, Boxes, Rows, or Columns

        Parameters:
            item (Item): The item to be checked.

        Returns:
            bool: True if the item is to be drawn, False otherwise.
        """
        if item is None:
            return True
        return False

    def precondition_check(self, problem: Problem) -> None:
        if problem.board is None:
            raise CommandException(f'{self.__class__.__name__} - Board not built')
        if problem.constraints is None:
            raise CommandException(f'{self.__class__.__name__} - Constraints not built')

    def execute(self, problem: Problem) -> None:
        """ Produce the SVG. """
        super().execute(problem)
        logging.info(f'Creating {self.problem_field}')

        # Get the glyphs to draw
        # There's an ordering so the items are drawn in the right order
        # This is what sorted glyphs does
        # self.select is passed in and that will select which glyphs are to be drawn
        glyphs: Glyph = problem.constraints.sorted_glyphs(self.select)

        # Create the canvas for the SVG
        # There is a one cell border around the drawing
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
        # add all the elements
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
        elements = xml.dom.minidom.parseString(canvas.tostring())
        problem[self.problem_field] = elements
        # problem[self.problem_field] = str(elements.toprettyxml())

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        The string is of the form "SVGCommand(problem_field)". The
        representation is useful for debugging and logging.

        :return: A string representation of the object.
        :rtype: str
        """
        return f"{self.__class__.__name__}({self.problem_field!r})"
