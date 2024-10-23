from strictyaml import Map, Seq, Optional, Str, Float, Int, Regex, EmptyNone

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

Cells_Comma_Separated = Regex(r'\s*\d{2}\s*(,\s*\d{2}\s*)*')
Digits_Comma_Separated = Regex(r'\s*\d\s*(,\s*\d\s*)*')
Knowns = Regex(r'[0-9.flmheo]+')
Cell_Pairs = Regex('\d\d-\d\d')
Little_Killers = Regex(r'[TLBR]\d[C|A]=\d+')
Quadruples = Regex(r'\d\d=[\d\?]+')
Rossini = Regex(r'[TLBR]\d=[DIU]')
OutsideArrowValue = Regex(r'[TLBR]\d=\d+')
CellValue = Regex(r'\d\d=\d+')
VertexDigit = Regex(r'\d\d=\d')
VertexValue = Regex(r'\d\d=\d+')


problem_schema = Map(
    {
        'Board': Map(
            {
                'Board': Str(),
                Optional('Boxes'): Str(),
                Optional('Video'): Str(),
                Optional('Reference'): Str(),
                Optional('Author'): Str(),
                Optional('Title'): Str()
            }
        ),
        'Constraints': Map(
            {
                Optional('Columns'): EmptyNone(),
                Optional('Rows'): EmptyNone(),
                Optional('Boxes'): EmptyNone(),
                Optional('DisjointGroups'): EmptyNone(),
                Optional('AntiRossini'): EmptyNone(),
                Optional('NegativeBattenburg'): EmptyNone(),
                Optional('OrthogonallyAdjacent'): EmptyNone(),
                Optional('AntiKnight'): EmptyNone(),
                Optional('AntiKing'): EmptyNone(),
                Optional('Asterix'): EmptyNone(),
                Optional('Girandola'): EmptyNone(),
                Optional('Quadro'): EmptyNone(),
                Optional('AntiQueen'): Digits_Comma_Separated,
                Optional('TLBR'): EmptyNone(),
                Optional('BLTR'): EmptyNone(),
                Optional('AntiTLBR'): EmptyNone(),
                Optional('AntiBLTR'): EmptyNone(),
                Optional('TLBRReflecting'): EmptyNone(),
                Optional('Knowns'): Seq(Knowns),
                Optional('Palindromes'): Seq(Cells_Comma_Separated),
                Optional('Windows'): Cells_Comma_Separated,
                Optional('LittleKillers'): Seq(Little_Killers),
                Optional('SimpleThermometers'): Seq(Cells_Comma_Separated),
                Optional('FrozenThermometers'): Seq(Cells_Comma_Separated),
                Optional('MinMaxSums'): Seq(OutsideArrowValue),
                Optional('SumArrows'): Seq(Cells_Comma_Separated),
                Optional('GermanWhispers'): Seq(Cells_Comma_Separated),
                Optional('DutchWhispers'): Seq(Cells_Comma_Separated),
                Optional('Mountains'): Seq(Cells_Comma_Separated),
                Optional('SumArrows'): Seq(Cells_Comma_Separated),
                Optional('MaxArrows'): Seq(Cells_Comma_Separated),
                Optional('Renbans'): Seq(Cells_Comma_Separated),
                Optional('EntropicLines'): Seq(Cells_Comma_Separated),
                Optional('EqualSums'): Seq(Cells_Comma_Separated),
                Optional('Rossinis'): Seq(Rossini),
                Optional('Quadruples'): Seq(Quadruples),
                Optional('ConsecutivePairs'): Seq(Cell_Pairs),
                Optional('Sandwiches'): Seq(OutsideArrowValue),
                Optional('NumberedRooms'): Seq(OutsideArrowValue),
                Optional('KropkiPairs'): Seq(Cell_Pairs),
                Optional('VPairs'): Seq(Cell_Pairs),
                Optional('XPairs'): Seq(Cell_Pairs),
                Optional('Frames'): Seq(OutsideArrowValue),
                Optional('Outsides'): Seq(OutsideArrowValue),
                Optional('Betweens'): Seq(Cells_Comma_Separated),
                Optional('OrthogonalProducts'): Seq(CellValue),
                Optional('Exclusions'): Seq(VertexDigit),
                Optional('CenterProducts'): Seq(VertexValue),
                Optional('MinMaxDifferences'): Seq(OutsideArrowValue),
                Optional('FrameProducts'): Seq(OutsideArrowValue),
                Optional('Sequences'): Seq(Cells_Comma_Separated),
                Optional('ColumnIndexer'): Digits_Comma_Separated,
                Optional('Knight'): Digits_Comma_Separated,
                Optional('MagicSquares'): Cells_Comma_Separated,
                Optional('Battenburg'): Cells_Comma_Separated,
                Optional('OddCells'): Cells_Comma_Separated,
                Optional('EvenCells'): Cells_Comma_Separated,
                Optional('FixedProductPairs'): Seq(Cell_Pairs),
                Optional('FixedRatioPairs'): Seq(Cell_Pairs),
                Optional('FixedSumPairs'): Seq(Cell_Pairs),
                Optional('FixedDifferencePairs'): Seq(Cell_Pairs),
                Optional('MOTES'): Seq(Cells_Comma_Separated),
            },
        ),
        Optional('Solution'): Seq(Regex("[0-9]+")),
    }
)
