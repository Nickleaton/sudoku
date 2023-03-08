import logging
from argparse import ArgumentParser
from urllib.parse import urlparse, parse_qs
import lzstring
import json
from selenium import webdriver
from pathlib import Path

# directory = "problems/fpuzzles/json"

logging.basicConfig(level=logging.INFO)


def process_url(url: str, directory: Path) -> None:
    original_parsed = urlparse(url)
    original_qs = parse_qs(original_parsed.query)
    ident = original_qs['id'][0]
    filename = Path(directory) / Path(ident + ".json")
    if filename.exists():
        logging.log(logging.INFO, f"Skipping file {filename.name}")
        return
    driver = webdriver.Chrome()
    decompressor = lzstring.LZString()
    driver.get(url)
    current_parsed = urlparse(driver.current_url)
    query = parse_qs(current_parsed.query)
    uncompressed = decompressor.decompressFromBase64(query['load'][0].replace(" ", "+"))
    data = json.loads(uncompressed)

    all_data = {'url': url, 'data': data}
    with filename.open('w') as file:
        logging.log(logging.INFO, f"Writing file {filename.name}")
        file.write(json.dumps(all_data, sort_keys=True, indent=4))


def get_parser() -> ArgumentParser:
    result = ArgumentParser('create fpuzzles json', 'Down load json from an fpuzzles url file')
    result.add_argument('-s', '--source')
    result.add_argument('-d', '--destination')
    result.add_argument('-v', '--verbose', action='store_true')
    return result


def main() -> None:
    logging.log(logging.INFO, "Start")
    parser = get_parser()
    args = parser.parse_args()
    source = Path(args.source)
    destination = Path(args.destination)
    with open(source, 'r') as f:
        urls = f.readlines()
    for i, u in enumerate(urls):
        logging.log(logging.INFO, f"{i:04d} {len(urls):04d} {u.strip()}")
        process_url(u.strip(), destination)
    logging.log(logging.INFO, "Finish")


if __name__ == '__main__':
    main()
