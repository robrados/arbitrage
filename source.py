import json


def get_sources():
    json.loads(Source.file, object_hook=Source.as_sources)


def __as_sources(obj):
    if '__source__' not in obj:
        return obj
    return Source(obj['url'], obj['home'], obj['home'], obj['home'], obj['home'])


class Source:
    file = ''

    def __init__(self, url, home, guest, homeQuote, guestQuote):
        self.url = url
        self.home = home
        self.guest = guest
        self.homeQuote = homeQuote
        self.guestQuote = guestQuote
