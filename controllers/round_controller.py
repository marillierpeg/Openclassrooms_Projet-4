from views.round_view import Round_View
from controllers.tournament_controller import TournamentController
from controllers.match_controller import MatchController

import random
import time
import json
from copy import deepcopy


class RoundController:

    def end_round():
        data = TournamentController.read_json("current_tournament")
        round = data["rounds_list"][-1]
        end_time = time.strftime("%d-%m-%Y %H:%M:%S")
        round["end_time"] = end_time
        with open("json_files/current_tournament.json", "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def start_first_round():
        data = TournamentController.read_json("current_tournament")
        for element in range(len(data)):
            dict = data[element]
            players_list = dict['players_list']
            rounds_list = dict['rounds_list']
        random.shuffle(players_list)
        first_round_list = []
        for i in range(0, len(players_list), 2):
            # parcours la liste de joueurs 2par2
            first_round_list.append(players_list[i:i + 2])
            # ajoute à la liste joueurs de l'index i à i+1
        match_list = deepcopy(first_round_list)
        for match in match_list:
            for dict in match:
                del dict['date_of_birth']
                del dict['last_name']
                del dict['first_name']
        start_round = time.strftime("%d-%m-%Y %H:%M:%S")
        dict_round = {
            "round_number": 1, "start_time": start_round,
            "end_time": "", "match_list": match_list
        }
        rounds_list.append(dict_round)
        with open(
            "json_files/current_tournament.json", "w", encoding="utf-8"
        ) as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Voici la liste des matchs de ce tour :")
        print(match_list)

    def round_menu_choice():
        while True:
            round_choice = Round_View.display_round_menu()
            if round_choice == "1":
                MatchController.first_matchs_begins()
            elif round_choice == "2":
                RoundController.end_round()
            elif round_choice == "3":
                pass
            elif round_choice == "4":
                MatchController.update_scores()
            elif round_choice == "5":
                break
            else:
                print("Choix invalide. Merci de saisir un nombre valide")
                time.sleep(1)
