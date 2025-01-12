"""RenderTemplateCommands."""
from jinja2 import Environment, FileSystemLoader, Template

from src.commands.create_meta_command import CreateMetaCommand
from src.commands.create_rules_command import CreateRulesCommand
from src.commands.file_writer_command import SVGProblemWriterCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.config import Config

config = Config()

env = Environment(loader=FileSystemLoader(config.temporary_directory), autoescape=True)


class RenderTemplateCommand(SimpleCommand):
    """Render the problem using start Jinja2 template."""

    def __init__(self):
        """Create the command.

        Args:
            template_name (str): Name of the Jinja2 template string to use for generating the HTML.
            target (str): Name of the field in the problem that will contain the template
        """
        super().__init__()
        self.template: Template | None = None

    def work(self, problem: Problem) -> None:
        """Produce the Jinja2 template.

        Create the template from the Jinja2 template string and store it in the problem

        Args:
            problem (Problem): The problem to render.
        """
        super().work(problem)
        setattr(problem, self.target, self.template.render(problem))


class RenderIndexTemplate(RenderTemplateCommand):
    """Render Index Template into the problem."""

    def __init__(self):
        """Create the command."""
        super().__init__()
        self.add_preconditions([CreateMetaCommand, CreateRulesCommand, SVGProblemWriterCommand])
        self.target = 'index_html'
        self.template: Template = env.get_template('index.html')


class RenderProblemTemplate(RenderTemplateCommand):
    """Render Problem Template into the problem."""

    def __init__(self):
        """Create the command."""
        super().__init__()
        self.add_preconditions([CreateMetaCommand, CreateRulesCommand, SVGProblemWriterCommand])
        self.target = 'problem_html'
        self.template: Template = env.get_template('problem.html')
