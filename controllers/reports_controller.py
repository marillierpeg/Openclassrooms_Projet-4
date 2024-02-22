from controllers.player_controller import PlayerController
from views.reports_view import ReportsView
from views.tournament_view import Tournament_View
from controllers.tournament_controller import TournamentController

import time


class ReportsController:

    def rounds_and_match_report():
        "affiche rounds et matchs du tournoi en cours dans un fichier texte"
        data = TournamentController.read_json("current_tournament")
        rounds_list = data[0]["rounds_list"]
        name = data[0]["name"]
        start_tournament = data[0]["start_date"]
        with open("reports/current_tournament_rounds.txt", "w", encoding="utf_8") as file:
            file.write(f"Voici les détails du tournoi {name} en cours : \n")
            file.write(f"Ce tournoi a débuté le {start_tournament} \n")
            for rounds in rounds_list:
                round = rounds["round_number"]
                start_round = rounds["start_time"]
                match_list = rounds["match_list"]
                file.write(f"Tour n°{round} commencé le : {start_round} \n")
                file.write(f"match_list : {match_list} \n")
        print("Rapport créé")
        time.sleep(1)

    def display_all_players_alphabetically():
        """affichage de la liste des joueurs par \
        ordre alphabétique dans un fichier texte"""
        players = PlayerController.players_database()
        players_dict = [player.__dict__ for player in players]
        sorted_players = sorted(
            players_dict, key=lambda player: (player["last_name"], player["first_name"]))
        with open("reports/all_players.txt", "w", encoding="utf_8")\
                as file:
            for item in sorted_players:
                file.write(f"{item}\n")
        print("Rapport créé")
        time.sleep(1)

    def current_tournament_players():
        """affiche les joueurs du tournoi en cours dans un fichier texte"""
        """ordre alphabétique du nom puis du prénom"""
        data = TournamentController.read_json("current_tournament")
        players = [dict_player.get('players_list') for dict_player in data]
        players = players[0]
        sorted_names = sorted(players, key=lambda x: (x['last_name'], x['first_name']))
        with open("reports/current_tournament_players.txt", "w", encoding="utf_8") as file:
            for item in sorted_names:
                file.write(f"{item}\n")
        print("Rapport créé")
        time.sleep(1)

    def chose_tournament_to_display():
        "affiche les details d'un tournoi donné dans un fichier texte"
        while True:
            choice = Tournament_View.closed_or_current_tournament()
            """choix tournoi en cours ou terminé"""
            if choice == "1":
                data = TournamentController.read_json("current_tournament")
                details = data[0]
                name = details['name']
                start = details['start_date']
                with open(
                    "reports/current_tournaments_details.txt",
                    "w", encoding="utf_8"
                ) as file:
                    file.write(f"Tournoi {name} \n débuté le : {start}")
                print("Rapport créé")
                time.sleep(1)
                break

            elif choice == "2":
                data = TournamentController.read_json("ended_tournaments")
                names = []
                for tournament in data:
                    details = tournament[0]
                    names.append(details['name'].lower())
                closed_choice = Tournament_View.display_tournaments(names)
                if closed_choice.lower() in names:
                    for tournaments in data:
                        datas = tournaments[0]
                        if datas['name'].lower() == closed_choice.lower():
                            with open("reports/ended_tournaments_details.txt", "w", encoding="utf_8") as file:
                                file.write(
                                    f"Tournoi {datas['name']} \n \
                                    débuté le : {datas['start_date']} \n \
                                    terminé le : {datas['end_date']}"
                                )
                    print("Rapport créé")
                    time.sleep(1)
                    break

                else:
                    print(f"Le tournoi '{closed_choice}' n'existe pas.")
            else:
                print("choix invalide")
                break

    def ended_report():
        ended_data = TournamentController.read_json("ended_tournaments")
        for tournament in ended_data:
            details = tournament[0]
            with open(
                "reports/all_tournaments_details.txt", "a", encoding="utf_8"
            ) as file:
                file.write(
                    f"Tournoi {details['name']}"
                    f" débuté le: {details['start_date']}"
                    f" terminé le : {details['end_date']} \n"
                )

    def current_report():
        current_data = TournamentController.read_json("current_tournament")
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
                ReportsController.rounds_and_match_report()
            elif report_choice == "5":
                ReportsController.current_report()
                ReportsController.ended_report()
                time.sleep(1)
                print("Rapport créé")
                time.sleep(1)
            elif report_choice == "6":
                break
            else:
                print("Choix invalide. Merci de saisir un nombre valide")
                time.sleep(1)
