"""Doc Commands Parser."""
import argparse
import logging
from pathlib import Path

from doc_commands import CommandValidationError
from doc_commands import DirectoryValidationError
from src.commands.command import Command


def validate_output_directory(output_dir: Path) -> None:
    """Validate the output directory exists and is a directory.

    Args:
        output_dir (Path): The directory to validate.

    Raises:
        DirectoryValidationError: If the directory does not exist or is not a directory.
    """
    if not output_dir.exists():
        logging.info(f'Creating output directory: {output_dir}')
        output_dir.mkdir(parents=True, exist_ok=True)

    if not output_dir.is_dir():
        raise DirectoryValidationError(f'The specified output path is not a directory: {output_dir}')


def validate_commands() -> None:
    """Validate that command modules are loaded and that Command.classes is populated.

    Raises:
        CommandValidationError: If no commands are found in Command.classes.
    """
    if not Command.classes:
        raise CommandValidationError('No commands found in Command.classes. Ensure modules are loaded correctly.')


def create_arg_parser() -> argparse.ArgumentParser:
    """Create an argument parser for command-line arguments.

    Returns:
        argparse.ArgumentParser: The argument parser instance configured with a description
        and an output directory argument.
    """
    parser = argparse.ArgumentParser(description='Generate DOT, SVG, and JPG files for command dependencies.')
    parser.add_argument(
        'output',
        type=Path,
        help='The output directory for the generated files.',
    )
    return parser
