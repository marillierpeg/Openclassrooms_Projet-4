from views.tournament_view import Tournament_View
import json
import time


class TournamentController:
    def tournament_menu_choices():
        """affichage du menu tournoi"""
        while True:
            tournament_choice = Tournament_View.tournament_menu()
            if tournament_choice == "1":
                TournamentController.create_tournament()
            elif tournament_choice == "2":
                TournamentController.choose_tournament()
            elif tournament_choice == "3":
                TournamentController.close_tournament()
            elif tournament_choice == "4":
                break
            else:
                print("Choix invalide. Merci de saisir un nombre valide")
                time.sleep(1)

    def create_tournament():
        """création d'un nouveau tournoi"""
        tournament_name = Tournament_View.new_tournament_name()
        tournament_place = Tournament_View.new_tournament_place()
        tournament_rounds = Tournament_View.new_tournament_rounds()
        players = TournamentController.tournament_players()
        tournament_description = Tournament_View.new_tournament_description()
        tournament_start = time.strftime("%d-%m-%Y %H:%M:%S")
        tournament_info = [{
            "name": tournament_name,
            "place": tournament_place,
            "rounds": tournament_rounds,
            "round_number": "",
            "number_of_players": players[0],
            "description": tournament_description,
            "start_date": tournament_start,
            "players_list": players[1],
            "rounds_list": []
        }]
        try:
            with open(
                "json_files/current_tournament.json", "r", encoding="utf-8"
            ) as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        data.extend(tournament_info)
        with open("json_files/current_tournament.json", "w", encoding="utf-8")\
                as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def tournament_players():
        number_of_players = Tournament_View.number_of_players()
        players = []
        players_list = []
        with open("json_files/players.json", "r", encoding="utf-8") as file:
            data = json.load(file)
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

    def choose_tournament():
        tournament_list = []
        name = []
        place = []
        with open("json_files/current_tournament.json", "r", encoding="utf-8")\
                as file:
            data = json.load(file)
        for i in range(len(data)):
            dict_player = data[i]
            item_list = list(dict_player.items())
            tournament_list.append(item_list)
        for tournament in tournament_list:
            tournament_name = tournament[0]
            name.append(tournament_name[1])
            tournament_place = tournament[1]
            place.append(tournament_place[1])
        name_place = zip(name, place)
        choice = Tournament_View.display_tournament_players(name_place)
        if choice in name:
            print("ok")
        else:
            print("pas ok")

    def close_tournament():
        """terminer un tournoi"""
        with open("json_files/current_tournament.json", "r", encoding="utf_8")\
                as file:
            data = json.load(file)
        end = time.strftime("%d-%m-%Y %H:%M:%S")
        end_date = {"end_date": end}
        data.append(end_date)
        with open("json_files/ended_tournaments.json", "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        current_tournament_data = []
        with open("json_files/current_tournament.json", "w") as file:
            json.dump(current_tournament_data, file, ensure_ascii=False)
