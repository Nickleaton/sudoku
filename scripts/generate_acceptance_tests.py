from argparse import ArgumentParser
from pathlib import Path
from string import Template
from typing import List

RAW = """from tests.acceptance.acceptance_test import AcceptanceTest


class Test$classname(AcceptanceTest):

    def setUp(self) -> None:
        self.name = "$name"
"""


def get_filenames(directory: str) -> List[str]:
    path = Path(directory)
    pattern = path.glob('*.yaml')
    return [str(f) for f in pattern]


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
        default=Path('tests') / 'acceptance_tests'
    )
    return result


if __name__ == '__main__':
    parser = parser()
    args = parser.parse_args()
    template = Template(RAW)
    for filename in get_filenames(args.source):
        name = "test_" + Path(filename).name.replace(".yaml", "") + ".py"
        output_filename = Path(args.output) / name
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(template.substitute(classname=name.capitalize(), name=name))
