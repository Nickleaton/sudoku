from urllib.parse import urlparse, parse_qs
import lzstring
import json
from selenium import webdriver
from pathlib import Path

directory = "problems/fpuzzles/json"


def process_url(url: str) -> None:
    original_parsed = urlparse(url)
    original_qs = parse_qs(original_parsed.query)
    ident = original_qs['id'][0]
    driver = webdriver.Chrome()
    decompressor = lzstring.LZString()
    driver.get(url)
    current_parsed = urlparse(driver.current_url)
    query = parse_qs(current_parsed.query)
    uncompressed = decompressor.decompressFromBase64(query['load'][0].replace(" ", "+"))
    data = json.loads(uncompressed)
    filename = Path(directory) / Path(ident + ".json")
    all_data = {'url': url, 'data': data}
    with filename.open('w') as file:
        file.write(json.dumps(all_data, sort_keys=True, indent=4))


def process_all() -> None:
    print("Start")
    with open('url.txt', 'r') as f:
        urls = f.readlines()
    for i, u in enumerate(urls):
        print(f"{i:04d} {len(urls):04d} {u.strip()}")
        process_url(u.strip())
    print("Finish")


if __name__ == '__main__':
    process_all()
