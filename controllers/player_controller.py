from views.player_view import ViewPlayer
from views.main_view import MainView
import json
import pprint
import time


class PlayerController:
    def create_player():
        """création d'un joueur"""
        first_name = ViewPlayer.first_name()
        last_name = ViewPlayer.last_name()
        date_of_birth = ViewPlayer.date_of_birth()
        ID_joueur = ViewPlayer.ID()
        score = 0
        players_info = [{
            "last_name": last_name,
            "first_name": first_name,
            "date_of_birth": date_of_birth,
            "ID": ID_joueur,
            "score": score
            }]
        try:
            with open(
                "json_files/players.json", "r", encoding="utf-8"
            ) as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        data.extend(players_info)
        with open("json_files/players.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        MainView.display_menu()

    def display_players():
        """affichage de la liste des joueurs par ordre alphabétique"""
        with open("json_files/players.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        players = []
        for i in range(len(data)):
            dict_player = data[i]
            item_list = list(dict_player.items())
            players.append(item_list)
        for i in range(len(players)):
            """Tri la liste d'abord par nom de famille puis par prénom"""
            sorted_name = sorted(players, key=lambda x: (x[0], x[1]))
        pprint.pprint(sorted_name)

    def player_menu_choice():
        """affichage du menu joueurs"""
        while True:
            player_choice = ViewPlayer.display_players_menu()
            if player_choice == "1":
                PlayerController.create_player()
            elif player_choice == "2":
                PlayerController.display_players()
            elif player_choice == "3":
                break
            else:
                print("Choix invalide. Merci de saisir un nombre valide")
                time.sleep(1)
