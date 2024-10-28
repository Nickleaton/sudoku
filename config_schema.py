import strictyaml
from strictyaml import Map, Seq, Optional, Str, Float, Int

from src.items.board import Board
from src.items.item import Item
from src.parsers.cell_list_parser import CellListParser
from src.parsers.cell_pairs_parser import CellPairsParser
from src.parsers.cell_parser import CellParser
from src.parsers.cell_value_parser import CellValueParser
from src.parsers.digit_parser import DigitParser
from src.parsers.digits_parser import DigitsParser
from src.parsers.known_parser import KnownParser
from src.parsers.little_killers_parser import LittleKillersParser
from src.parsers.none_parser import NoneParser
from src.parsers.outside_arrow_value_parser import OutsideArrowValueParser
from src.parsers.quadruples_parser import QuadruplesParser
from src.parsers.rossini_parser import RossiniParser
from src.parsers.solution_parser import SolutionParser
from src.parsers.vertex_digit_parser import VertexDigitParser
from src.parsers.vertex_value_parser import VertexValueParser
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

# CellListParser = Regex(r'\s*\d{2}\s*(,\s*\d{2}\s*)*')  # Done
# DigitParsersParser = Regex(r'\s*\d\s*(,\s*\d\s*)*')  # Done
# Knowns = Regex(r'[0-9.flmheo]+')  # Done
# CellPairsParser = Regex(r'\d\d\-\d\d')  # Done
# LittleKillersParser = Regex(r'[TLBR]\d[C|A]=\d+')  # Done
# DigitParser = Regex(r"\d")  # Done
# CellParser = Regex(r"\d\d")  # Done
# 
# QuadruplesParser = Regex(r'\d\d=[\d\?]+')  # Done
# 
# Rossini = Regex(r'[TLBR]\d=[DIU]')  # Done
# OutsideArrowValueParser = Regex(r'[TLBR]\d=\d+')  # Done
# CellValueParser = Regex(r'\d\d=\d+')
# VertexDigitParser = Regex(r'\d\d=\d')
# VertexValue = Regex(r'\d\d=\d+')


problem_schema = Map(
    {
        "Board": Board.schema(),
        "Constraints": Map(
            {
                Optional("AntiBLTR"): NoneParser(),
                Optional("AntiKing"): NoneParser(),
                Optional("AntiKnight"): NoneParser(),
                Optional("AntiQueens"): DigitsParser,
                Optional("AntiRossini"): NoneParser(),
                Optional("AntiTLBR"): NoneParser(),
                Optional("Asterix"): NoneParser(),
                Optional("BLTR"): NoneParser(),
                Optional("Battenburg"): CellListParser(),
                Optional("Between"): Seq(CellListParser()),
                Optional("Boxes"): NoneParser(),
                Optional("CenterProduct"): Seq(VertexValueParser()),
                Optional("ColumnIndexer"): DigitsParser(),
                Optional("Columns"): NoneParser(),
                Optional("ConsecutivePair"): Seq(CellPairsParser),
                Optional("DisjointGroup"): NoneParser(),
                Optional("DutchWhisperLine"): Seq(CellListParser()),
                Optional("EntropicLine"): Seq(CellListParser()),
                Optional("EqualSumLine"): Seq(CellListParser()),
                Optional("EvenCellParser"): Seq(CellParser()),
                Optional("Exclusion"): Seq(VertexDigitParser()),
                Optional("FixedDifferencePair"): Seq(CellPairsParser()),
                Optional("FixedProductPair"): Seq(CellPairsParser()),
                Optional("FixedRatioPair"): Seq(CellPairsParser()),
                Optional("FixedSumPair"): Seq(CellPairsParser()),
                Optional("Frame"): Seq(OutsideArrowValueParser()),
                Optional("FrameProduct"): Seq(OutsideArrowValueParser()),
                Optional("FrozenThermometer"): Seq(CellListParser()),
                Optional("GermanWhisperLine"): Seq(CellListParser()),
                Optional("Girandola"): NoneParser(),
                Optional("Knight"): Seq(DigitParser()),
                Optional("Known"): Seq(KnownParser()),
                Optional("KropkiPair"): Seq(CellPairsParser()),
                Optional("LittleKiller"): Seq(LittleKillersParser()),
                Optional("MOTE"): Seq(CellListParser()),
                Optional("MagicSquare"): Seq(CellParser()),
                Optional("MaxArrowLine"): Seq(CellListParser()),
                Optional("MinMaxDifference"): Seq(OutsideArrowValueParser()),
                Optional("MinMaxSum"): Seq(OutsideArrowValueParser()),
                Optional("MountainLine"): Seq(CellListParser()),
                Optional("NegativeBattenburg"): NoneParser(),
                Optional("NumberedRoom"): Seq(OutsideArrowValueParser()),
                Optional("OddCellParser"): Seq(CellParser()),
                Optional("OrthogonalProduct"): Seq(CellValueParser()),
                Optional("OrthogonallyAdjacent"): NoneParser(),
                Optional("Outside"): Seq(OutsideArrowValueParser()),
                Optional("Palindrome"): Seq(CellListParser()),
                Optional("Quadro"): NoneParser(),
                Optional("Quadruple"): Seq(QuadruplesParser()),
                Optional("RenbanLine"): Seq(CellListParser()),
                Optional("Rossini"): Seq(RossiniParser()),
                Optional("Rows"): NoneParser(),
                Optional("Sandwich"): Seq(OutsideArrowValueParser()),
                Optional("SequenceLine"): Seq(CellListParser()),
                Optional("SimpleThermometer"): Seq(CellListParser()),
                Optional("SumArrowLine"): Seq(CellListParser()),
                Optional("SumArrowLine"): Seq(CellListParser()),
                Optional("TLBR"): NoneParser(),
                Optional("TLBRReflecting"): NoneParser(),
                Optional("VPair"): Seq(CellPairsParser()),
                Optional("Window"): Seq(CellParser()),
                Optional("XPair"): Seq(CellPairsParser()),
            },
        ),
        Optional("Solution"): Seq(SolutionParser()),
    }
)

with open('generated_config_schema.py', 'w') as f:
    f.write("from strictyaml import Map, Seq, Optional, Str, Float, Int, Regex, NoneParser, Str, Regex\n\n")
    f.write(repr(problem_schema))

with open('generated_config_schema2.py', 'w') as f:
    import_names = set({})
    constraints = {}
    for key, value in Item.classes.items():
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
    f.write("from strictyaml import Map, Seq, Optional, Str, Regex\n\n")
    for name in sorted(import_names):
        f.write(f"from src.parsers.{Name.camel_to_snake(name)} import {name}\n")
    f.write(f"problem_schema = {mapping!r}")
