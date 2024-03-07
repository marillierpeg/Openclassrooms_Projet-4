class MainView:
    def display_menu():
        """affiche menu principal"""
        print("Menu Principal :")
        print("1 : Gestion des Joueurs")
        print("2 : Gestion des Tournois")
        print("3 : Gestion des Tours")
        print("4 : Rapports")
        print("5 : Quitter le programme")
        start_choice = input(
            "Saisir le numéro du menu auquel vous souhaiter accéder :"
            )
        return start_choice

    def invalid_choice():
        print("Choix invalide")
