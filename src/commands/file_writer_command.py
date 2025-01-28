"""FileWriterCommand."""
from pathlib import Path
from xml.dom.minidom import Document

import oyaml as yaml

from src.commands.command import CommandException
from src.commands.create_linear_program_command import CreateLinearProgramCommand
from src.commands.create_rules_command import CreateRulesCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.commands.svg_command import SVGAnswerCommand  # noqa: I001
from src.commands.svg_command import SVGPencilMarkCommand  # noqa: I001
from src.commands.svg_command import SVGProblemCommand  # noqa: I001
from src.commands.svg_command import SVGSolutionCommand  # noqa: I001


# flake8: noqa WPS202
# TODO Remove above

class FileWriterCommand(SimpleCommand):
    """Write output into start_location file_path."""

    def __init__(self):
        """Initialize FileWriterCommand."""
        super().__init__()
        self.target_file_path: Path | None = None
        self.source: str | None = None

    def work(self, problem: Problem) -> None:
        """Write to start_location file_path.

        Args:
            problem (Problem): The problem to load the file_path and file_path name into.

        Raises:
            CommandException: If an error occurs while writing the file_path.
            CommandException: If the target file_path is not set.
            CommandException: If the source is not set.
        """
        super().work(problem)
        if self.target_file_path is None:
            raise CommandException(f'Target file_path is not set {self.name}.')
        target_file_path: Path = problem.output_directory / self.target_file_path
        if self.source is None:
            raise CommandException(f'Source is not set {self.name}.')
        data_to_write = getattr(problem, self.source)
        try:
            with target_file_path.open(mode='w', encoding='utf-8') as file_handler:
                if isinstance(data_to_write, str):
                    file_handler.write(data_to_write)
                if isinstance(data_to_write, Document):
                    file_handler.write(data_to_write.toprettyxml(indent='  '))
        except Exception as exc:
            raise CommandException(f'Failed to write {target_file_path!s}: {exc}') from exc

    def __repr__(self) -> str:
        """Return a string representation of the command.

        Returns:
            str: The string representation of the command
        """
        return f'{self.__class__.__name__}()'


class PythonToYamlCommand(SimpleCommand):
    """Output a python object as yaml."""

    def __init__(self):
        """Initialize FileWriterCommand."""
        super().__init__()
        self.target: str | None = None
        self.source: str | None = None

    def work(self, problem: Problem) -> None:
        """Write to start_location file_path.

        Args:
            problem (Problem): The problem to load the file_path and file_path name into.

        Raises:
            CommandException: If an error occurs while writing the file_path.
            CommandException: If the target file_path is not set.
        """
        super().work(problem)
        if self.target is None:
            raise CommandException(f'Target is not set {self.name}.')
        if self.source is None:
            raise CommandException(f'Source is not set {self.name}.')
        text: str = yaml.dump(self.convert(problem), sort_keys=False, indent=2, encoding=None)
        setattr(problem, self.target, text)

    def convert(self, problem: Problem) -> dict:
        """Convert data item in problem to dictionary so it can be written out as yaml. Default just gets the data.

        Args:
            problem (Problem): The problem to convert.

        Returns:
            dict: A dictionary representation of the data.

        Raises:
            CommandException: If the source is not set.
            CommandException: If the source is not set.
        """
        if self.source is None:
            raise CommandException(f'Source is not set {self.name}.')
        if not isinstance(getattr(problem, self.source), dict):
            raise CommandException(f'Cannot convert {self.source} to dictionary.')
        data: dict = getattr(problem, self.source)
        return data


class RulesToYamlCommand(PythonToYamlCommand):
    """Convert rules to yaml."""

    def __init__(self):
        """Initialize RulesToYamlCommand."""
        super().__init__()
        self.source: str = 'rules'
        self.target: str = 'rule_text'
        self.add_preconditions([CreateRulesCommand])

    def convert(self, problem: Problem) -> dict:
        """Convert rules to dictionary so it can be written out as yaml.

        Args:
            problem (Problem): The problem to convert.

        Returns:
            dict: A dictionary representation of the rules.
        """
        return {'Rules': [data_item.to_dict() for data_item in getattr(problem, self.source)]}


class RuleWriterCommand(FileWriterCommand):
    """Writer riles into a file."""

    def __init__(self) -> None:
        """Initialize RuleWriterCommand."""
        super().__init__()
        self.source: str = 'rule_text'
        self.add_preconditions([RulesToYamlCommand])
        self.target_file_path: Path = Path('rules.yaml')


class SVGPencilMarkWriterCommand(FileWriterCommand):
    """Write SVG svg_pencil_mark into a file."""

    def __init__(self) -> None:
        """Initialize SVGFileWriterCommand."""
        super().__init__()
        self.source: str = 'problem'
        self.add_preconditions([SVGPencilMarkCommand])
        self.target_file_path: Path = Path('svg_pencil_mark.svg')


class SVGProblemWriterCommand(FileWriterCommand):
    """Write SVG svg_problem into a file."""

    def __init__(self) -> None:
        """Initialize SVGFileWriterCommand."""
        super().__init__()
        self.source: str = 'svg_problem'
        self.add_preconditions([SVGProblemCommand])
        self.target_file_path: Path = Path('svg_problem.svg')


class SVGSolutionWriterCommand(FileWriterCommand):
    """Write SVG solution into a file."""

    def __init__(self) -> None:
        """Initialize SVGFileWriterCommand."""
        super().__init__()
        self.source: str = 'answer'
        self.add_preconditions([SVGSolutionCommand])
        self.target_file_path: Path = Path('solution.svg')


class SVGAnswerFileWriterCommand(FileWriterCommand):
    """Write SVG answer into a file."""

    def __init__(self) -> None:
        """Initialize SVGFileWriterCommand."""
        super().__init__()
        self.source: str = 'answer'
        self.add_preconditions([SVGAnswerCommand])
        self.target_file_path: Path = Path('answer.svg')


class LPFileWriterCommand(FileWriterCommand):
    """Write LP file into a file."""

    def __init__(self) -> None:
        """Initialize LPFileWriterCommand."""
        super().__init__()
        self.source: str = 'linear_program'
        self.add_preconditions([CreateLinearProgramCommand])
        self.target_file_path = Path('problem.lp')
