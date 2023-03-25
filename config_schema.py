from strictyaml import Map, Seq, Optional, Str, Float, Int

config_schema = Map(
    {
        'statistic_database': Str(),
        'statistic_elements': Map(Str(), Str()),
        'drawing':
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
    }
)

problem_schema = Map(
    {
        'Board': Map(
            {
                'Board': Str(),
                'Boxes': Str(),
                'Video': Str(),
                'Reference': Str(),
                'Author': Str(),
                'Title': Str()
            }
        ),
        'Constraints': Map(
            {
                Optional('AntiBLTR'): None,
                Optional('AntiKing'): None,
                Optional('AntiKnight'): None,
                Optional('AntiQueen'): Int(),
                Optional('AntiRossini'): None,
                Optional('AntiTLBR'): None,
                Optional('Arrow'): Str(),
                Optional('Arrow'): Str(),
                Optional('Asterix'): None,
                Optional('BLTR'): None,
                Optional('Battenburg'): Str(),
                Optional('Between'): Str(),
                Optional('Boxes'): None,
                Optional('CenterProduct'): Str(),
                Optional('ColumnIndexer'): Int(),
                Optional('Columns'): None,
                Optional('ConsecutivePair'): Str(),
                Optional('ConsecutivePair'): Str(),
                Optional('DisjointGroups'): None,
                Optional('DutchWhisper'): Str(),
                Optional('Entropic'): Str(),
                Optional('EqualSum'): Str(),
                Optional('EvenCell'): Str(),
                Optional('Exclusion'): None,
                Optional('Exclusion'): Str(),
                Optional('FixedDifferencePair'): Str(),
                Optional('FixedProductPair'): Str(),
                Optional('FixedRatioPair'): Str(),
                Optional('FixedSumPair'): Str(),
                Optional('Frame'): Str(),
                Optional('FrameProduct'): Str(),
                Optional('FrozenThermometer'): Str(),
                Optional('GermanWhisper'): Str(),
                Optional('Girandola'): None,
                Optional('Knight'): Str(),
                Optional('Knowns'): Seq(Str()),
                Optional('KropkiPair2'): Str(),
                Optional('LittleKiller'): Str(),
                Optional('MagicSquare'): Str(),
                Optional('MaxArrow'): Str(),
                Optional('MinMaxDifference'): Str(),
                Optional('MinMaxSum'): Str(),
                Optional('Mountain'): Str(),
                Optional('NegativeBattenburg'): None,
                Optional('NumberedRoom'): Str(),
                Optional('NumberedRoom'): Str(),
                Optional('OddCell'): Str(),
                Optional('OrthogonalProduct'): Str(),
                Optional('Outside'): Str(),
                Optional('Palindrome'): Str(),
                Optional('Quadro'): None,
                Optional('Quadruple'): Str(),
                Optional('Renban'): Str(),
                Optional('Rossini'): Str(),
                Optional('RowIndexer'): Int(),
                Optional('Rows'): None,
                Optional('Sandwich'): Str(),
                Optional('Sequence'): Str(),
                Optional('SimpleThermometer'): Str(),
                Optional('Solution'): Seq(Str()),
                Optional('TLBR'): None,
                Optional('TLBRReflecting'): None,
                Optional('VIPair'): Str(),
                Optional('VPair'): Str(),
                Optional('Window'): Str(),
                Optional('XIPair'): Str(),
                Optional('XPair'): Str()
            }
        )
    }
)
