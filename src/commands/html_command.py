""" Command to produce an HTML file of the puzzle"""
import logging
import os
from pathlib import Path

from jinja2 import Environment, select_autoescape, FileSystemLoader

from src.commands.simple_command import SimpleCommand
from src.commands.svg_command import SVGCommand

# set up environment for jinja templates
env = Environment(
    loader=FileSystemLoader(os.path.join('src', 'html')),
    autoescape=select_autoescape()
)


class HTMLCommand(SimpleCommand):
    """ Produce HTML output of the puzzle"""
    def __init__(self, config_filename: Path | str):
        """Create the command

        :param config_filename: name of the yaml file containing the puzzle
        """
        super().__init__(config_filename)
        self.svg = SVGCommand(config_filename)

    def process(self) -> None:
        """Create the html"""
        super().process()
        self.svg.process()
        logging.info("Producing html file of type")
        assert self.problem is not None
        template = env.get_template("problem.html")
        if self.problem.sorted_unique_rules is None:
            logging.error("Sorted unique rules is None")  # pragma: no cover
        else:
            rules = [{'name': rule.name, 'text': rule.text} for rule in self.problem.sorted_unique_rules]
            self.output = template.render(
                rules=rules,
                problem_svg=self.svg.output,
                meta=self.problem.board.to_dict()['Board']
            )
