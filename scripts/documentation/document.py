import argparse
from pathlib import Path

from jinja2 import Template, Environment, FileSystemLoader

from src.tokens.cell_token import CellToken
from src.tokens.cycle_token import CycleToken
from src.tokens.digit_token import DigitToken
from src.tokens.known_token import KnownToken
from src.tokens.quadruple_token import QuadrupleToken
from src.tokens.side_token import SideToken
from src.tokens.symbols import CommaToken, DashToken, EqualsToken, QuestionMarkToken
from src.tokens.token import Token
from src.tokens.value_token import ValueToken
from src.utils.load_modules import load_modules

env: Environment = Environment(loader=FileSystemLoader(Path('scripts/documentation/templates')))


def directory_path(value):
    """Custom argparse type to validate a directory path."""
    path = Path(value)
    if not path.is_dir():
        raise argparse.ArgumentTypeError(f"The specified path '{value}' is not a valid directory.")
    return path


def get_parser():
    """Creates and returns an argument parser with subcommands.

    Returns:
        argparse.ArgumentParser: The argument parser configured with subcommands for 'parser', 'token', and 'constraint',
        and an 'output' directory argument.
    """
    parser = argparse.ArgumentParser(
        description='Process some input arguments using subcommands.'
    )

    subparsers = parser.add_subparsers(
        title='Commands',
        dest='command',  # The selected command will be stored here
        required=True,  # Enforce that a subcommand must be provided
        help='Available commands'
    )

    # Subcommand: parser
    parser_parser = subparsers.add_parser(
        'parser',
        help='Perform parsing operations.'
    )
    parser_parser.add_argument(
        '--output',
        type=directory_path,
        required=True,
        help='The output directory where results will be saved.'
    )

    # Subcommand: token
    parser_token = subparsers.add_parser(
        'token',
        help='Perform tokenization operations.'
    )
    parser_token.add_argument(
        '--output',
        type=directory_path,
        required=True,
        help='The output directory where results will be saved.'
    )

    # Subcommand: constraint
    parser_constraint = subparsers.add_parser(
        'constraint',
        help='Apply constraints.'
    )
    parser_constraint.add_argument(
        '--output',
        type=directory_path,
        required=True,
        help='The output directory where results will be saved.'
    )

    return parser


def document_parser(output: Path):
    load_modules('src.parsers')
    if not output.exists():
        output.makedir(parents=True)


def document_tokens(output: Path):
    tokens: List[Token] = [
        Token(),
        CellToken(),
        CycleToken(),
        DigitToken(),
        KnownToken(),
        QuadrupleToken(),
        SideToken(),
        EqualsToken(),
        CommaToken(),
        DashToken(),
        QuestionMarkToken(),
        ValueToken(),
    ]
    tokens_template: Template = env.get_template('tokens.md')
    output_path: Path = output / Path('tokens.md')
    tokens_template.stream(tokens=[token.to_dict() for token in tokens]).dump(str(output_path))


def document_constraints(output: Path):
    load_modules('src.items')
    if not output.exists():
        output.makedir(parents=True)


def main():
    """Main method to parse arguments."""
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
