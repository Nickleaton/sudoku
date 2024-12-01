"""LoadTemplateCommand."""
import logging
from pathlib import Path

import jinja2
from jinja2 import Template

from src.commands.key_type import KeyType

from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class TemplateCommand(SimpleCommand):
    """Render the problem using a Jinja2 template."""

    def __init__(self, template_raw: str, target: str):
        """Create the command.

        Args:
            template_raw (str): Name of the Jinja2 template string to use for generating the HTML.
            target (str): Name of the field in the problem that will contain the template
        """
        super().__init__()
        self.template_raw: str = template_raw
        self.target: str = target


        self.inputs: list[KeyType] = [
            KeyType(self.template_file.name, str)
        ]
        self.outputs: list[KeyType] = [
            KeyType(self.target, Template)
        ]


    def work(self, problem: Problem) -> None:
        """Produce the Jinja2 template.

        Create the template from the Jinja2 template string and store it in the problem

        Args:
            problem (Problem): The problem to render.

        Returns:
            None
        """
        problem[self.target] = jinja2.Template(problem[self.template_raw])

