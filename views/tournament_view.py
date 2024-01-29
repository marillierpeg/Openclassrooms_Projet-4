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

    def new_tournament_description():
        description = input("description/commentaire à propos de ce tournoi?")
        return description

    def number_of_players():
        """choix des joueurs à ajouter au tournoi"""
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

    def add_players(players_list, player):
        add_player = input(
            f"{player} \n Voulez-vous ajouter ce joueur au tournoi : oui/non?"
            )
        if add_player == "oui":
            players_list.append(dict((x, y) for x, y in player))
        elif add_player == "non":
            pass
        else:
            print("merci de répondre par 'oui' ou 'non' uniquement")
        return players_list

    def display_tournament_players(name_place):
        for number, name_place in enumerate(name_place, start=1):
            print(f"{number} : Tournoi '{name_place[0]}' ayant "
                  f"eu lieu à {name_place[1]}")
        choice = input("saisir le nom du tournoi dont "
                       "vous voulez afficher les joueurs : "
                       )
        return choice

    def closed_or_current_tournament():
        print("le tournoi que vous voulez afficher est-il :")
        print("1. En cours")
        print("2. Terminé")
        choice = input("Merci de saisir '1' ou '2' :  ")
        return choice

    def display_tournaments(tournaments_names):
        for number, tournaments_names in enumerate(tournaments_names, start=1):
            print(f"{number} : {tournaments_names}")
        closed_choice = input(
            "Quel est le nom de tournoi dont"
            "vous souhaitez voir les détails? \n"
        )
        return closed_choice
