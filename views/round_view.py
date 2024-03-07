class Round_View:
    def display_round_menu():
        """affiche menu des tours"""
        print("Menu tours")
        print("1. Démarrer un premier tour")
        print("2. Terminer un tour")
        print("3. Démarrer un autre tour")
        print("4. Saisir les scores des matchs d'un tour")
        print("5. Revenir au menu principal")
        choice = input(
            "Merci de saisir le numéro du menu auquel vous voulez accéder : "
            )
        return choice

    def end_of_rounds():
        print("Fin des rounds, vous pouvez maintenant terminer le tournoi")
