from views.main_view import MainView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.reports_controller import ReportsController
from controllers.round_controller import RoundController

import time


class MainController:
    """menu principal"""
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
                ReportsController.reports_menu()
            elif choice == "5":
                break
            else:
                MainView.invalid_choice()
                time.sleep(2)
