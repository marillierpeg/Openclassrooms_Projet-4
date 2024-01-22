from views.match_view import Match_View
from controllers.round_controller import RoundController
import random


class MatchController:

    def white_black():
        """tirage au sort couleur des pions en début de partie"""
        couleur_pion = random.randint(1, 2)
        if couleur_pion == 1:
            pions = "blanc"
        elif couleur_pion == 2:
            pions = "noir"
        return pions

    def first_matchs_begins():
        first_round_list = RoundController.random_pairs_of_players()
        for players in first_round_list:
            players_one = []
            players_one.append(players[0])
            for player_one in players_one:
                couleur_pion = MatchController.white_black()
                Match_View.first_player(player_one, couleur_pion)

    def score_selection():
        """sélection joueurs suivant leurs scores"""
        pass

    def winner_loser():
        """définir le gagnant d'un  match"""
        pass
