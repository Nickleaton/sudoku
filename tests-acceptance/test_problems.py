import glob
import os
import shutil
import unittest
import xml.dom.minidom
from typing import Dict, List, Any

import oyaml as yaml
from jinja2 import Environment, select_autoescape, FileSystemLoader
from parameterized import parameterized
from svgwrite import Drawing

from src.items.board import Board
from src.items.item import Item
from src.items.solution import Solution
from src.solvers.pulp_solver import PulpSolver

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

    filenames = ['problem065']

    @staticmethod
    def config(filename: str) -> Any:
        full_filename = os.path.join("problems", filename + ".yaml")
        with open(full_filename, 'r') as f:
            config = yaml.load(f, yaml.SafeLoader)
        return config

    @staticmethod
    def board(config: Dict) -> Board:
        return Board.create('Board', config)

    @staticmethod
    def problem(filename: str) -> Item:
        config = TestFiles.config(filename)
        board = TestFiles.board(config)
        return Item.create(board, {'Constraints': config['Constraints']})

    @staticmethod
    def svg(problem: Item) -> str:
        glyph = problem.sorted_glyphs
        canvas = Drawing(filename="test.svg", size=("35cm", "35cm"))
        for clz in glyph.used_classes:
            if (element := clz.start_marker()) is not None:
                canvas.defs.add(element)
            if (element := clz.end_marker()) is not None:
                canvas.defs.add(element)
            if (element := clz.symbol()) is not None:
                canvas.add(element)
        canvas.add(glyph.draw())
        canvas.add_stylesheet(href="glyph.css", title="glyphs")
        elements = xml.dom.minidom.parseString(canvas.tostring())
        return str(elements.toprettyxml())

    @staticmethod
    def html(problem: Item) -> str:
        template = env.get_template("problem.html")
        rules = [{'name': rule.name, 'text': rule.text} for rule in problem.sorted_unique_rules]
        svg = TestFiles.svg(problem)
        result = template.render(rules=rules, problem_svg=svg, meta=problem.board.to_dict()['Board'])
        return result

    @parameterized.expand(filenames, name_func=custom_name_func)
    def test_svg(self, filename: str) -> None:
        problem = TestFiles.problem(filename)
        svg = TestFiles.svg(problem)
        directory = os.path.join("output", "svg")
        if not os.path.exists(directory):
            os.makedirs(directory)
        full_filename = os.path.join(directory, filename + ".svg")
        with open(full_filename, 'w', encoding="utf-8") as f:
            f.write(svg)

    @parameterized.expand(filenames, name_func=custom_name_func)
    def test_html(self, filename: str) -> None:
        problem = TestFiles.problem(filename)
        full_filename = os.path.join("output", "html", filename + ".html")
        with open(full_filename, 'w', encoding="utf-8") as f:
            f.write(TestFiles.html(problem))

    @parameterized.expand(filenames, name_func=custom_name_func)
    def xtest_solution(self, filename: str) -> None:
        config = TestFiles.config(filename)
        self.assertIn('Solution', config)
        problem = TestFiles.problem(filename)
        expected = Solution.create(problem.board, config['Solution'])
        self.assertIsNotNone(expected)

    @parameterized.expand(filenames, name_func=custom_name_func)
    def test_solve(self, filename: str) -> None:
        config = TestFiles.config(filename)
        problem = TestFiles.problem(filename)
        solver = PulpSolver(problem.board, 'PULP_CBC_CMD')
        problem.add_variables(problem.board, solver)
        problem.add_constraint(solver)
        directory = os.path.join("output", "lp")
        if not os.path.exists(directory):
            os.makedirs(directory)
        solver.save(os.path.join(directory, filename + ".lp"))
        solver.solve()
        print(str(solver.solution))
        expected = Solution.create(problem.board, config['Solution'])
        self.assertEqual(expected, solver.solution)

    def test_css(self):
        directory = os.path.join("output", "html")
        if not os.path.exists(directory):
            os.makedirs(directory)
        shutil.copy(os.path.join("src", "html", "glyph.css"), directory)


class TestIndex(unittest.TestCase):

    def setUp(self):
        self.filenames = [(os.path.basename(filename)[:-5]) for filename in
                          glob.glob((os.path.join('problems', '*.yaml')))]

    @staticmethod
    def tags(filename: str) -> List[str]:
        config = TestFiles.config(filename)
        board = TestFiles.board(config)
        return sorted(list(Item.create(board, {'Constraints': config['Constraints']}).tags))

    def test_index(self):
        template = env.get_template("index.html")
        data = {}
        for filename in self.filenames:
            data[filename] = " ".join(self.tags(filename))
        result = template.render(data=data)

        with open(os.path.join("output", 'html', 'index.html'), 'w', encoding="utf-8") as f:
            f.write(result)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
