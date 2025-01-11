"""LoadTemplateCommand."""

from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class RenderTemplateCommand(SimpleCommand):
    """Render the problem using start Jinja2 template."""

    def __init__(self):
        """Create the command.

        Args:
            template_name (str): Name of the Jinja2 template string to use for generating the HTML.
            target (str): Name of the field in the problem that will contain the template
        """
        super().__init__()


    def work(self, problem: Problem) -> None:
        """Produce the Jinja2 template.

        Create the template from the Jinja2 template string and store it in the problem

        Args:
            problem (Problem): The problem to render.
        """
        super().work(problem)
        problem[self.target] = problem[self.template_name].render(problem)
