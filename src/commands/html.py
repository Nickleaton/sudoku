import logging
import os

from jinja2 import Environment, select_autoescape, FileSystemLoader

from src.commands.command import Command
from src.commands.svg import SVG

env = Environment(
    loader=FileSystemLoader(os.path.join('src', 'html')),
    autoescape=select_autoescape()
)


class HTML(Command):

    def process(self) -> None:
        logging.info(f"Producing html  file of type")
        super().process()
        assert self.problem is not None
        svg_command = SVG(self.config_filename, "")
        template = env.get_template("problem.html")
        if self.problem.sorted_unique_rules is None:
            logging.error("Sorted unique rules is None")
        else:
            rules = [{'name': rule.name, 'text': rule.text} for rule in self.problem.sorted_unique_rules]
            self.output = template.render(
                rules=rules,
                problem_svg=svg_command.output,
                meta=self.problem.board.to_dict()['Board']
            )
