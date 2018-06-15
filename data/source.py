
class Source:
    def __init__(self, url, home, guest, homeQuote, guestQuote):
        self.url = url
        self.home = home
        self.guest = guest
        self.homeQuote = homeQuote
        self.guestQuote = guestQuote

    def __str__(self):
        return "url : %s , home : %s , guest : %s , homeQuote : %s , guestQuote : %s" % (self.url, self.home, self.guest, self.homeQuote, self.guestQuote)
