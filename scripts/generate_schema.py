"""Generate Schema."""
import argparse
import logging
import logging.config
import shutil
import subprocess  # noqa: S404
from pathlib import Path

from strictyaml import Map, Optional, Seq, Validator  # noqa: WPS458

from src.board.board import Board
from src.items.item import Item
from src.parsers.parser import Parser
from src.parsers.solution_parser import SolutionParser
from src.utils.config import Config
from src.utils.load_modules import load_modules
from src.utils.names import Name

config: Config = Config()
logging.config.dictConfig(config.logging)
logger = logging.getLogger('generate_schema')


def create_config_schema() -> Map:
    """Create the config schema mapping.

    A schema is generated for the configuration based on the `Item` classes,
    including constraints, the board schema, and an optional solution arg_parser.

    Returns:
        Map: The generated configuration schema.
    """
    constraints: dict[Optional, Validator | Optional] = {}
    for class_name, constraint in Item.classes.items():
        if class_name == 'Solution':
            continue
        constraints[Optional(class_name)] = constraint.schema()

    return Map(
        {
            'Board': Board.schema(),
            'Constraints': Map(constraints),
            Optional('Solution'): Seq(SolutionParser()),
        },
    )


def write_config_schema(file_path: str, schema: Map, import_names: set[str]) -> None:
    """Write the generated configuration schema to a Python file.

    Args:
        file_path (str): The path where the generated schema is saved.
        schema (Map): The configuration schema to be written to the file.
        import_names (set[str]): The set of import names included in the file.
    """
    with open(file_path, 'w', encoding='utf-8') as schema_file:
        schema_file.write('"""ConfigSchema. Autogenerated."""\n')
        schema_file.write('from strictyaml import Map, Optional, Seq, Str\n\n')

        # Write the import statements
        for name in sorted(import_names):
            schema_file.write(f'from src.parsers.{Name.camel_to_snake(name)} import {name}\n')

        # Convert the schema to string and write it
        map_string: str = repr(schema).replace('"', "'")
        schema_file.write(f'problem_schema = {map_string}\n')


def format_python_file(file_path: str) -> None:
    """Format the specified Python file using `black`.

    `Black` is used to format the specified file according to PEP 8 standards.

    Note:
        Requires `black` to be installed and available in the environment.

    Args:
        file_path (str): The path to the Python file to be formatted.

    Raises:
        ValueError: If the file path is invalid.
        FileNotFoundError: If `black` is not found.
    """
    schema_file: Path = Path(file_path)
    if not schema_file.is_file():
        raise ValueError(f'The file does not exist: {file_path}')
    black_path: str | None = shutil.which('black')
    if black_path is None:
        raise FileNotFoundError('The "black" executable was not found in the PATH.')
    try:  # noqa: WPS229
        black_output: subprocess.CompletedProcess = subprocess.run(  # noqa: S404, S603
            [black_path, str(schema_file.resolve())],
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8',
        )
        logging.info(black_output.stdout)  # Display `black`'s output
    except subprocess.CalledProcessError as exp:
        logging.error(f'Error formatting the file: {exp.stderr}')


def replace_quotes_in_file(file_path: str) -> None:
    """Replace double quotes with single quotes in a Python file.

    All double quotes in the file are replaced with single quotes, and triple-quoted
    strings are adjusted to maintain valid syntax.

    Args:
        file_path (str): The path to the Python file to modify.
    """
    with open(file_path, 'r', encoding='utf-8') as input_file:
        python_code: str = input_file.read()
    python_code = python_code.replace('"', "'")
    python_code = python_code.replace("'''", '"""')
    with open(file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(python_code)


def create_arg_parser() -> argparse.ArgumentParser:
    """Create an argument arg_parser for command-line arguments.

    Returns:
        argparse.ArgumentParser: The argument arg_parser instance.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Generate config schema file.')
    parser.add_argument(
        'output',
        type=str,
        help='The output path for the generated config schema file',
    )
    return parser


def get_import_names() -> set[str]:
    """Retrieve a set of import names based on `Item` classes.

    All `Item` classes are processed, excluding the `Solution` class, and the
    names of their associated parser classes are added to the set of import names.
    The set also includes the name 'SolutionParser'.

    Returns:
        set[str]: A set of import names derived from the `Item` class parsers.
    """
    import_names: set[str] = {'SolutionParser'}
    for class_name, constraint in Item.classes.items():
        if class_name == 'Solution':
            continue
        parser: Parser = constraint.parser()
        import_names.add(parser.__class__.__name__)
    return import_names


if __name__ == '__main__':
    logging.info('Generating config schema...')
    arg_parser: argparse.ArgumentParser = create_arg_parser()
    args: argparse.Namespace = arg_parser.parse_args()
    load_modules('src.items')
    mapping: Map = create_config_schema()
    names: set[str] = get_import_names()
    write_config_schema(args.output, mapping, names)
    format_python_file(args.output)
    replace_quotes_in_file(args.output)
    logging.info('Config schema generation completed.')
