"""Process for the solve command."""
import itertools
from pathlib import Path

from solve import logger
from src.commands.command import Command  # noqa: I001, I003
from src.commands.extract_answer_command import ExtractAnswerCommand  # noqa: I001
from src.commands.file_writer_command import LPFileWriterCommand  # noqa: I001, I003, I005
from src.commands.file_writer_command import RuleWriterCommand  # noqa: I005
from src.commands.file_writer_command import SVGProblemWriterCommand  # noqa: I001
from src.commands.problem import Problem  # noqa: I005
from src.commands.validate_config_command import ValidateConfigCommand


def process_schema(problem: Problem) -> None:
    """Process the schema command for the given problem.

    Args:
        problem (Problem): The problem instance to process.

    Raises:
        ValueError: If the schema validation fails.
    """
    logger.info(f'Processing schema for file: {problem.problem_file_name}')
    command: Command = ValidateConfigCommand()
    command.execute(problem=problem)
    if problem.validation != 'OK':
        raise ValueError(problem.validation)
    logger.info(f'Schema validation OK for file: {problem.problem_file_name}')


def process_solve(problem: Problem) -> None:
    """Process the solve command for the given problem.

    Args:
        problem (Problem): The problem instance to process.
    """
    command: Command = ExtractAnswerCommand()
    command.execute(problem=problem)


def process_validate(problem: Problem) -> None:
    """Process the validate command for the given problem.

    Args:
        problem (Problem): The problem instance to process.
    """
    logger.info(f'Processing validate for file: {problem.problem_file_name} with output: {problem.output_directory}')


def process_problem(problem: Problem) -> None:
    """Process the problem command for the given problem.

    Args:
        problem (Problem): The problem instance to process.
    """
    command: Command = SVGProblemWriterCommand()
    command.execute(problem=problem)


def process_lp(problem: Problem) -> None:
    """Produce the LP file for the given problem.

    Args:
        problem (Problem): The problem instance to process.
    """
    command = LPFileWriterCommand()
    command.execute(problem=problem)


def process_rules(problem: Problem) -> None:
    """Produce the rule file for the given problem.

    Args:
        problem (Problem): The problem instance to process.

    Logs:
        Logs the start and completion of rule processing.
    """
    logger.info(f'Processing rules for file: {problem.problem_file_name} with output: {problem.output_directory}')
    command = RuleWriterCommand()
    command.execute(problem=problem)
    logger.info(f'Processing rules complete for file: {problem.problem_file_name}')


def process_command(command: str, input_file: Path, output_path: Path) -> None:
    """Dispatch the command to the appropriate handler.

    Args:
        command (str): The command to process.
        input_file (Path): The input file path.
        output_path (Path): The output directory path.

    Logs:
        Logs error if the command is unknown.
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
        case 'lp':
            process_lp(problem)
        case 'rules':
            process_rules(problem)
        case _:
            logger.error(f'Unknown command: {command}')


def get_yaml_files(files_path: Path) -> list[Path]:
    """
    Retrieve a sorted list of YAML files from the given path.

    If the given `files_path` is a file, it returns a list containing that file.
    If the given `files_path` is a directory, it returns a list of all `.yaml` files in the directory, sorted.

    Args:
        files_path (Path): The path to a file or directory.

    Returns:
        list[Path]: A sorted list of `Path` objects representing YAML files.
    """
    files: list[Path] = [files_path] if files_path.is_file() else list(files_path.glob('*.yaml'))
    files.sort()  # Sort files alphabetically
    return files


def process(commands: list[str], files_path: Path, output_path: Path) -> None:
    """Process all combinations of commands and files.

    Args:
        commands (list[str]): List of commands to process.
        files_path (Path): Input file or directory path.
        output_path (Path): The output directory path.

    Logs:
        Logs creation of output directories if necessary.
    """
    files: list[Path] = get_yaml_files(files_path)
    for file_name, command in itertools.product(files, commands):
        file_stem: Path = Path(file_name.name.removesuffix('.yaml'))
        specific_output_path: Path = output_path / file_stem
        if not specific_output_path.exists():
            logger.info(f'Creating output directory: {specific_output_path}')
            specific_output_path.mkdir(parents=True)
        process_command(command, file_name, specific_output_path)
