"""FileWriterCommand."""
from pathlib import Path
from xml.dom.minidom import Document

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.commands.svg_command import SVGAnswerCommand
from src.commands.svg_command import SVGPencilMarkCommand
from src.commands.svg_command import SVGProblemCommand
from src.commands.svg_command import SVGSolutionCommand


class FileWriterCommand(SimpleCommand):
    """Write output into start file_path."""

    def __init__(self):
        """Initialize FileWriterCommand."""
        super().__init__()
        self.target_file_path: Path | None = None

    def work(self, problem: Problem) -> None:
        """Write to start file_path.

        Args:
            problem (Problem): The problem to load the file_path and file_path name into.

        Raises:
            CommandException: If an error occurs while writing the file_path.
            CommandException: If the target file_path is not set.
        """
        super().work(problem)
        if self.target_file_path is None:
            raise CommandException(f'Target file_path is not set {self.name}.')
        target_file_path: Path = problem.output_directory / self.target_file_path
        data = getattr(problem, self.source)
        try:
            with target_file_path.open(mode='w', encoding='utf-8') as file_handler:
                if isinstance(data, str):
                    file_handler.write(data)
                if isinstance(data, Document):
                    file_handler.write(data.toprettyxml(indent='  '))
        except Exception as exc:
            raise CommandException(f'Failed to write {target_file_path!s}: {exc}') from exc

    def __repr__(self) -> str:
        """Return a string representation of the command.

        Returns:
            str: The string representation of the command
        """
        return f'{self.__class__.__name__}()'


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
