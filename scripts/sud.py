"""Script to solve sudokus"""
import glob
import logging
import os
import sys
from argparse import ArgumentParser, Namespace
from typing import Optional, List


def create_parser() -> ArgumentParser:
    """Create the argument parser."""
    parser = ArgumentParser(description="Solve Sudoku Variants.")
    parser.add_argument(
        dest='command',
        help='Command',
        choices=['validate', 'solve'],
    )
    parser.add_argument(
        "-l",
        "--log",
        dest="loglevel",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help="Set the logging level",
        default='INFO',
        required=False
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-c',
        '--config',
        help='YAML configuration file containing the problem.',
        type=str,
        required=False
    )
    group.add_argument(
        '-d',
        '--directory',
        help='YAML configuration directory containing the problems.',
        type=str,
        required=False
    )
    return parser


def validate_command(args: Namespace) -> Optional[str]:
    """
    Validate arguments
    :param args: results from argparser
    :return: string containing error or None
    """
    if args.config:
        if not os.path.exists(args.config):
            return f"Config file {args.config} doesn't exist"
        if not os.path.isfile(args.config):
            return f"Config file {args.config} not a file"
    if args.directory:
        if not os.path.exists(args.directory):
            return f"Directory {args.directory} doesn't exist"
        if not os.path.isdir(args.directory):
            return f"Config file {args.directory} not a directory"
    return None


def extract_files(args: Namespace) -> List[str]:
    """
    Get all the file names to process.

    :param args: Namespace of parsed argument
    :return: List of filenames
    """
    files = []
    if args.config:
        files.append(args.config)
    if args.directory:
        files.extend(glob.glob(os.path.join(args.directory, '*.yaml')))
    return files


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)
    result = validate_command(args)
    if result:
        print(result)
        sys.exit(1)
    files = extract_files(args)
    for file in files:
        logging.info(f"{args.command} {file}")

    sys.exit(0)
