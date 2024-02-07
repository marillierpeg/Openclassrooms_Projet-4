from views.player_view import ViewPlayer
from models.player_model import ModelPlayer

import json
import time
import pprint


class PlayerController:
    def create_player():
        """création d'un joueur"""
        first_name = ViewPlayer.first_name()
        last_name = ViewPlayer.last_name()
        date_of_birth = ViewPlayer.date_of_birth()
        ID_joueur = ViewPlayer.ID()
        current_score = 0
        players_info = [{
            "last_name": last_name,
            "first_name": first_name,
            "date_of_birth": date_of_birth,
            "ID": ID_joueur,
            "current_score": current_score
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

    def players_database():
        players = []
        with open("json_files/players.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        for players_data in range(len(data)):
            dict_player = data[players_data]
            player = ModelPlayer(
                dict_player['first_name'],
                dict_player['last_name'],
                dict_player['date_of_birth'],
                dict_player['ID'],
                dict_player['current_score']
                )
            players.append(player)
        return players

    def player_menu_choice():
        """affichage du menu joueurs"""
        while True:
            player_choice = ViewPlayer.display_players_menu()
            if player_choice == "1":
                PlayerController.create_player()
            elif player_choice == "2":
                pprint.pprint(PlayerController.players_database())
            elif player_choice == "3":
                break
            else:
                print("Choix invalide. Merci de saisir un nombre valide")
                time.sleep(1)
