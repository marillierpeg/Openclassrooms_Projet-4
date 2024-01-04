"""Définit un tournoi"""


class ModelTournament:
    def __init__(self,
                 name="",
                 place="",
                 start_date="",
                 end_date="",
                 rounds=4,
                 round_number="",
                 description="",
                 players_list=[],
                 numbers_of_players=""
                 ):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.round_number = round_number
        self.description = description
        self.players_list = players_list
        self.numbers_of_players = numbers_of_players
