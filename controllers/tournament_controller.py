from views.tournament_view import Tournament_View
import json
import time


class TournamentController:
    def tournament_menu_choices():
        """menu tournoi"""
        while True:
            tournament_choice = Tournament_View.tournament_menu()
            if tournament_choice == "1":
                TournamentController.create_tournament()
            elif tournament_choice == "2":
                TournamentController.close_tournament()
            elif tournament_choice == "3":
                break
            else:
                print("Choix invalide. Merci de saisir un nombre valide")
                time.sleep(1)

    def create_tournament():
        """création d'un nouveau tournoi"""
        tournament_name = Tournament_View.new_tournament_name()
        tournament_place = Tournament_View.new_tournament_place()
        tournament_rounds = Tournament_View.new_tournament_rounds()
        players = TournamentController.tournament_add_players()
        tournament_description = Tournament_View.new_tournament_description()
        tournament_start = time.strftime("%d-%m-%Y %H:%M:%S")
        tournament_info = {
            "name": tournament_name,
            "place": tournament_place,
            "rounds": tournament_rounds,
            "number_of_players": players[0],
            "description": tournament_description,
            "start_date": tournament_start,
            "end_date": "",
            "players_list": players[1],
            "rounds_list": []
        }
        try:
            with open(
                "json_files/current_tournament.json", "r", encoding="utf-8"
            ) as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        data.append(tournament_info)
        with open("json_files/current_tournament.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def tournament_add_players():
        """ajoute des joueurs au tournoi"""
        number_of_players = Tournament_View.number_of_players()
        players = []
        players_list = []
        data = TournamentController.read_json("players")
        for i in range(len(data)):
            dict_player = data[i]
            item_list = list(dict_player.items())
            players.append(item_list)
        for player in players:
            if len(players_list) < number_of_players:
                Tournament_View.add_players(players_list, player)
            else:
                print("nombre maximum de joueurs atteint")
                break
        return number_of_players, players_list

    def close_tournament():
        """terminer un tournoi"""
        ended_data_list = []
        ended_data = TournamentController.read_json("ended_tournaments")
        ended_data_list.append(ended_data)
        data = TournamentController.read_json("current_tournament")
        end = time.strftime("%d-%m-%Y %H:%M:%S")
        data[0]["end_date"] = end
        ended_data_list.append(data)
        TournamentController.write_json("ended_tournaments", ended_data_list)

        current_tournament_data = []
        TournamentController.write_json(
            "current_tournament", current_tournament_data
        )

    def read_json(file_name):
        with open(
            f"json_files/{file_name}.json", "r", encoding="utf_8"
        ) as file:
            data = json.load(file)
        return data

    def write_json(file_name, data_to_write):
        with open(f"json_files/{file_name}.json", "w") as file:
            json.dump(data_to_write, file, ensure_ascii=False, indent=4)
