"""Document constraints, tokens, and parsers to structured files."""

import logging
from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, Template

from src.tokens.token import Token
from src.utils.config import Config
from src.utils.load_modules import load_modules

config: Config = Config()
logging.config.dictConfig(config.logging)
logger = logging.getLogger('document')
env: Environment = Environment(loader=FileSystemLoader(Path('scripts/documentation/templates')), autoescape=True)


def directory_path(path_name: str) -> Path:
    """Validate that the specified path is a directory.

    Args:
        path_name (str): The directory path to validate.

    Returns:
        Path: A `Path` object if the path is valid.

    Raises:
        ArgumentTypeError: If the path does not exist or is not a directory.
    """
    path: Path = Path(path_name)
    if not path.is_dir():
        raise ArgumentTypeError(f'The specified path {path_name!r} is not a valid directory.')
    return path


def get_parser() -> ArgumentParser:
    """Create an argument parser with subcommands for documentation.

    Returns:
        ArgumentParser: An argument parser with subcommands 'parser', 'token', and 'constraint',
        each requiring an 'output' directory.
    """
    parser: ArgumentParser = ArgumentParser(
        description='Generate documentation for constraints, tokens, and parsers.',
    )

    subparsers = parser.add_subparsers(
        title='Commands',
        dest='command',
        required=True,
        help='Available commands',
    )
    parser_parser = subparsers.add_parser(
        'parser',
        help='Generate documentation for parsers.',
    )
    parser_parser.add_argument(
        '--output',
        type=directory_path,
        required=True,
        help='The output directory for saving the documentation.',
    )
    parser_token = subparsers.add_parser(
        'token',
        help='Generate documentation for tokens.',
    )
    parser_token.add_argument(
        '--output',
        type=directory_path,
        required=True,
        help='The output directory for saving the documentation.',
    )
    parser_constraint = subparsers.add_parser(
        'constraint',
        help='Generate documentation for constraints.',
    )
    parser_constraint.add_argument(
        '--output',
        type=directory_path,
        required=True,
        help='The output directory for saving the documentation.',
    )
    return parser


def document_parser(output: Path) -> None:
    """Generate and save documentation for parsers.

    Args:
        output (Path): The directory where parser documentation will be saved.
    """
    load_modules('src.parsers')
    if not output.exists():
        output.makedir(parents=True)


def document_tokens(output: Path) -> None:
    """Generate and save documentation for tokens.

    Args:
        output (Path): The directory where token documentation will be saved.
    """
    tokens: list[Token] = Token.token_list()
    tokens_template: Template = env.get_template('tokens.md')
    output_path: Path = output / Path('tokens.md')
    tokens_template.stream(tokens=[token.to_dict() for token in tokens]).dump(str(output_path))


def document_constraints(output: Path) -> None:
    """Generate and save documentation for constraints.

    Args:
        output (Path): The directory where constraint documentation will be saved.
    """
    load_modules('src.items')
    if not output.exists():
        output.makedir(parents=True)


def main() -> None:
    """Parse command-line arguments and execute the appropriate command."""
    parser = get_parser()
    args = parser.parse_args()
    match args.command:
        case 'parser':
            document_parser(args.output)
        case 'token':
            document_tokens(args.output)
        case 'constraint':
            document_constraints(args.output)


if __name__ == '__main__':
    main()
