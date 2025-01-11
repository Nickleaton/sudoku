import argparse
import itertools
import logging.config
from pathlib import Path

from src.commands.command import Command
from src.commands.problem import Problem
from src.commands.validate_config_command import ValidateConfigCommand
from src.utils.config import Config

config: Config = Config()
logging.config.dictConfig(Config().get_dict('logging'))
logger = logging.getLogger("solve")


def process_schema(problem: Problem) -> None:
    """Processes the schema command.

    Args:
        problem (Problem): The problem instance to process.
    """
    logger.info(f"Processing schema for file: {problem.problem_file_name}")
    command: Command = ValidateConfigCommand()
    command.execute(problem=problem)
    if problem.validation != "OK":
        raise ValueError(problem.validation)
    logger.info(f"Schema validation OK for file: {problem.problem_file_name}")


def process_solve(problem: Problem) -> None:
    """Processes the solve command.

    Args:
        problem (Problem): The problem instance to process.
    """
    logger.info(f"Processing solve for file: {problem.problem_file_name} with output: {problem.output_directory}")


def process_validate(problem: Problem) -> None:
    """Processes the validate command.

    Args:
        problem (Problem): The problem instance to process.
    """
    logger.info(f"Processing validate for file: {problem.problem_file_name} with output: {problem.output_directory}")


def process_problem(problem: Problem) -> None:
    """Processes the problem command.

    Args:
        problem (Problem): The problem instance to process.
    """
    logger.info(f"Processing problem for file: {problem.problem_file_name} with output: {problem.output_directory}")


def process_command(command: str, input_file: Path, output_path: Path) -> None:
    """Processes a single command by dispatching it to the appropriate handler.

    Args:
        command (str): The command to process.
        input_file (Path): The input file path.
        output_path (Path): The output directory path.
    """
    problem: Problem = Problem(input_file, output_path)
    match command:
        case 'schema':
            process_schema(problem)
        case 'solve':
            process_solve(problem)
        case 'validate':
            process_validate(problem)
        case 'problem':
            process_problem(problem)
        case _:
            logger.error(f"Unknown command: {command}")


def process(commands: list[str], files_path: Path, output_path: Path) -> None:
    """Processes all combinations of commands and files.

    Args:
        commands (list[str]): List of commands to process.
        files_path (Path): List of input file paths.
        output_path (Path): The output directory path.
    """
    if not output_path.exists():
        logger.info(f"Creating output directory: {output_path}")
        output_path.mkdir(parents=True)
    files: list[Path] = [files_path] if files_path.is_file() else [f for f in files_path.glob('*.yaml')]
    for file_name, command in itertools.product(files, commands):
        process_command(command, file_name, output_path)


def validate_args(input_path: Path, output_path: Path) -> None:
    """Validates the input and output arguments.

    Args:
        input_path (Path): The input file or directory path.
        output_path (Path): The output directory path.

    Raises:
        ValueError: If any validation check fails.
    """
    logger.info(f"Validating arguments: input='{input_path}', output='{output_path}'")

    # Check if the output is a directory
    if output_path.exists() and not output_path.is_dir():
        logger.error(f"Output path '{output_path}' is not a valid directory.")
        raise ValueError(f"Output path '{output_path}' is not a valid directory.")

    # Check if the input path is a file
    if input_path.is_file():
        if not input_path.exists():
            logger.error(f"Input file '{input_path}' does not exist.")
            raise ValueError(f"Input file '{input_path}' does not exist.")
    # Check if the input path is a directory
    elif input_path.is_dir():
        # Check if the directory contains at least one YAML file
        yaml_files = list(input_path.glob("*.yaml")) + list(input_path.glob("*.yml"))
        if not yaml_files:
            logger.error(f"Input directory '{input_path}' does not contain any YAML files.")
            raise ValueError(f"Input directory '{input_path}' does not contain any YAML files.")
    else:
        logger.error(f"Input path '{input_path}' is neither a file nor a directory.")
        raise ValueError(f"Input path '{input_path}' is neither a file nor a directory.")


def get_parser() -> argparse.ArgumentParser:
    """Creates and configures the argument parser.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    commands = ['schema', 'solve', 'validate', 'problem']

    argument_parser = argparse.ArgumentParser(description='Process some commands.')

    argument_parser.add_argument(
        '--input', type=Path, required=True,
        help='The input file or directory (as a Path).'
    )
    argument_parser.add_argument(
        '--output', type=Path, required=True,
        help='The output directory.'
    )
    argument_parser.add_argument(
        'commands', nargs='+', choices=commands,
        help='List of commands to run.'
    )

    return argument_parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    try:
        validate_args(args.input, args.output)
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        exit(1)
    logger.info("Starting processing...")
    process(args.commands, args.input, args.output)
    logger.info("Processing completed.")
