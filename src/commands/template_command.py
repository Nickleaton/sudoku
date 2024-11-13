"""
Command to produce an HTML file of the puzzle.
"""
import logging
from pathlib import Path
from typing import Optional

import jinja2
from jinja2 import Template

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.file_handling import is_readable_file


class TemplateCommand(SimpleCommand):
    """Render the problem using a Jinja2 template."""

    def __init__(self, template: Path | str, target: str):
        """Create the command.

        Args:
            template (Path | str): Name of the Jinja2 template to use for generating the HTML.
            target (str): Name of the field in the problem that will contain the HTML.
        """
        super().__init__()
        self.template_file: Path = Path(template) if isinstance(template, str) else template
        self.target: str = target
        self.template: Optional[Template] = None

    def precondition_check(self, problem: Problem) -> None:
        """Check the preconditions for the command.

        This method checks that the target attribute does not already exist in the
        problem's configuration and that the source file exists and is readable.

        Args:
            problem (Problem): The problem to check.

        Raises:
            CommandException: If the preconditions are not met.
        """
        if not is_readable_file(self.template_file):
            raise CommandException(
                f'{self.__class__.__name__} - {self.template_file} does not exist or is not readable '
            )
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already exists')

    def execute(self, problem: Problem) -> None:
        """Produce the HTML output of the puzzle.

        This function renders the Jinja2 template using the values of the problem as
        variables. The rendered HTML is stored in the problem in the field specified by target.

        Args:
            problem (Problem): The problem to render.

        Returns:
            None
        """
        if self.template is None:
            logging.info(f"Loading template {self.template_file}")
            with open(self.template_file, encoding='utf-8') as f:
                self.template = jinja2.Template(source=f.read())
        logging.info(f"Creating {self.target}")
        problem[self.target] = self.template.render(problem)

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({str(self.template_file)!r}, {self.target!r})"
