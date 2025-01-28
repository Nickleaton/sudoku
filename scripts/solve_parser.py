"""Parser for the solve script."""
import argparse
from pathlib import Path

from solve import logger


def validate_output_directory(output_path: Path) -> None:
    """Validate the output directory.

    Args:
        output_path (Path): The output directory path.

    Raises:
        ValueError: If the output path exists and is not a directory.

    Logs:
        Logs an error if the output path is invalid.
    """
    if output_path.exists() and not output_path.is_dir():
        logger.error(f'Output path {output_path!s} is not a valid directory.')
        raise ValueError(f'Output path {output_path!s} is not a valid directory.')


def validate_input_file(input_path: Path) -> None:
    """Validate if the input path is a valid file.

    Args:
        input_path (Path): The input file path.

    Raises:
        ValueError: If the input path is not a file or does not exist.

    Logs:
        Logs an error if the input file is invalid.
    """
    if input_path.is_file() and not input_path.exists():
        logger.error(f'Input file {input_path!s} does not exist.')
        raise ValueError(f'Input file {input_path!s} does not exist.')


def validate_input_directory(input_path: Path) -> None:
    """Validate if the input path is a valid directory containing YAML files.

    Args:
        input_path (Path): The input directory path.

    Raises:
        ValueError: If the directory does not contain any YAML files.

    Logs:
        Logs an error if the directory is invalid or empty.
    """
    if input_path.is_dir():
        yaml_files = list(input_path.glob('*.yaml')) + list(input_path.glob('*.yml'))
        if not yaml_files:
            logger.error(f'Input directory {input_path!s} does not contain any YAML files.')
            raise ValueError(f'Input directory {input_path!s} does not contain any YAML files.')


def validate_input_path(input_path: Path) -> None:
    """Validate the input path, whether it's a file or directory.

    Args:
        input_path (Path): The input file or directory path.

    Raises:
        ValueError: If the input path is neither a file nor a directory.

    Logs:
        Logs an error if the input path is invalid.
    """
    if not (input_path.is_file() or input_path.is_dir()):
        logger.error(f'Input path {input_path!s} is neither a file nor a directory.')
        raise ValueError(f'Input path {input_path!s} is neither a file nor a directory.')


def validate_args(input_path: Path, output_path: Path) -> None:
    """Validate the input and output arguments.

    Args:
        input_path (Path): The input file or directory path.
        output_path (Path): The output directory path.

    Logs:
        Logs errors if any validation fails.
    """
    logger.info(f'Validating arguments: input={input_path!s}, output={output_path!s}')

    # Validate the output directory
    validate_output_directory(output_path)

    # Validate the input path based on whether it's a file or directory
    if input_path.is_file():
        validate_input_file(input_path)
    elif input_path.is_dir():
        validate_input_directory(input_path)

    # Check if input_path is either a file or directory
    validate_input_path(input_path)


def get_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    commands = ['schema', 'solve', 'validate', 'problem', 'lp', 'rules']

    argument_parser = argparse.ArgumentParser(description='Process some commands.')

    argument_parser.add_argument(
        '--input',
        type=Path,
        required=True,
        help='The input file or directory (as a Path).',
    )
    argument_parser.add_argument(
        '--output',
        type=Path,
        required=True,
        help='The output directory.',
    )
    argument_parser.add_argument(
        'commands',
        nargs='+',
        choices=commands,
        help='List of commands to run.',
    )

    return argument_parser
