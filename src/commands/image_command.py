"""
Base class for all image producing classes.
"""
import logging
from enum import Enum
from pathlib import Path

from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.file_handling import is_writeable_file


class ImageFormat(Enum):
    """Enum for image formats."""
    PNG = "png"
    GIF = "gif"
    JPEG = "jpeg"
    BMP = "bmp"
    TIFF = "tiff"
    EPS = "eps"
    SVG = "svg"

    @classmethod
    def from_suffix(cls, suffix: str) -> 'ImageFormat':
        """
        Return the ImageFormat corresponding to the given suffix.

        Args:
            suffix (str): The file suffix, optionally with a leading '.'.

        Returns:
            ImageFormat: The corresponding ImageFormat.

        Raises:
            ValueError: If the suffix is not supported.
        """
        suffix = suffix.lower().lstrip('.')
        # Try to return the corresponding ImageFormat
        try:
            return cls(suffix)
        except ValueError:
            raise ValueError(f"Unsupported image format for suffix: {suffix}")


class ImageCommand(SimpleCommand):

    def __init__(self, source: str, target: Path | str) -> None:
        """
        Initialize an ImageCommand.

        Args:
            source (str): The attribute of the problem to write out.
            target (Path | str): The name of the file to write to.

        Raises:
            ValueError: If the target has an unsupported suffix.
        """
        super().__init__()
        self.target: Path = Path(target) if isinstance(target, str) else target
        self.source: str = source
        self.image_format: ImageFormat = ImageFormat.from_suffix(self.target.suffix)

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        Args:
            problem (Problem): The problem to check.

        Raises:
            CommandException: If the preconditions are not met.
        """
        if self.source not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.source} not in problem')
        if not is_writeable_file(self.target):
            raise CommandException(f'{self.__class__.__name__} - {self.target} is not writeable')

    def execute(self, problem: Problem) -> None:
        """
        Write the image to a file.

        The image is written to the file specified in `target`. The image format
        is determined by the suffix of the file name. If the suffix is ".svg",
        the image is written as an SVG file. Otherwise, the image is converted to
        the specified format using the `svglib` library.

        The problem should have an attribute named `source` that is an XML
        element of the SVG to write out in the specified format.

        Args:
            problem (Problem): The problem to write the image of.

        Raises:
            CommandException: If the image cannot be written for any reason.
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        if self.image_format == ImageFormat.SVG:
            # Handle SVG which is just pretty print out as XML
            with open(self.target, 'wb') as f:
                text: str = str(problem[self.source].toprettyxml(indent="  "))
                f.write(text.encode('utf-8'))
        else:
            # For other formats, use renderPM to convert the XML to the specified format
            drawing = svg2rlg(problem[self.source])
            renderPM.drawToFile(drawing, self.target.name, fmt=self.image_format.name)

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        The string is of the form "ImageCommand(problem_field, file_name)". The
        representation is useful for debugging and logging.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({self.source!r}, {self.target!r})"
