import glob
import os
import unittest

from jinja2 import Environment, select_autoescape, FileSystemLoader
from parameterized import parameterized

from src.commands.lp import LP
from src.commands.svg import SVG
from src.commands.solve import Solve
from src.items.solution import Solution

env = Environment(
    loader=FileSystemLoader(os.path.join('src', 'html')),
    autoescape=select_autoescape()
)


def custom_name_func(testcase_func, _, param) -> str:
    return "%s_%s" % (
        testcase_func.__name__,
        parameterized.to_safe_name("_".join(str(x) for x in param.args)),
    )


class TestFiles(unittest.TestCase):
    filenames = sorted(
        [
            (os.path.basename(filename)[:-5]) for filename in glob.glob((os.path.join('problems', '*.yaml')))
        ]
    )

    # filenames = ['problem068']

    @parameterized.expand(filenames, name_func=custom_name_func)
    def test_svg(self, filename: str) -> None:
        command = SVG(os.path.join("problems", filename + ".yaml"), os.path.join("output", "svg", filename + ".svg"))
        command.process()
        self.assertIsNotNone(command.output)
        command.write()

    @parameterized.expand(filenames, name_func=custom_name_func)
    def test_html(self, filename: str) -> None:
        command = SVG(os.path.join("problems", filename + ".yaml"), os.path.join("output", "html", filename + ".html"))
        command.process()
        self.assertIsNotNone(command.output)
        command.write()

    @parameterized.expand(filenames, name_func=custom_name_func)
    def test_lp(self, filename: str) -> None:
        command = LP(os.path.join("problems", filename + ".yaml"), os.path.join("output", "lp", filename + ".lp"))
        command.process()
        command.write()

    @parameterized.expand(filenames, name_func=custom_name_func)
    def test_verify(self, filename: str) -> None:
        command = Solve(os.path.join("problems", filename + ".yaml"),
                        os.path.join("output", "verify", filename + ".txt"))
        command.process()
        command.write()
        expected = Solution.create(command.board, command.config['Solution'])
        self.assertEqual(expected, command.solution)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
