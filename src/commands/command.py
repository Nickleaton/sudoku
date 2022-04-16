import os

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader(os.path.join('src', 'html')),
    autoescape=select_autoescape()
)

# class Runner:
#
#     def __init__(self, filename: str):
#         self.filename = filename
#         with open(self.filename, 'r', encoding='utf-8') as file:
#             self.config = yaml.load(f, yaml.SafeLoader)
#         self.board = Board.create('Board', self.config)
#         self.problem = Item.create('Constraints', self.board, self.config['Constraints'])
#         self.svg = None
#         self.html = None
#         self.create_drawing()
#         self.create_html()
#
#     def create_drawing(self) -> None:
#         glyph = self.problem.sorted_glyphs
#         canvas = Drawing(filename="test.svg", size=("35cm", "35cm"))
#         for clz in glyph.used_classes:
#             if (element := clz.start_marker()) is not None:
#                 canvas.defs.add(element)
#             if (element := clz.end_marker()) is not None:
#                 canvas.defs.add(element)
#             if (element := clz.symbol()) is not None:
#                 canvas.add(element)
#         canvas.add(glyph.draw())
#         canvas.add_stylesheet(href="glyph.css", title="glyphs")
#         elements = xml.dom.minidom.parseString(canvas.tostring())
#         self.svg = str(elements.toprettyxml())
#
#     def create_html(self) -> None:
#         template = env.get_template("problem.html")
#         rules = [{'name': rule.name, 'text': rule.text} for rule in self.problem.sorted_unique_rules]
#         self.html = template.render(rules=rules, problem_svg=self.svg, meta=self.problem.board.to_dict()['Board'])
