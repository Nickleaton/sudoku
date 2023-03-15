import glob
import os
from argparse import ArgumentParser
from string import Template
from typing import List

RAW = """from tests.acceptance.acceptance_test import AcceptanceTest


class Test$classname(AcceptanceTest):

    def setUp(self) -> None:
        self.name = "$name"
"""


def get_filenames(directory: str) -> List[str]:
    pattern = os.path.join(directory, '*.yaml')
    return glob.glob(pattern)


def parser() -> ArgumentParser:
    result = ArgumentParser(description='Generate acceptance tests')
    result.add_argument(
        '--source',
        help='directory containing yamls',
        action='store',
        dest='source',
        default='problems'
    )
    result.add_argument(
        '--output',
        help='output directory',
        action='store',
        dest='output',
        default=os.path.join('tests', 'acceptance_tests')
    )
    return result


if __name__ == '__main__':
    parser = parser()
    args = parser.parse_args()
    template = Template(RAW)
    for filename in get_filenames(args.source):
        name = os.path.basename(filename)[:-5]
        output_filename = os.path.join(args.output, "test_" + name + ".py")
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(template.substitute(classname=name.capitalize(), name=name))
