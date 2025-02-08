"""Sudoku Script."""
import logging
import sys

from solve_parser import get_parser, validate_args
from solve_process import process
from src.utils.config import Config
from src.utils.load_modules import load_modules

config: Config = Config()
logging.config.dictConfig(config.logging)
logger = logging.getLogger('solve')

if __name__ == '__main__':
    load_modules('src', 'items')
    parser = get_parser()
    args = parser.parse_args()
    try:
        validate_args(args.input, args.output)
    except ValueError as exp:
        logger.error(f'Validation error: {exp}')
        sys.exit(1)
    logger.info('Starting processing...')
    process(args.commands, args.input, args.output)
    logger.info('Processing completed.')
