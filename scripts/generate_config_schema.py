import argparse
import subprocess
import sys

import strictyaml
from strictyaml import Map, Seq, Optional

from src.board.board import Board
from src.items.item import Item
from src.parsers.solution_parser import SolutionParser
from src.utils.load_modules import load_modules
from src.utils.names import Name


def create_config_schema() -> Map:
    """Creates the config schema mapping.

    Generates a schema for the configuration based on the `Item` classes, including
    constraints, board schema, and an optional solution parser.

    Returns:
        Map: The generated config schema.
    """
    constraints: dict = {}
    for key, value in Item.classes.items():
        if key == 'Solution':
            continue
        constraints[strictyaml.Optional(key)] = value.schema()

    return Map(
        {
            'Board': Board.schema(),
            'Constraints': Map(constraints),
            Optional('Solution'): Seq(SolutionParser())
        }
    )


def write_config_schema(file_path: str, mapping: Map, import_names: set[str]) -> None:
    """Writes the generated config schema to a Python file.

    Args:
        file_path (str): The file path where the generated schema will be saved.
        mapping (Map): The config schema to be written to the file.
        import_names (set[str]): The set of import names to be included in the file.
    """
    with open(file_path, 'w') as f:
        f.write('"""ConfigSchema. Autogenerated."""\n')
        f.write("from strictyaml import Map, Optional, Seq, Str\n\n")

        # Write the import statements
        for name in sorted(import_names):
            f.write(f"from src.parsers.{Name.camel_to_snake(name)} import {name}\n")

        # Convert the schema to string and write it
        map_string = repr(mapping).replace('"', "'")
        f.write(f"problem_schema = {map_string}\n")


def format_python_file(file_path: str) -> None:
    """Formats the specified Python file using `black`.

    Runs `black` on the provided file to format it according to PEP 8 standards.

    Args:
        file_path (str): The path to the Python file to be formatted.
    """
    subprocess.run(
        ['black', file_path],
        capture_output=True,  # Captures both stdout and stderr
        text=False  # Decodes output as text (not bytes)
    )


def replace_quotes_in_file(file_path: str) -> None:
    """Replaces double quotes (") with single quotes (') in a Python file.

    Reads the specified file, replaces all double quotes with single quotes, and
    writes the result back to the file. Adjusts triple-quote strings to maintain
    proper syntax.

    Args:
        file_path (str): The path to the Python file to modify.
    """
    with open(file_path, 'r') as file:
        content = file.read()

    # Replace double quotes with single quotes
    content = content.replace('"', "'")

    # Replace single-quote triple quotes back to double-quote triple quotes
    content = content.replace("'''", '"""')

    with open(file_path, 'w') as file:
        file.write(content)


def create_arg_parser() -> argparse.ArgumentParser:
    """Creates an argument parser for command-line arguments.

    Returns:
        argparse.ArgumentParser: The argument parser instance.
    """
    parser = argparse.ArgumentParser(description='Generate config schema file.')
    parser.add_argument(
        'output',
        type=str,
        help='The output path for the generated config schema file'
    )
    return parser


def get_import_names() -> set[str]:
    """Retrieves a set of import names based on `Item` classes.

    Processes all `Item` classes, excluding the `Solution` class, and adds the
    name of their associated parser class to the set of import names. The set
    also includes the name 'SolutionParser'.

    Returns:
        set[str]: A set of import names derived from the `Item` class parsers.
    """
    import_names: set[str] = {'SolutionParser'}

    # Process all Item classes except for 'Solution'
    for key, value in Item.classes.items():
        if key == 'Solution':
            continue
        parser = value.parser()
        import_names.add(parser.__class__.__name__)

    return import_names


def main() -> None:
    """Main function to generate the config schema and format the file.

    Parses the command-line arguments, generates the config schema, writes it
    to a specified file, and then formats the file using `black`.
    """
    parser = create_arg_parser()
    args = parser.parse_args()

    # Ensure all item classes are loaded and registered
    load_modules('src.items')

    # Generate the schema
    mapping = create_config_schema()

    # Get the names of classes to import
    import_names = get_import_names()

    # Output the schema
    write_config_schema(args.output, mapping, import_names)

    # Format the file using black
    format_python_file(args.output)

    # Replace double quotes with single quotes for flake8 compliance
    replace_quotes_in_file(args.output)

    sys.exit(0)


if __name__ == '__main__':
    main()
