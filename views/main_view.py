class MainView:
    def display_menu():
        """affiche menu principal"""
        print("Menu Principal :")
        print("1 : Gestion des joueurs")
        print("2 : Gestion des Tournois")
        print("3 : Gestion des Rounds")
        print("4 : Gestion des matchs")
        print("5 : Rapports")
        print("6 : Quitter le programme")
        start_choice = input(
            "Saisir le numéro du menu auquel vous souhaiter accéder :"
            )
        return start_choice
