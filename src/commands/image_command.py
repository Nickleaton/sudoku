"""Base class for all image producing classes."""
import logging
from enum import Enum
from xml.dom.minidom import Document

from src.commands.command import CommandException
from src.commands.key_type import KeyType
from src.commands.parameter_value_type import ParameterValueType
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

    def __init__(self, image_format_name: str, image_format: ImageFormat, source: str, target: str) -> None:
        """Initialize an ImageCommand.

        Args:
            image_format_name (str): The human-readable name of the image format.
            image_format (ImageFormat): The image format.
            source (str): The name of the problem attribute containing the image source.
            target (str): The name of the problem attribute for storing the generated image.

        Raises:
            ValueError: If the target file has an unsupported suffix.
        """
        super().__init__()
        self.source: str = source
        self.target: str = target
        self.image_format_name: str = image_format_name
        self.image_format: ImageFormat = image_format
        self.parameters: list[ParameterValueType] = [
            ParameterValueType(image_format_name, image_format, ImageFormat)
        ]
        self.input_types: list[KeyType] = [
            KeyType(source, Document),
        ]
        self.output_types: list[KeyType] = [
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
                problem[self.target] = str(problem[self.source].toprettyxml(indent="  "))
            else:
                raise CommandException(f"Unsupported image format: {self.image_format}")
        except OSError as exc:
            raise CommandException(f"Failed to write to {self.target}: {exc}") from exc
