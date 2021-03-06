import logging
import xml.dom.minidom

from svgwrite import Drawing
from svgwrite.container import Style

from src.commands.simple_command import SimpleCommand
from src.items.item import Item


class Answer(SimpleCommand):

    def process(self) -> None:
        super().process()
        assert self.problem is not None
        assert self.board is not None
        logging.info("Producing answer")
        glyph = self.problem.sorted_glyphs
        canvas = Drawing(
            filename="answer.svg",
            size=("35cm", "35cm"),
            viewBox=f"0 0 {100 * (self.board.board_rows + 2)} {100 * (self.board.board_columns + 2)}"
        )
        canvas.add(Style(content="\n" + Item.css_text(self.problem.css(), 0)))
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
