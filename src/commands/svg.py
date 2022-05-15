import logging
import xml.dom.minidom

from svgwrite import Drawing
from svgwrite.container import Style

from src.commands.command import Command
from src.items.item import Item


class SVG(Command):

    def process(self) -> None:
        assert self.problem is not None
        super().process()
        logging.info(f"Producing svg")
        glyph = self.problem.sorted_glyphs
        canvas = Drawing(filename="test.svg", size=("35cm", "35cm"), viewBox="0 0 1100 1100")
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
