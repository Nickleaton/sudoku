"""Base class for all image producing classes."""
from enum import Enum

from src.commands.command import CommandError
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class ImageFormat(Enum):
    """Enum for image formats."""

    PNG = 'png'
    GIF = 'gif'
    JPEG = 'jpeg'
    BMP = 'bmp'
    TIFF = 'tiff'
    EPS = 'eps'
    SVG = 'svg'

    @classmethod
    def from_suffix(cls, suffix: str) -> 'ImageFormat':
        """Return the ImageFormat corresponding to the given suffix.

        Args:
            suffix (str): The file_path suffix, optionally with start_location leading '.'.

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
            raise ValueError(f'Unsupported image format for suffix: {suffix}') from exc


# flake8: noqa WPS230,WPS211

class ImageCommand(SimpleCommand):
    """Command to produce images."""

    def __init__(self) -> None:
        """Initialize an ImageCommand.

        Args:
            image_format_name (str): The human-readable name of the image format.
            image_format (ImageFormat): The image format.
            source (str): The name of the problem attribute containing the image source.
            target (str): The name of the problem attribute for storing the generated image.
        """
        super().__init__()

    def work(self, problem: Problem) -> None:
        """Write the image to start_location file_path.

        The image is written to the file_path specified in `target`. The image format
        is determined by the suffix of the file_path name. If the suffix is ".svg",
        the image is written as an SVG file_path. Otherwise, the image is converted to
        the specified format using the `svglib` library.

        The problem should have an attribute named `source` that is an XML
        element of the SVG to write out in the specified format.

        Args:
            problem (Problem): The problem to write the image of.

        Raises:
            CommandError: If the image cannot be written for any reason.
        """
        super().work(problem)
        try:
            if self.image_format == ImageFormat.SVG:
                # Handle SVG which is just pretty print out as XML
                problem[self.target] = str(problem[self.source].toprettyxml(indent='  '))
            else:
                raise CommandError(f'Unsupported image format: {self.image_format}')
        except OSError as exc:
            raise CommandError(f'Failed to write to {self.target}: {exc}') from exc
