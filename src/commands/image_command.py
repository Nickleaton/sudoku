"""Base class for all image producing classes."""
import logging
from enum import Enum
from pathlib import Path

from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

from src.commands.command import CommandException
from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


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
        """Return the ImageFormat corresponding to the given suffix.

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
        except ValueError as exc:
            raise ValueError(f"Unsupported image format for suffix: {suffix}") from exc


class ImageCommand(SimpleCommand):
    """Command to produce images."""

    def __init__(self, source: str, target: str) -> None:
        """Initialize an ImageCommand.

        Args:
            source (str): The attribute of the problem to write out.
            target (Path): the attribute to add to the problem.

        Raises:
            ValueError: If the target has an unsupported suffix.
        """
        super().__init__()
        self.source: str = source
        self.target: str = target
        self.image_format: ImageFormat = ImageFormat.from_suffix(self.target.suffix)
        self.inputs: list[KeyType] = [
            KeyType(source, str),
        ]
        self.outputs: list[KeyType] = [
            KeyType(target, str)
        ]

    def work(self, problem: Problem) -> None:
        """Write the image to a file.

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
        super().work(problem)
        logging.info(f"Creating {self.target}")
        try:
            if self.image_format == ImageFormat.SVG:
                # Handle SVG which is just pretty print out as XML
                with self.target.open(mode='wb', encoding='utf-8') as f:
                    text: str = str(problem[self.source].toprettyxml(indent="  "))
                    f.write(text.encode('utf-8'))
            else:
                # For other formats, use renderPM to convert the XML to the specified format
                drawing = svg2rlg(problem[self.source])
                renderPM.drawToFile(drawing, self.target.name, fmt=self.image_format.name)
        except OSError as exc:
            raise CommandException(f"Failed to write to {self.target}: {exc}") from exc
