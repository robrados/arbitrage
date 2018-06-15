class Match:

    def __init__(self, player1, player2, quote1="", quote2="", league=""):
        self.player1 = player1
        self.player2 = player2
        self.quote1 = quote1
        self.quote2 = quote2
        self.league = league

    def __str__(self):
        return "player 1 : %s , player 2 : %s" % (self.player1, self.player2)
