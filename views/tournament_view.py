class Tournament_View:
    def tournament_menu():
        """affiche menu tournois"""
        print("Menu Tournois")
        print("1 : Commencer un tournoi")
        print("2 : Afficher la liste des joueurs du tournoi")
        print("3 : Terminer un tournoi")
        print("4 : Retour au menu principal")
        tournament_choice = input(
            "Saisir le numéro du menu auquel vous souhaiter accéder :"
        )
        return tournament_choice

    def new_tournament_name():
        """récupère les informations liées au nouveau tournoi"""
        tournament_name = input("quel est le nom de ce tournoi?")
        return tournament_name

    def new_tournament_place():
        tournament_place = input("A quel endroit à lieu ce tournoi?")
        return tournament_place

    def new_tournament_rounds():
        number_of_rounds = input(
            "Combien de rounds comptera ce tournoi? (par défaut 4)")
        if number_of_rounds == "":
            number_of_rounds = 4
        return number_of_rounds

    def new_tournament_players():
        number_of_players = int(input(
            "combien de joueurs seront inscrits à ce tournoi?"
            ))
        if (number_of_players % 2) == 0:
            pass
        else:
            print("merci d'entrer un nombre pair de joueurs")
            number_of_players = int(
                input("combien de joueurs seront inscrits à ce tournoi?")
                   )
        return number_of_players

    def new_tournament_description():
        description = input("description/commentaire à propos de ce tournoi?")
        return description
