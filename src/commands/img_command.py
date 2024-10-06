""" Base class for all image producing classes"""
from enum import Enum
from pathlib import Path

from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.file_handling import check_if_writable


class ImageFormat(Enum):
    """ Enum for image formats """
    PNG = "png"
    GIF = "gif"
    JPEG = "jpeg"
    BMP = "bmp"
    TIFF = "tiff"
    EPS = "eps"
    SVG = "svg"

    @classmethod
    def from_suffix(cls, suffix: str):
        # Remove the leading '.' from the suffix
        """
        Return the ImageFormat corresponding to the given suffix.

        :param suffix: The file suffix, optionally with a leading '.'
        :return: The corresponding ImageFormat
        :raises ValueError: If the suffix is not supported
        """
        suffix = suffix.lower().lstrip('.')
        # Try to return the corresponding ImageFormat
        try:
            return cls(suffix)
        except ValueError:
            raise ValueError(f"Unsupported image format for suffix: {suffix}")


class IMGCommand(SimpleCommand):

    def __init__(self, problem_field: str, file_name: Path) -> None:
        """
        Initialize an IMGCommand.

        :param problem_field: The attribute of the problem to write out
        :param file_name: The name of the file to write to
        :raises ValueError: If the file_name has an unsupported suffix
        """
        super().__init__()
        self.file_name: Path = file_name
        self.problem_field: str = problem_field
        self.image_format: ImageFormat = ImageFormat.from_suffix(file_name.suffix)

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        :param problem: The problem to check
        :raises CommandException: If the preconditions are not met
        """
        if self.problem_field not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.problem_field} not in problem')
        if problem[self.problem_field] is None:
            raise CommandException(f'{self.__class__.__name__} - {self.problem_field} is None')
        if self.file_name.exists():
            if not self.file_name.is_file():
                raise CommandException(f'{self.__class__.__name__} - {self.file_name} exists and is not a file')
            if not check_if_writable(self.file_name):
                raise CommandException(f'{self.__class__.__name__} - {self.file_name} is not writeable')

    def execute(self, problem: Problem) -> None:
        """
        Write the image to a file.

        The image is written to the file specified in :attr:`file_name`. The
        image format is determined by the suffix of the file name. If the
        suffix is ".svg", the image is written as an svg file. Otherwise, the
        image is converted to the specified format using the svglib library.

        See ImageFormat for a list of supported image formats.

        the problem should have an attribute named :attr:`problem_field` that is an xml
        element of the svg to write out in the specified format

        :param problem: The problem to write the image of.
        :type problem: Problem
        :raises CommandException: If the image cannot be written for any
            reason.
        """
        super().execute(problem)
        if self.image_format == ImageFormat.SVG:
            # handle svg which is just pretty print out as xml
            with open(self.file_name, 'wb') as f:
                text: str =  str(problem[self.problem_field].toprettyxml(indent="  "))
                f.write(text.encode('utf-8'))
        else:
            # for other formats, use renderPM to convert the xml to the specified format
            drawing = svg2rlg(problem[self.problem_field])
            renderPM.drawToFile(drawing, self.file_name.name, fmt=self.image_format.name)

    def __repr__(self):
        """
        Return a string representation of the object.

        The string is of the form "IMGCommand(problem_field, file_name)". The
        representation is useful for debugging and logging.

        :return: A string representation of the object.
        :rtype: str
        """
        return f"{self.__class__.__name__}({repr(self.problem_field)}, {repr(self.file_name)})"
