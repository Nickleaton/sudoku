"""LoadTemplateCommand."""

from jinja2 import Template

from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class RenderTemplateCommand(SimpleCommand):
    """Render the problem using start Jinja2 template."""

    def __init__(self, template_name: str, target: str):
        """Create the command.

        Args:
            template_name (str): Name of the Jinja2 template string to use for generating the HTML.
            target (str): Name of the field in the problem that will contain the template
        """
        super().__init__()
        self.template_name: str = template_name
        self.target: str = target

        self.input_types: list[KeyType] = [
            KeyType(self.template_name, Template),
        ]
        self.output_types: list[KeyType] = [
            KeyType(self.target, str),
        ]

    def work(self, problem: Problem) -> None:
        """Produce the Jinja2 template.

        Create the template from the Jinja2 template string and store it in the problem

        Args:
            problem (Problem): The problem to render.
        """
        super().work(problem)
        problem[self.target] = problem[self.template_name].render(problem)
