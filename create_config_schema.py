import subprocess

import strictyaml
from strictyaml import Map, Seq, Optional, Str, Float, Int

from src.items.board import Board
from src.items.item import Item
from src.parsers.solution_parser import SolutionParser
from src.utils.names import Name

config_schema = Map(
    {
        'statistic_database': Str(),
        'statistic_elements': Map({Str(): Str()}),
        'drawing': Map(
            {
                'size': Str(),
                'cell_size': Int(),
                'killer_offset': Int(),
                'arrow_head_percentage': Float(),
                'thermo_head_percentage': Float(),
                'odd_cell_radius': Int(),
                'kropki_radius': Int(),
                'consecutive_radius': Int(),
                'even_cell_size': Int()
            }
        )
    }
)

with open('src/parsers/config_schema.py', 'w') as f:
    import_names = {'SolutionParser'}
    constraints = {}
    for key, value in Item.classes.items():
        if key == 'Solution':
            continue
        constraints[strictyaml.Optional(key)] = value.schema()
        parser = value.parser()
        import_names.add(value.parser().__class__.__name__)
    mapping = Map(
        {
            'Board': Board.schema(),
            'Constraints': Map(constraints),
            Optional('Solution'): Seq(SolutionParser())
        }
    )
    f.write(r'"""ConfigSchema. Autogenerated."""\n')
    f.write("from strictyaml import Map, Seq, Optional, Str\n\n")
    for name in sorted(import_names):
        f.write(f"from src.parsers.{Name.camel_to_snake(name)} import {name}\n")
    f.write(f"problem_schema = {mapping!r}")
    f.close()
    subprocess.run(["black", "src/parsers/config_schema.py"])