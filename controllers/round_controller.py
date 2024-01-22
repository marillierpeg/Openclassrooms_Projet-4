from views.round_view import Round_View
from controllers.player_controller import PlayerController

import random
import time


class RoundController:

    def round_menu_choice():
        while True:
            round_choice = Round_View.display_round_menu()
            if round_choice == "1":
                pass
            elif round_choice == "2":
                break
            else:
                print("Choix invalide. Merci de saisir un nombre valide")
                time.sleep(1)

    def random_pairs_of_players():
        """génère une liste de paires de joueurs aléatoirement"""
        players = PlayerController.players_database()
        random.shuffle(players)
        first_round_list = []
        for i in range(0, len(players), 2):
            first_round_list.append(players[i:i + 2])

        return first_round_list
