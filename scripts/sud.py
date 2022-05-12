"""Script to solve sudokus"""
import logging
import sys

from scripts.parser import parser
from src.commands.html import HTML

# def produce_jpg(config: str, filename: Optional[str]) -> None:
#     if filename is None:
#         return
#     logging.info(f"{'jpg':20} {config} {filename}")
#
#
# def produce_rst(config: str, filename: Optional[str]) -> None:
#     if filename is None:
#         return
#     logging.info(f"{'rst':20} {config} {filename}")
#
#
# def produce_verify(config: str, filename: Optional[str]) -> None:
#     if filename is None:
#         return
#     logging.info(f"{'verify':20} {config} {filename}")
#
#
# def produce_solve(config: str, filename: Optional[str]) -> None:
#     if filename is None:
#         return
#     logging.info(f"{'solve':20} {config} {filename}")
#
#
# def produce_solution(config: str, filename: Optional[str]) -> None:
#     if filename is None:
#         return
#     logging.info(f"{'solution':20} {config} {filename}")
#
#
# def produce_yaml(config: str, filename: Optional[str]) -> None:
#     if filename is None:
#         return
#     logging.info(f"{'yaml':20} {config} {filename}")


if __name__ == "__main__":
    argparser = parser()
    args = argparser.parse_args()
    if args.logfile:
        logging.basicConfig(filename=args.logfile, encoding='utf-8', level=args.loglevel)
    else:
        logging.basicConfig(encoding='utf-8', level=args.loglevel)
    command = None
    output = None
    if args.html is not None:
        command = HTML(args.config)
        output = args.html

    command.load_config()
    command.create_board()
    command.create_problem()
    command.process()
    command.write(output)
    sys.exit(0)
