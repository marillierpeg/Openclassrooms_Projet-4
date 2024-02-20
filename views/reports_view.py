class ReportsView:
    def display_reports_menu():
        print("Menu Rapports")
        print("1 : Liste de tous les joueurs (ordre alphabétique)")
        print("2 : Liste des joueurs du tournoi en cours "
              "(ordre alphabétique)")
        print("3 : Nom et dates d'un tournoi donné")
        print("4 : Liste des tours et matchs du tournoi en cours")
        print("5 : Liste de tous les tournois")
        print("6 : Retour au menu principal")
        rapport_choice = input(
            "Saisir le numéro du menu auquel vous souhaiter accéder : "
            )
        return rapport_choice
