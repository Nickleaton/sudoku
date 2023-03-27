import inspect
import json
import logging
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import Dict, List, Tuple

import oyaml as yaml

logging.basicConfig(level=logging.INFO)


class ConversionException(Exception):
    pass


def header(data: Dict) -> Dict:
    size = data['size']
    board_x = size
    board_y = size
    if size == 9:
        box_x = 3
        box_y = 3
    elif size == 8:
        box_x = 2
        box_y = 4
    elif size == 6:
        box_x = 2
        box_y = 3
    else:
        box_x = 0
        box_y = 0
    author = data.get('author')
    if author is None:
        author = 'Unknown'
    elif author == '?':
        author = 'Unknown'
    return {'Board': f'{board_x}x{board_y}', 'Boxes': f'{box_x}x{box_y}', 'Author': author}


def grid(data: Dict, size: int) -> Dict:
    values = []
    for x in range(size):
        row = ""
        for y in range(size):
            cell = data['grid'][x][y]
            row += '.' if cell.get('value') is None else str(cell.get('value'))
        values.append(row)
    return {'Knowns': values}


def solution(data: Dict, size: int) -> Dict:
    result = []
    for x in range(size):
        row = ''
        for y in range(size):
            row += str(data['solution'][x * size + y])
        result.append(row)
    return {'Solution': result}


def rc(s: str) -> Tuple[int, int]:
    rs, cs = s[1:].split('C')
    return int(rs), int(cs)


def cyclic(s: str) -> str:
    if s == 'DL':
        return "A"
    if s == 'DR':
        return "C"
    if s == 'UL':
        return "A"
    if s == 'UR':
        return "C"
    return ""


def side(s: str, n: int) -> str:
    r, c = rc(s)
    if r == 0:
        return "T"
    if c == 0:
        return "L"
    if r == n + 1:
        return "B"
    if c == n + 1:
        return "R"
    return ""


def antiking() -> Dict:
    return {'AntiKing': ''}


def antiknight() -> Dict:
    return {'AntiKnight': ''}


def arrow(data: Dict) -> List:
    result = []
    for item in data:
        lhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['cells']])
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0][len(item['cells']):]])
        result.append({"SumArrow": f"{lhs}={rhs}"})
    return result


def maxarrow(data: Dict) -> List:
    result = []
    for item in data:
        lhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['cells']])
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0][len(item['cells']):]])
        result.append({"MaxArrow": f"{lhs}={rhs}"})
    return result


def productarrow(data: Dict) -> List:
    result = []
    for item in data:
        lhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['cells']])
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0][len(item['cells']):]])
        result.append({"ProductArrow": f"{lhs}={rhs}"})
    return result


def betweenline(data: Dict) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({"Between": rhs})
    return result


def clone(data: List) -> List:
    result = []
    for item in data:
        region = {'ClonedRegion': []}
        r1 = []
        r2 = []
        for c1, c2 in zip(item['cells'], item['cloneCells']):
            r1.append(c1[1] + c1[3])
            r2.append(c2[1] + c2[3])
        s1 = ",".join(r1)
        s2 = ",".join(r2)
        region['ClonedRegion'] = [s1, s2]
        result.append(region)
    return result


def columnindexer(data: List) -> List:
    result = []
    columns = set()
    for region in data:
        for cell in region['cells']:
            r, c = rc(cell)
            columns.add(c)
    for c in columns:
        result.append({"ColumnIndexer": c})
    return result


def diagonal_bltr() -> Dict:
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


def diagonal_tlbr() -> Dict:
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


def difference(data: List) -> List:
    if len(data) == 0:
        return []
    result = []
    for item in data:
        r1, c1 = rc(item['cells'][0])
        r2, c2 = rc(item['cells'][1])
        result.append({'ConsecutivePair': f"{r1}{c1}-{r2}{c2}"})
    return result


def disjointgroups() -> Dict:
    return {"DisjointGroups": ""}


def entropicline(data: List) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({'Entropic': rhs})
    return result


def even(data: List) -> List:
    result = []
    for item in data:
        r, c = rc(item['cell'])
        result.append({'EvenCell': f"{r}{c}"})
    return result


def extraregion(data: List) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['cells']])
        result.append({'UniqueRegion': rhs})
    return result


def killercage(data: List) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['cells']])
        if 'value' in item:
            lhs = item['value']
            result.append({'Killer': f"{lhs}={rhs}"})
        else:
            result.append({'UniqueRegion': rhs})
    return result


def littlekillersum(data: List, n: int) -> List:
    result = []
    for item in data:
        r, c = rc(item['cell'])
        rot = cyclic(item['direction'])
        s = side(item['cell'], n)
        if s in ('T', 'B'):
            x = c
        else:
            x = r
        value = int(item['value'])
        result.append({'LittleKiller': f"{s}{x}{rot}={value}"})
    return result


def lockout(data: List) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({'LockOut': rhs})
    return result


def maximum(data: List) -> List:
    result = []
    for item in data:
        r, c = rc(item['cell'])
        result.append({'FortressCell': f"{r}{c}"})
    return result


def negative() -> Dict:
    return {"NegativeXV": ""}


def nonconsecutive() -> Dict:
    return {'OrthogonallyAdjacent': ''}


def odd(data: List) -> List:
    result = []
    for item in data:
        r, c = rc(item['cell'])
        result.append({'OddCell': f"{r}{c}"})
    return result


def palindrome(data: List) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({'Palindrome': rhs})
    return result


def quadruple(data: Dict) -> List:
    result = []
    for quad in data:
        row = quad['cells'][0][1]
        col = quad['cells'][0][3]
        values = "".join([str(d) for d in quad['values']])
        result.append({'Quadruple': f"{row}{col}={values}"})
    return result


def ratio(data: Dict) -> List:
    if len(data) == 0:
        return []
    result = []
    for item in data:
        r1, c1 = rc(item['cells'][0])
        r2, c2 = rc(item['cells'][1])
        result.append({'KropkiPair': f"{r1}{c1}-{r2}{c2}"})
    return result


def regionsumline(data: List) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({'EqualSum': rhs})
    return result


def renban(data: List) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({'Renban': rhs})
    return result


def sandwichsum(data: List, n: int) -> List:
    result = []
    for item in data:
        r, c = rc(item['cell'])
        s = side(item['cell'], n)
        value = int(item['value'])
        if s in ('T', 'B'):
            x = c
        else:
            x = r
        result.append({'Sandwich': f"{s}{x}={value}"})
    return result


def thermometer(data: List) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({'SimpleThermometer': rhs})
    return result


def whispers(data: List) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({'GermanWhisper': rhs})
    return result


def xsum(data: List, n: int) -> List:
    result = []
    for item in data:
        r, c = rc(item['cell'])
        s = side(item['cell'], n)
        value = int(item['value'])
        if s in ('T', 'B'):
            x = c
        else:
            x = r
        result.append({'XSum': f"{s}{x}={value}"})
    return result


def xv(data: List) -> List:
    if len(data) == 0:
        return []
    result = []
    for item in data:
        r1, c1 = rc(item['cells'][0])
        r2, c2 = rc(item['cells'][1])
        if item['value'] == 'V':
            result.append({'VPair': f"{r1}{c1}-{r2}{c2}"})
        elif item['value'] == 'X':
            result.append({'XPair': f"{r1}{c1}-{r2}{c2}"})
    return result


def convert(source_file: Path, destination_file: Path) -> bool:
    logging.info(f"Convert {source_file} to {destination_file}")
    out = {}
    with source_file.open() as s_file:
        data = json.load(s_file)
    raw = data['data']
    n = raw['size']
    if n not in (6, 8, 9):
        logging.log(logging.ERROR, f"Unknown board size {n} {source_file}")
        return False
        # raise ConversionException(f"Unknown board size {size}")

    good = True
    try:
        out['Board'] = header(raw)
        out['Constraints'] = []
        out['Constraints'].append(grid(raw, n))
        out['Constraints'].append({'Columns': ''})
        out['Constraints'].append({'Rows': ''})
        out['Constraints'].append({'Boxes': ''})
        if 'solution' in raw:
            out['Constraints'].append(solution(raw, n))

        # if 'title' in raw:
        #     out['Constraints'].append(title(raw['title'], n))
        # if 'size' in raw:
        #     out['Constraints'].append(size(raw['size'], n))
        # if 'author' in raw:
        #     out['Constraints'].append(author(raw['author'], n))

        if 'antiking' in raw:
            out['Constraints'].append(antiking())
        if 'antiknight' in raw:
            out['Constraints'].append(antiknight())
        if 'arrow' in raw:
            out['Constraints'].extend(arrow(raw['arrow']))
        if 'maxarrow' in raw:
            out['Constraints'].extend(maxarrow(raw['maxarrow']))
        if 'productarrow' in raw:
            out['Constraints'].extend(productarrow(raw['productarrow']))

        if 'betweenline' in raw:
            out['Constraints'].extend(betweenline(raw['betweenline']))
        if 'clone' in raw:
            out['Constraints'].extend(clone(raw['clone']))
        if 'columnindexer' in raw:
            out['Constraints'].extend(columnindexer(raw['columnindexer']))
        if 'diagonal_bltr' in raw:
            out['Constraints'].append(diagonal_bltr())
        if 'diagonal_tlbr' in raw:
            out['Constraints'].append(diagonal_tlbr())
        if 'difference' in raw:
            out['Constraints'].extend(difference(raw['difference']))
        if 'disjointgroups' in raw:
            out['Constraints'].append(disjointgroups())
        if 'entropicline' in raw:
            out['Constraints'].extend(entropicline(raw['entropicline']))
        if 'even' in raw:
            out['Constraints'].extend(even(raw['even']))
        if 'extraregion' in raw:
            out['Constraints'].extend(extraregion(raw['extraregion']))
        # if 'highlightConflicts' in raw:
        #     out['Constraints'].append(highlightConflicts(raw['highlightConflicts']))
        if 'killercage' in raw:
            out['Constraints'].extend(killercage(raw['killercage']))
        # if 'line' in raw:
        #     out['Constraints'].append(line(raw['line']))
        if 'littlekillersum' in raw:
            out['Constraints'].extend(littlekillersum(raw['littlekillersum'], n))
        if 'lockout' in raw:
            out['Constraints'].append(lockout(raw['lockout']))
        if 'maximum' in raw:
            out['Constraints'].extend(maximum(raw['maximum']))
        if 'negative' in raw:
            out['Constraints'].append(negative())
        if 'nonconsecutive' in raw:
            out['Constraints'].append(nonconsecutive())
        if 'odd' in raw:
            out['Constraints'].extend(odd(raw['odd']))
        if 'palindrome' in raw:
            out['Constraints'].extend(palindrome(raw['palindrome']))
        if 'quadruple' in raw:
            out['Constraints'].extend(quadruple(raw['quadruple']))
        if 'ratio' in raw:
            out['Constraints'].extend(ratio(raw['ratio']))
        if 'regionsumline' in raw:
            out['Constraints'].extend(regionsumline(raw['regionsumline']))
        if 'renban' in raw:
            out['Constraints'].extend(renban(raw['renban']))
        # if 'ruleset' in raw:
        #     out['Constraints'].append(ruleset(raw['ruleset']))
        if 'sandwichsum' in raw:
            out['Constraints'].extend(sandwichsum(raw['sandwichsum'], n))
        if 'thermometer' in raw:
            out['Constraints'].extend(thermometer(raw['thermometer']))
        if 'whispers' in raw:
            out['Constraints'].extend(whispers(raw['whispers']))
        if 'xsum' in raw:
            out['Constraints'].append(xsum(raw['xsum'], n))
        if 'xv' in raw:
            out['Constraints'].extend(xv(raw['xv']))
    except NotImplementedError as e:
        logging.log(logging.ERROR, f"{e} {source_file}")
        good = False

    if good:
        with open(destination_file, 'w') as d_file:
            d_file.write(
                yaml.dump(
                    out,
                    indent=2,
                    default_style='',
                    default_flow_style=False,
                ).replace("'", "")
            )
    return good


def destination_file_name(source_file: Path, destination_directory: Path) -> Path:
    return destination_directory / (source_file.stem + ".yaml")


def get_parser() -> ArgumentParser:
    result = ArgumentParser('Convert', 'Convert FPuzzles to Yaml')
    result.add_argument('-s', '--source')
    result.add_argument('-d', '--destination')
    result.add_argument('-v', '--verbose', action='store_true')
    return result


def main() -> None:
    count = 0
    total_count = 0

    logging.info("Start")
    parser = get_parser()
    args = parser.parse_args()
    source = Path(args.source)
    destination = Path(args.destination)
    if source.is_dir():
        if destination.is_dir():
            for source_file in source.glob("*.json"):
                destination_file = destination_file_name(Path(source_file), destination)
                total_count += 1
                if convert(source_file, destination_file):
                    count += 1
        else:
            logging.log(logging.ERROR, "Cannot convert directory to single file")
            sys.exit(1)
    else:
        if destination.is_dir():
            destination_file = destination_file_name(source, destination)
            total_count += 1
            if convert(source, destination_file):
                count += 1
        else:
            total_count += 1
            if convert(source, destination):
                count += 1

    logging.info(F"Count {count} / {total_count}")
    logging.info("Finish")


if __name__ == '__main__':
    main()
