""" Command to produce an HTML file of the puzzle"""
import logging
from pathlib import Path

import jinja2

from src.commands.simple_command import SimpleCommand


class HTMLCommand(SimpleCommand):
    """ Produce HTML output of the puzzle"""

    def __init__(self, template_file: Path):
        """Create the command

        :param template_file: name of the jinja2 template to use generating the html
        """
        super().__init__()
        self.template_file = template_file
        self.output = None
        with open(self.template_file) as f:
            self.template = jinja2.Template(source=f.read())

    def execute(self) -> None:
        """Create the html"""
        super().execute()
        logging.info("Producing html file of type")
        assert self.parent.problem is not None
        if self.parent.problem.problem.sorted_unique_rules is None:
            logging.error("Sorted unique rules is None")  # pragma: no cover
        else:
            rules = [{'name': rule.name, 'text': rule.text} for rule in self.parent.problem.problem.sorted_unique_rules]
            self.output = self.template.render(
                rules=rules,
                problem_svg=self.parent.svg.output,
                meta=self.parent.board.board.to_dict()['Board']
            )
