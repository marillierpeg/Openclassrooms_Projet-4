from views.main_view import MainView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.reports_controller import ReportsController
from controllers.round_controller import RoundController

import time


class MainController:
    def choices():
        while True:
            choice = MainView.display_menu()
            if choice == "1":
                PlayerController.player_menu_choice()
            elif choice == "2":
                TournamentController.tournament_menu_choices()
            elif choice == "3":
                RoundController.round_menu_choice()
            elif choice == "4":
                pass
            elif choice == "5":
                ReportsController.reports_menu()
            elif choice == "6":
                break
            else:
                print("Choix invalide. Merci de saisir un nombre valide")
                time.sleep(2)
