""" Create an SVG drawing of the problem"""
import logging
import xml.dom.minidom

from svgwrite import Drawing
from svgwrite.container import Style

from src.commands.simple_command import SimpleCommand
from src.items.item import Item
from src.items.solution import Solution
from src.utils.config import Config

config = Config()


class SVGCommand(SimpleCommand):

    def __init__(self):
        super().__init__()
        self.output = None

    @staticmethod
    def select(item: Item) -> bool:
        """ Selector
        :param item: Item to check if it's included in the output
        :return: True if the item is to be displayed
        """
        return not isinstance(item, Solution)

    def execute(self) -> None:
        """ Produce the SVG"""
        super().execute()
        assert self.parent.problem.problem is not None
        assert self.parent.board.board is not None
        logging.info(f"Producing {self.name} svg")

        glyph = self.parent.problem.problem.sorted_glyphs(SVGCommand.select)

        canvas = Drawing(
            filename=f"{self.name}.svg",
            size=(config.drawing.size, config.drawing.size),
            viewBox=f"0 0 {config.drawing.cell_size * (self.parent.board.board.board_rows + 2)} {config.drawing.cell_size * (self.parent.board.board.board_columns + 2)}"
        )
        canvas.add(Style(content="\n" + Item.css_text(self.parent.problem.problem.css(), 0)))
        for clz in glyph.used_classes:
            if (element := clz.start_marker()) is not None:
                canvas.defs.add(element)
            if (element := clz.end_marker()) is not None:
                canvas.defs.add(element)
            if (element := clz.symbol()) is not None:
                canvas.add(element)
        canvas.add(glyph.draw())
        elements = xml.dom.minidom.parseString(canvas.tostring())
        self.output = str(elements.toprettyxml())
