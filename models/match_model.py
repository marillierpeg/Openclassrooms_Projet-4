"""Définit un match"""


class ModelMatch:
    def __init__(self, two_players=[], winner="", loser="", draw=""):
        self.two_players = two_players
        self.winner = winner
        self.loser = loser
        self.draw = draw
