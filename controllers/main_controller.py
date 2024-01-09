from views.main_view import MainView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
import time


class MainController:
    def choices():
        while True:
            choice = MainView.display_menu()
            if choice == "1":
                PlayerController.player_menu_choice()
            elif choice == "2":
                TournamentController.tournament_menu_choices()
            elif choice == "6":
                break
            else:
                print("Choix invalide. Merci de saisir un nombre valide")
                time.sleep(2)
