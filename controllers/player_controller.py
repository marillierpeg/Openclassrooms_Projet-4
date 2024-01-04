from views.player_view import ViewPlayer
from views.main_view import MainView
import json
import pprint
import time


class ControllerPlayer:
    def create_player():
        """création d'un joueur"""
        first_name = ViewPlayer.first_name()
        last_name = ViewPlayer.last_name()
        date_of_birth = ViewPlayer.date_of_birth()
        ID_joueur = ViewPlayer.ID()
        score = 0
        players_info = [{
            "Nom :": last_name,
            "Prénom :": first_name,
            "Date de naissance :": date_of_birth,
            "ID :": ID_joueur,
            "Score :": score
            }]
        try:
            with open(
                "json_files/Joueurs.json", "r", encoding="utf-8"
            ) as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        data.extend(players_info)
        with open("json_files/Joueurs.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        MainView.display_menu()

    def display_players():
        with open("json_files/Joueurs.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        players = []
        for i in range(len(data)):
            dict_player = data[i]
            item_list = list(dict_player.items())
            players.append(item_list)
        for i in range(len(players)):
            sorted_name = sorted(players, key=lambda x: (x[0], x[1]))
        pprint.pprint(sorted_name)

    def player_menu_choice():
        while True:
            player_choice = ViewPlayer.display_players_menu()
            if player_choice == "1":
                ControllerPlayer.create_player()
            elif player_choice == "2":
                ControllerPlayer.display_players()
            elif player_choice == "3":
                break
            else:
                print("Choix invalide. Merci de saisir un nombre valide")
                time.sleep(2)
