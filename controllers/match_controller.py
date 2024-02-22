from views.match_view import Match_View
from controllers.tournament_controller import TournamentController

import random
import json


class MatchController:

    def update_scores():
        """mettre à jour les scores des matchs"""
        data = TournamentController.read_json("current_tournament")
        match_list = data[0]["rounds_list"][-1]["match_list"]
        player_list = data[0]["players_list"]
        for position, match in enumerate(match_list, start=1):
            print(position, match)
            choix = input("Mettre à jour les scores de ce match? oui/non? ")
            if choix == "oui":
                for joueur in match:
                    score = input(f"Quelle est le score de ce joueur {joueur} ?")
                    joueur["current_score"] = float(joueur["current_score"]) + float(score)
                    for player in player_list:
                        if joueur["ID"] == player["ID"]:
                            player["current_score"] = player["current_score"] + joueur["current_score"]
                with open("json_files/current_tournament.json", "w") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
            elif choix == "non":
                pass
            else:
                print("merci de répondre par oui ou par non")
            MatchController.winner_loser(match_list)

    def white_black():
        """tirage au sort de la couleur des pions"""
        pawn_color = random.randint(1, 2)
        if pawn_color == 1:
            pawn = "blanc"
        elif pawn_color == 2:
            pawn = "noir"
        return pawn

    def first_matchs_begins(first_round_list):
        """définir quel joueur joue avec les blancs"""
        for players in first_round_list:
            players_one = []
            players_one.append(players[0])
            for player_one in players_one:
                pawn_color = MatchController.white_black()
                Match_View.first_player(player_one, pawn_color)

    def winner_loser(match_list):
        """définit le gagnant d'un match"""
        for match in match_list:
            joueur1 = match[0]
            joueur2 = match[1]
            if joueur1["current_score"] == joueur2["current_score"]:
                print(f"match nul entre {joueur1} et {joueur2}")
            elif joueur1["current_score"] < joueur2["current_score"]:
                print(f"le gagnant de ce tour est : {joueur2}")
            elif joueur1["current_score"] > joueur2["current_score"]:
                print(f"le gagnant de ce tour est : {joueur1}")
