"""Problem module."""

from pathlib import Path

from pydotted import pydot


class Problem(pydot):
    """A container for the components of a problem.

    Represents a dynamic container for the components of a problem.
    Inherits from the `pydotted` library to enable dot notation access
    for its attributes.
    """

    def __init__(self, problem_file: Path, output_directory: Path) -> None:
        super().__init__()
        if not problem_file.exists():
            raise FileNotFoundError(f"File {problem_file} does not exist")
        self.problem_file: Path = problem_file
        if output_directory.exists():
            if not output_directory.is_dir():
                raise NotADirectoryError(f"Output directory {output_directory} is not a directory")
        self.output_directory: Path = output_directory

    def __str__(self) -> str:
        """Convert the problem's keys to a string representation.

        Returns:
            str: A string listing the keys.
        """
        return f"| {', '.join(self.keys())} |"
