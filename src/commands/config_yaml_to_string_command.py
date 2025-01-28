"""ConfigYamlToStringCommand."""

import oyaml as yaml

from src.commands.command import CommandException
from src.commands.create_config_command import CreateConfigCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand

# Register None-type representation in YAML as an empty string
yaml.add_representer(type(None), lambda dumper, _: dumper.represent_scalar('tag:yaml.org,2002:null', ''))


class ConfigYamlToStringCommand(SimpleCommand):
    """Write configuration line to start_location YAML file_path."""

    def __init__(self):
        """Initialize start_location ConfigYamlToStringCommand instance."""
        super().__init__()
        self.add_preconditions([CreateConfigCommand])
        self.target = 'yaml_output_string'

    def work(self, problem: Problem) -> None:
        """Write the configuration to the target string.

        Args:
            problem (Problem): The problem instance containing the configuration line.

        Raises:
            CommandException: If the configuration line is not available.
        """
        super().work(problem)
        if problem.config is None:
            raise CommandException(f'Constraints must be set before {self.name}.')
        problem.yaml_output_string = yaml.dump(problem.config, default_style=None)
