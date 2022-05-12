import os

from jinja2 import Environment, select_autoescape, FileSystemLoader

from src.commands.command import Command
from src.commands.svg import SVG

env = Environment(
    loader=FileSystemLoader(os.path.join('src', 'html')),
    autoescape=select_autoescape()
)


class HTML(Command):

    def __init__(self, filename: str):
        super().__init__(filename)

    @property
    def extension(self) -> str:
        return "html"

    def process(self) -> None:
        super().process()
        svg_command = SVG(self.filename)
        template = env.get_template("problem.html")
        rules = [{'name': rule.name, 'text': rule.text} for rule in self.problem.sorted_unique_rules]
        self.output = template.render(
            rules=rules,
            problem_svg=svg_command.output,
            meta=self.problem.board.to_dict()['Board']
        )
