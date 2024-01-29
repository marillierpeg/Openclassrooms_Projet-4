from controllers.player_controller import PlayerController
from views.reports_view import ReportsView
from views.tournament_view import Tournament_View

import json
import time


class ReportsController:

    def tournament_players_database():
        """joueurs du tournoi en cours"""
        with open("json_files/current_tournament.json", "r", encoding="utf_8")\
                as file:
            data = json.load(file)
        players = [dict_player.get('players_list') for dict_player in data]
        sorted_names = sorted(players, key=lambda x: (x[0], x[1]))
        return sorted_names

    def display_all_players_alphabetically():
        """affichage de la liste des joueurs par ordre alphabétique"""
        players = PlayerController.players_database()
        players_dict = [player.__dict__ for player in players]
        sorted_players = sorted(
            players_dict, key=lambda player: (player['last_name'],
                                              player['first_name'])
            )
        with open("reports/all_players.txt", "w", encoding="utf_8")\
                as file:
            for item in sorted_players:
                file.write(f"{item}\n")

    def current_tournament_players():
        """joueurs du tournoi en cours"""
        with open("json_files/current_tournament.json", "r", encoding="utf_8")\
                as file:
            data = json.load(file)
        players = [dict_player.get('players_list') for dict_player in data]
        players = players[0]
        sorted_names = sorted(
            players, key=lambda x: (x['last_name'], x['first_name'])
            )
        with open(
            "reports/current_tournament_players.txt", "w", encoding="utf_8"
        ) as file:
            for item in sorted_names:
                file.write(f"{item}\n")

    def chose_tournament_to_display():
        while True:
            choice = Tournament_View.closed_or_current_tournament()
            if choice == "1":
                with open(
                    "json_files/current_tournament.json", "r", encoding="utf_8"
                ) as file:
                    data = json.load(file)
                details = data[0]
                name = details['name']
                start = details['start_date']
                with open(
                    "reports/current_tournaments_details.txt", "w"
                ) as file:
                    file.write(f"Tournoi {name} \n débuté le : {start}")
            elif choice == "2":
                with open(
                    "json_files/ended_tournaments.json", "r", encoding="utf_8"
                ) as file:
                    data = json.load(file)
                names = []
                for tournament in data:
                    details = tournament[0]
                    names.append(details['name'].lower())
                closed_choice = Tournament_View.display_tournaments(names)
                if closed_choice.lower() in names:
                    print(f"Détails du tournoi {closed_choice}:")
                    for tournament in data:
                        details = tournament[0]
                        end = tournament[1]
                        if details['name'].lower() == closed_choice.lower():
                            with open(
                                "reports/ended_tournaments_details.txt", "w",
                                encoding="utf_8"
                            ) as file:
                                file.write(
                                    f"Tournoi {details['name']} \n \
                                    débuté le : {details['start_date']} \n \
                                    terminé le : {end['end_date']}"
                                )
                        else:
                            print(
                                f"Le tournoi '{closed_choice}' n'existe pas."
                            )
                break
            else:
                print("choix invalide")

    def open_current_json():
        with open(
            "json_files/current_tournament.json", "r", encoding="utf_8"
        ) as file:
            data = json.load(file)
        return data

    def open_ended_json():
        with open(
            "json_files/ended_tournaments.json", "r", encoding="utf_8"
        ) as file:
            data = json.load(file)
        return data

    def ended_report():
        ended_data = ReportsController.open_ended_json()
        for tournament in ended_data:
            details = tournament[0]
            end = tournament[1]
            with open(
                "reports/all_tournaments_details.txt", "a", encoding="utf_8"
            ) as file:
                file.write(
                    f"Tournoi {details['name']}"
                    f" débuté le: {details['start_date']}"
                    f" terminé le : {end['end_date']} \n"
                )

    def current_report():
        current_data = ReportsController.open_current_json()
        current_details = current_data[0]
        with open(
            "reports/all_tournaments_details.txt", "a", encoding="utf_8"
        ) as file:
            file.write(
                f"Tournoi {current_details['name']}"
                f" débuté le : {current_details['start_date']}"
                f" (Tournoi en cours) \n"
            )

    def reports_menu():
        while True:
            report_choice = ReportsView.display_reports_menu()
            if report_choice == "1":
                ReportsController.display_all_players_alphabetically()
            elif report_choice == "2":
                ReportsController.current_tournament_players()
            elif report_choice == "3":
                ReportsController.chose_tournament_to_display()
            elif report_choice == "4":
                pass
            elif report_choice == "5":
                ReportsController.current_report()
                ReportsController.ended_report()
            elif report_choice == "6":
                break
            else:
                print("Choix invalide. Merci de saisir un nombre valide")
                time.sleep(1)
