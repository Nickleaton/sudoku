"""
Script to solve sudokus
"""

from argparse import ArgumentParser


def parser() -> ArgumentParser:
    parser = ArgumentParser(description='Solve sudokus v0.01')
    parser.add_argument(
        '--version',
        help='version',
        action='store_true',
        default=False
    )
    parser.add_argument(
        '--html',
        help='html directory',
        action='store',
        dest='html',
        default='output/html'
    )
    parser.add_argument(
        '--svg',
        help='svg directory',
        action='store',
        dest='svg',
        default='output/svg'
    )
    parser.add_argument(
        '--lp',
        help='lp directory',
        action='store',
        dest='lp',
        default='output/lp'
    )
    parser.add_argument(
        '--problem',
        help='yaml file(s) containing the problem',
        dest='problems',
        action='append',
        nargs='+'
    )
    return parser


if __name__ == '__main__':
    parser = parser()
    args = parser.parse_args()
    print(args.problems)
