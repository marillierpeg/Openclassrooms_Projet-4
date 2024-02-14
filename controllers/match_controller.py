from views.match_view import Match_View
from controllers.round_controller import RoundController
from controllers.tournament_controller import TournamentController

import random
import json


class MatchController:

    def update_scores():
        data = TournamentController.read_json("current_tournament")
        match_list = data["rounds_list"][0]["match_list"]
        player_list = data["players_list"]
        for position, match in enumerate(match_list, start=1):
            print(position, match)
            choix = input("Mettre à jour les scores de ce match? oui/non? ")
            if choix == "oui":
                for joueur in match:
                    score = input(
                        f"Quelle est le score de ce joueur {joueur} ?"
                    )
                    joueur["current_score"] = \
                        float(joueur["current_score"]) + float(score)
                    for player in player_list:
                        if joueur["ID"] == player["ID"]:
                            player["current_score"] = joueur["current_score"]
                with open("json_files/current_tournament.json", "w") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
            elif choix == "non":
                pass
            else:
                print("merci de répondre par oui ou par non")

    def white_black():
        """tirage au sort couleur des pions en début de partie"""
        pawn_color = random.randint(1, 2)
        if pawn_color == 1:
            pawn = "blanc"
        elif pawn_color == 2:
            pawn = "noir"
        return pawn

    def first_matchs_begins():
        first_round_list = RoundController.start_first_round()
        for players in first_round_list:
            players_one = []
            players_one.append(players[0])
            for player_one in players_one:
                pawn_color = MatchController.white_black()
                Match_View.first_player(player_one, pawn_color)
