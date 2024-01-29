from views.match_view import Match_View
from controllers.round_controller import RoundController

import random


class MatchController:

    def white_black():
        """tirage au sort couleur des pions en début de partie"""
        pawn_color = random.randint(1, 2)
        if pawn_color == 1:
            pawn = "blanc"
        elif pawn_color == 2:
            pawn = "noir"
        return pawn

    def first_matchs_begins():
        first_round_list = RoundController.random_pairs_of_players()
        for players in first_round_list:
            players_one = []
            players_one.append(players[0])
            for player_one in players_one:
                pawn_color = MatchController.white_black()
                Match_View.first_player(player_one, pawn_color)

    def score_selection():
        """sélection joueurs suivant leurs scores"""
        pass

    def winner_loser():
        """définir les scores d'un  match"""
        pass
