"""Script to solve sudokus"""
import logging
import sys

from commands.solve_command import SolveCommand
from src.commands.html_command import HTMLCommand
from src.commands.img_command import ImageCommand

from postponed.parser import parser
from src.commands.svg_command import SVGCommand

# def produce_jpg(config: str, filename: Optional[str]) -> None:
#     if filename is None:
#         return
#     logging.info(f'{'jpg':20} {config} {filename}')
#
#
# def produce_rst(config: str, filename: Optional[str]) -> None:
#     if filename is None:
#         return
#     logging.info(f'{'rst':20} {config} {filename}')
#
#
# def produce_verify(config: str, filename: Optional[str]) -> None:
#     if filename is None:
#         return
#     logging.info(f'{'verify':20} {config} {filename}')
#
#
# def produce_solve(config: str, filename: Optional[str]) -> None:
#     if filename is None:
#         return
#     logging.info(f'{'solve':20} {config} {filename}')
#
#
# def produce_solution(config: str, filename: Optional[str]) -> None:
#     if filename is None:
#         return
#     logging.info(f'{'solution':20} {config} {filename}')
#
#
# def produce_yaml(config: str, filename: Optional[str]) -> None:
#     if filename is None:
#         return
#     logging.info(f'{'yaml':20} {config} {filename}')


if __name__ == '__main__':
    argument_parser = parser()
    args = argument_parser.parse_args()
    if args.logfile:
        logging.basicConfig(filename=args.logfile, encoding='utf-8', level=args.loglevel)
    else:
        logging.basicConfig(encoding='utf-8', level=args.loglevel)
    command = None
    output = None
    if args.solve is not None:
        command = SolveCommand(args.config, args.solve)
    if args.html is not None:
        command = HTMLCommand(args.config, args.html)
        output = args.html
    if args.svg is not None:
        command = SVGCommand(args.config, args.svg)
        output = args.svg
    if args.png is not None:
        command = ImageCommand(args.png, args.config)
    if args.jpg is not None:
        command = ImageCommand(args.jpg, args.config)
    command.execute()
    command.write()
    sys.exit(0)
