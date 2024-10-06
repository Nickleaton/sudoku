""" Command to produce an HTML file of the puzzle"""
import logging
from pathlib import Path
from typing import Optional

import jinja2
from jinja2 import Template

from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class TemplateCommand(SimpleCommand):
    """ Render the problem using a Jinja2 template """

    def __init__(self, template_file_name: Path, field_name: str):
        """Create the command

        :param template_file: name of the jinja2 template to use generating the html
        :param field_name: name of the field in the problem that will contain the html
        """
        super().__init__()
        self.template_file_name: Path = template_file_name
        self.field_name: str = field_name
        with open(self.template_file_name) as f:
            self.template: Template = jinja2.Template(source=f.read())

    def execute(self, problem: Problem) -> None:
        """
        Produce the HTML output of the puzzle.

        This function renders the jinja2 template using the values of the problem as
        variables. The rendered HTML is stored in the problem in the field
        specified by field_name.

        Parameters:
            problem (Problem): The problem to render
        Returns:
            None
        """
        super().execute(problem)
        logging.info("Producing html file")
        problem[self.field_name] = self.template.render(problem)

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}('{self.template_file_name}', '{self.field_name}')"
