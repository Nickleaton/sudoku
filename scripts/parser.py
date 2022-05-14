import pathlib
from argparse import ArgumentParser


def parser() -> ArgumentParser:
    """Create the argument parser."""
    result = ArgumentParser(description="Solve Sudoku Variants.")
    result.add_argument(
        "--loglevel",
        nargs='?',
        dest="loglevel",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help="Set the logging level",
        default='INFO',
        required=False
    )
    result.add_argument(
        "--logfile",
        nargs='?',
        const="",
        default=None,
        dest="logfile",
        help="Where to write the log file",
        required=False
    )

    result.add_argument(
        '--html',
        nargs='?',
        const="",
        default=None,
        help='Produce html output',
        type=str,
        required=False
    )
    result.add_argument(
        '--svg',
        nargs='?',
        const="",
        default=None,
        help='Produce svg output',
        type=str,
        required=False
    )
    result.add_argument(
        '--jpg',
        nargs='?',
        const="",
        default=None,
        help='Produce jpg output',
        type=str,
        required=False
    )
    result.add_argument(
        '--png',
        nargs='?',
        const="",
        default=None,
        help='Produce png output',
        type=str,
        required=False
    )
    result.add_argument(
        '--rst',
        nargs='?',
        const="",
        default=None,
        help='Produce rst output',
        type=str,
        required=False
    )
    result.add_argument(
        '--verify',
        nargs='?',
        const="",
        default=None,
        help='Verify solution satisfies the problem',
        type=str,
        required=False
    )
    result.add_argument(
        '--yaml',
        nargs='?',
        const="",
        default=None,
        help='Dump problem as yaml',
        type=str,
        required=False
    )
    result.add_argument(
        '--solve',
        nargs='?',
        const="",
        default=None,
        help='Solve the problem',
        type=str,
        required=False
    )
    result.add_argument(
        '--solution',
        nargs='?',
        const="",
        default=None,
        help='Out the solution as text',
        type=str,
        required=False
    )
    result.add_argument(
        '--config',
        help='YAML configuration file containing the problem.',
        type=pathlib.Path,
        required=True
    )
    return result
