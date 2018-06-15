import json
from data.source import Source


__sources = []

def get_sources():
    with open('../configs/egb_config.json', encoding='utf-8') as file:
        data = json.loads(file.read(), object_hook=__as_sources)
    return __sources


def __as_sources(dct):
    if 'url' in dct:
        __sources.append(Source(dct['url'], dct['home'], dct['guest'], dct['homeQuote'], dct['guestQuote']))


get_sources()