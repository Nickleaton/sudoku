"""CreateTemplateCommand."""

from jinja2 import Template

from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class CreateTemplateCommand(SimpleCommand):
    """Create Template into the problem."""

    def __init__(self, source: str, target: str):
        """Create the command.

        Args:
            source (str): Name of the Jinja2 template string to use for generating the HTML.
            target (str): Name of the field in the problem that will contain the template
        """
        super().__init__()
        self.source: str = source
        self.target: str = target

        self.input_types: list[KeyType] = [
            KeyType(source, str)
        ]
        self.output_types: list[KeyType] = [
            KeyType(target, Template)
        ]

    def work(self, problem: Problem) -> None:
        """Produce the Jinja2 template.

        Create the template from the Jinja2 template string and store it in the problem

        Args:
            problem (Problem): The problem to render.

        Returns:
            None
        """
        problem[self.target] = Template(problem[self.source])
