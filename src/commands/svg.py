import xml.dom.minidom

from svgwrite import Drawing

from src.commands.command import Command


class SVG(Command):

    def __init__(self, filename: str):
        super().__init__(filename)

    @property
    def extension(self) -> str:
        return "svg"

    def process(self) -> None:
        super().process()
        glyph = self.problem.sorted_glyphs
        canvas = Drawing(filename="test.svg", size=("35cm", "35cm"))
        for clz in glyph.used_classes:
            if (element := clz.start_marker()) is not None:
                canvas.defs.add(element)
            if (element := clz.end_marker()) is not None:
                canvas.defs.add(element)
            if (element := clz.symbol()) is not None:
                canvas.add(element)
        canvas.add(glyph.draw())
        canvas.add_stylesheet(href="glyph.css", title="glyphs")
        elements = xml.dom.minidom.parseString(canvas.tostring())
        self.output = str(elements.toprettyxml())
