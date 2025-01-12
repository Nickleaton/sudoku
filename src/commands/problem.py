"""Problem module."""

from pathlib import Path
from xml.dom.minidom import Document

from jinja2 import Template
from pydotted import pydot

from src.board.board import Board
from src.items.constraints import Constraints
from src.solvers.answer import Answer
from src.solvers.solver import Solver
from src.utils.rule import Rule
from src.utils.tags import Tags


class Problem:
    """Container for the components of a problem."""

    def __init__(self, problem_file_name: Path, output_directory: Path) -> None:
        """Initialize a new instance of the Problem class.

        Args:
            problem_file_name (Path): The path to the problem file.
            output_directory (Path): The path to the output directory.

        Raises:
            FileNotFoundError: If the problem file does not exist.
            NotADirectoryError: If the output directory is not a directory.
        """
        if not problem_file_name.exists():
            raise FileNotFoundError(f'File "{problem_file_name}" does not exist.')
        if output_directory.exists() and not output_directory.is_dir():
            raise NotADirectoryError(f'Output directory "{output_directory}" is not a directory.')
        self.problem_file_name: Path = problem_file_name
        self.output_directory: Path = output_directory

        # Optional fields (initialized as None)
        self.constraints: Constraints | None = None
        self.raw_config: str | None = None
        self.config: pydot | None = None
        self.board: Board | None = None
        self.solver: Solver | None = None
        self.yaml_output_string: str | None = None
        self.meta: Tags | None = None
        self.rules: list[Rule] | None = None
        self.bookkeeping_unique: str | None = None
        self.linear_program: str | None = None
        self.index_template: Template | None = None
        self.problem_template: Template | None = None
        self.svg_problem: Document | None = None
        self.svg_solution: Document | None = None
        self.svg_pencil_mark: Document | None = None
        self.answer: Answer | None = None
        self.validation: str | None = None
        self.index_html: str | None = None
        self.problem_html: str | None = None

    def __repr__(self) -> str:
        """Return a detailed string representation of the problem.

        Returns:
            str: The string representation of the problem
        """
        return (
            f'Problem('
            f'problem_file_name={self.problem_file_name!r}, '
            f'output_directory={self.output_directory!r}, '
            f'solver={self.solver!r})'
        )

    def __str__(self) -> str:
        """Return a user-friendly string representation of the problem.

        Returns:
            str: The string representation of the problem
        """
        return (
            f'Problem file: {self.problem_file_name}, '
            f'Output directory: {self.output_directory}'
        )
