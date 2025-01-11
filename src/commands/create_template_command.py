"""LoadTemplateCommand."""

from abc import ABC

from jinja2 import Environment, FileSystemLoader

from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.config import Config

config = Config()

env = Environment(loader=FileSystemLoader(config.temporary_directory), autoescape=True)


class CreateTemplateCommand(SimpleCommand, ABC):
    """Create Template into the problem."""

    def __init__(self):
        """Create the command."""
        super().__init__()
        self.template_name: str | None = None

    def work(self, problem: Problem) -> None:
        """Produce the Jinja2 template.

        Create the template from the Jinja2 template string and store it in the problem

        Args:
            problem (Problem): The problem to render.
        """
        super().work(problem)
        setattr(problem, self.target, env.get_template(self.template_name))


class CreateIndexTemplate(CreateTemplateCommand):
    """Create Index Template into the problem."""

    def __init__(self):
        """Create the command."""
        super().__init__()
        self.target = 'index_template'
        self.template_name = 'index.html'


class CreateProblemTemplate(CreateTemplateCommand):
    """Create Problem Template into the problem."""

    def __init__(self):
        """Create the command."""
        super().__init__()
        self.target = 'index_template'
        self.template_name = 'problem.html'
