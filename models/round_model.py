class ModelRound:
    """définit un tour"""
    def __init__(self, tournament_name="",
                 start_date="",
                 end_date="",
                 round_number="",
                 players_pairs=[]
                 ):
        self.tournament_name = tournament_name
        self.start_date = start_date
        self.end_date = end_date
        self.round_number = round_number
        self.players_pairs = players_pairs
