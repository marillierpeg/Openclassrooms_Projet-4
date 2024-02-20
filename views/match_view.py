class Match_View:

    def match_menu():
        """affiche menu match"""
        print("Menu Match")
        print("1 : Enregistrer les scores des matchs")
        print("2 : Retour au menu principal")
        match_choice = input(
            "Saisir le numéro du menu auquel vous souhaiter accéder : "
        )
        return match_choice

    def first_player(player, pions):
        print(f"{player} jouera avec les pions {pions}")
