import inspect
import json
import logging
import sys
from pathlib import Path
from argparse import ArgumentParser
from typing import Dict, List, Tuple, Optional

import oyaml as yaml

logging.basicConfig(level=logging.WARNING)


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
    if s == 'DR':
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


def antiking(data: Dict, n: int) -> Dict:
    return {'AntiKing': ''}


def antiknight(data: Dict, n: int) -> Dict:
    return {'AntiKnight': ''}


def arrow(data: Dict, n: int) -> List:
    result = []
    for item in data:
        lhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['cells']])
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0][len(item['cells']):]])
        result.append({"SumArrow": f"{lhs}={rhs}"})
    return result


def maxarrow(data: Dict, n: int) -> List:
    result = []
    for item in data:
        lhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['cells']])
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0][len(item['cells']):]])
        result.append({"MaxArrow": f"{lhs}={rhs}"})
    return result


def productarrow(data: Dict, n: int) -> List:
    result = []
    for item in data:
        lhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['cells']])
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0][len(item['cells']):]])
        result.append({"ProductArrow": f"{lhs}={rhs}"})
    return result


def author(data: Dict, n: int) -> Dict:
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


def betweenline(data: Dict, n: int) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({"Between": rhs})
    return result


def cage(data: Dict, n: int) -> Dict:
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


def circle(data: Dict, n: int) -> Dict:
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


def clone(data: List, n: int) -> List:
    result = []
    for item in data:
        region = {'ClonedRegion': []}
        for c, cc in zip(item['cells'], item['cloneCells']):
            region['ClonedRegion'].append({'Clone': f"{c}={cc}"})
        result.append(region)
    return result


def columnindexer(data: List, n: int) -> List:
    result = []
    columns = set()
    for region in data:
        for cell in region['cells']:
            r, c = rc(cell)
            columns.add(c)
    for c in columns:
        result.append({"ColumnIndexer": c})
    return result


def diagonal_bltr(data: Dict, n: int) -> Dict:
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


def diagonal_tlbr(data: Dict, n: int) -> Dict:
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


def difference(data: List, n: int) -> List:
    if len(data) == 0:
        return []
    result = []
    for item in data:
        r1, c1 = rc(item['cells'][0])
        r2, c2 = rc(item['cells'][1])
        result.append({'ConsecutivePair': f"{r1}{c1}-{r2}{c2}"})
    return result


def disabledlogic(data: Dict, n: int) -> Dict:
    # TODO print(f'disabledlogic not implemented')
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


def disjointgroups(data: Dict, n: int) -> Dict:
    return {"DisjointGroups": ""}


def entropicline(data: List, n: int) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({'Entropic': rhs})
    return result


def even(data: List, n: int) -> List:
    result = []
    for item in data:
        result.append({'Even': rc(item['cell'])})
    return result


def extraregion(data: List, n: int) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['cells']])
        result.append({'UniqueRegion': rhs})
    return result


def highlightConflicts(data: Dict, n: int) -> Dict:
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


def killercage(data: List, n: int) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['cells']])
        if 'value' in item:
            lhs = item['value']
            result.append({'Killer': f"{lhs}={rhs}"})
        else:
            result.append({'UniqueRegion': rhs})
    return result


def line(data: Dict, n: int) -> Dict:
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


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


def lockout(data: List, n: int) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({'LockOut': rhs})
    return result


def maximum(data: List, n: int) -> List:
    result = []
    for item in data:
        result.append({'FortressCell': rc(item['cell'])})
    return result


def negative(data: Dict, n: int) -> Dict:
    return {"NegativeXV":""}


def nonconsecutive(data: Dict, n: int) -> Dict:
    return {'OrthoganallyAdjacent': ''}


def odd(data: List, n: int) -> List:
    result = []
    for item in data:
        result.append({'Odd': rc(item['cell'])})
    return result


def palindrome(data: List, n: int) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({'Palindrome': rhs})
    return result


def quadruple(data: Dict, n: int) -> List:
    result = []
    for quad in data:
        row = quad['cells'][0][1]
        col = quad['cells'][0][3]
        values = "".join([str(d) for d in quad['values']])
        result.append({'Quadruple': f"{row}{col}={values}"})
    return result


def ratio(data: Dict, n: int) -> List:
    if len(data) == 0:
        return []
    result = []
    for item in data:
        r1, c1 = rc(item['cells'][0])
        r2, c2 = rc(item['cells'][1])
        result.append({'KropkiPair': f"{r1}{c1}-{r2}{c2}"})
    return result


def rectangle(data: Dict, n: int) -> Dict:
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


def regionsumline(data: List, n: int) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({'EqualSum': rhs})
    return result


def renban(data: List, n: int) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({'Renban': rhs})
    return result


def ruleset(data: Dict, n: int) -> Dict:
    return {}


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


def size(data: List, n: int) -> List:
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


def text(data: Dict, n: int) -> Dict:
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


def thermometer(data: List, n: int) -> List:
    result = []
    for item in data:
        rhs = ", ".join([f"{rc(cell)[0]}{rc(cell)[1]}" for cell in item['lines'][0]])
        result.append({'SimpleThermometer': rhs})
    return result


def title(data: Dict, n: int) -> Dict:
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


def truecandidatesoptions(data: Dict, n: int) -> Dict:
    raise NotImplementedError(inspect.currentframe().f_code.co_name)


def whispers(data: List, n: int) -> List:
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


def xv(data: List, n: int) -> List:
    if len(data) == 0:
        return []
    result = []
    for item in data:
        r1, c1 = rc(item['cells'][0])
        r2, c2 = rc(item['cells'][1])
        if item['value'] == 'V':
            result.append({'V_Pair': f"{r1}{c1}-{r2}{c2}"})
        elif item['value'] == 'X':
            result.append({'X_Pair': f"{r1}{c1}-{r2}{c2}"})
    return result


def convert(source_file: Path, destination_file: Path) -> bool:
    logging.log(logging.INFO, f"Convert {source_file} to {destination_file}")
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
            out['Constraints'].append(antiking(raw['antiking'], n))
        if 'antiknight' in raw:
            out['Constraints'].append(antiknight(raw['antiknight'], n))
        if 'arrow' in raw:
            out['Constraints'].extend(arrow(raw['arrow'], n))
        if 'maxarrow' in raw:
            out['Constraints'].extend(maxarrow(raw['maxarrow'], n))
        if 'productarrow' in raw:
            out['Constraints'].extend(productarrow(raw['productarrow'], n))

        if 'betweenline' in raw:
            out['Constraints'].extend(betweenline(raw['betweenline'], n))
        # if 'cage' in raw:
        #     out['Constraints'].append(cage(raw['cage'], n))
        # if 'circle' in raw:
        #     out['Constraints'].append(circle(raw['circle'], n))
        if 'clone' in raw:
            out['Constraints'].extend(clone(raw['clone'], n))
        if 'columnindexer' in raw:
            out['Constraints'].extend(columnindexer(raw['columnindexer'], n))
        if 'diagonal_bltr' in raw:
            out['Constraints'].append(diagonal_bltr(raw['diagonal_bltr'], n))
        if 'diagonal_tlbr' in raw:
            out['Constraints'].append(diagonal_tlbr(raw['diagonal_tlbr'], n))
        if 'difference' in raw:
            out['Constraints'].append(difference(raw['difference'], n))
        # if 'disabledlogic' in raw:
        #     out['Constraints'].append(disabledlogic(raw['disabledlogic'], n))
        if 'disjointgroups' in raw:
            out['Constraints'].append(disjointgroups(raw['disjointgroups'], n))
        if 'entropicline' in raw:
            out['Constraints'].extend(entropicline(raw['entropicline'], n))
        if 'even' in raw:
            out['Constraints'].extend(even(raw['even'], n))
        if 'extraregion' in raw:
            out['Constraints'].extend(extraregion(raw['extraregion'], n))
        # if 'highlightConflicts' in raw:
        #     out['Constraints'].append(highlightConflicts(raw['highlightConflicts'], n))
        if 'killercage' in raw:
            out['Constraints'].extend(killercage(raw['killercage'], n))
        # if 'line' in raw:
        #     out['Constraints'].append(line(raw['line'], n))
        if 'littlekillersum' in raw:
            out['Constraints'].append(littlekillersum(raw['littlekillersum'], n))
        if 'lockout' in raw:
            out['Constraints'].append(lockout(raw['lockout'], n))
        if 'maximum' in raw:
            out['Constraints'].append(maximum(raw['maximum'], n))
        if 'negative' in raw:
            out['Constraints'].append(negative(raw['negative'], n))
        if 'nonconsecutive' in raw:
            out['Constraints'].append(nonconsecutive(raw['nonconsecutive'], n))
        if 'odd' in raw:
            out['Constraints'].extend(odd(raw['odd'], n))
        if 'palindrome' in raw:
            out['Constraints'].extend(palindrome(raw['palindrome'], n))
        if 'quadruple' in raw:
            out['Constraints'].extend(quadruple(raw['quadruple'], n))
        if 'ratio' in raw:
            out['Constraints'].append(ratio(raw['ratio'], n))
        if 'rectangle' in raw:
            out['Constraints'].append(rectangle(raw['rectangle'], n))
        if 'regionsumline' in raw:
            out['Constraints'].extend(regionsumline(raw['regionsumline'], n))
        if 'renban' in raw:
            out['Constraints'].extend(renban(raw['renban'], n))
        # if 'ruleset' in raw:
        #     out['Constraints'].append(ruleset(raw['ruleset'], n))
        if 'sandwichsum' in raw:
            out['Constraints'].extend(sandwichsum(raw['sandwichsum'], n))

        # if 'text' in raw:
        #     out['Constraints'].append(text(raw['text'], n))
        if 'thermometer' in raw:
            out['Constraints'].extend(thermometer(raw['thermometer'], n))

        # if 'truecandidatesoptions' in raw:
        #     out['Constraints'].append(truecandidatesoptions(raw['truecandidatesoptions'], n))
        if 'whispers' in raw:
            out['Constraints'].extend(whispers(raw['whispers'], n))
        if 'xsum' in raw:
            out['Constraints'].append(xsum(raw['xsum'], n))
        if 'xv' in raw:
            out['Constraints'].extend(xv(raw['xv'], n))
    except NotImplementedError as e:
        logging.log(logging.ERROR, f"{e}")
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

    logging.log(logging.INFO, "Start")
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

    logging.log(logging.INFO, F"Count {count} / {total_count}")
    logging.log(logging.INFO, "Finish")


if __name__ == '__main__':
    main()
