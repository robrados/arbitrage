import json


def get_sources():
    with open('./configs/egb_config.json', encoding='utf-8') as file:
        data = json.loads(file.read(), object_hook=__as_sources)


def __as_sources(dct):
    if 'url' in dct:
        src = Source(dct['url'], dct['home'], dct['guest'], dct['homeQuote'], dct['guestQuote'])
        print(src)


class Source:
    def __init__(self, url, home, guest, homeQuote, guestQuote):
        self.url = url
        self.home = home
        self.guest = guest
        self.homeQuote = homeQuote
        self.guestQuote = guestQuote

    def __str__(self):
        return "url : %s , home : %s , guest : %s , homeQuote : %s , guestQuote : %s" % (self.url, self.home, self.guest, self.homeQuote, self.guestQuote)


get_sources()
