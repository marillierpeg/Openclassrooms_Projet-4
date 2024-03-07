class Tournament_View:
    def tournament_menu():
        """affiche menu tournois"""
        print("Menu Tournois")
        print("1 : Commencer un tournoi")
        print("2 : Terminer un tournoi")
        print("3 : Retour au menu principal")
        tournament_choice = input(
            "Saisir le numéro du menu auquel vous souhaiter accéder : "
        )
        return tournament_choice

    def new_tournament_name():
        """récupère le nom du tournoi"""
        tournament_name = input("quel est le nom de ce tournoi?")
        return tournament_name

    def new_tournament_place():
        """récupère le lieu du tournoi"""
        tournament_place = input("A quel endroit à lieu ce tournoi?")
        return tournament_place

    def new_tournament_rounds():
        """récupère le nombre de rounds du tournoi"""
        number_of_rounds = input(
            "Combien de rounds comptera ce tournoi? (par défaut 4)")
        if number_of_rounds == "":
            number_of_rounds = 4
        return number_of_rounds

    def new_tournament_description():
        """récupère l'éventuelle description liée au tournoi"""
        description = input("description/commentaire à propos de ce tournoi?")
        return description

    def number_of_players():
        """choix du nombre de joueurs que comptera le tournoi"""
        number_of_players = int(input(
            "combien de joueurs seront inscrits à ce tournoi?"
            ))
        while True:
            if (number_of_players % 2) == 0:
                return number_of_players
            else:
                print("merci d'entrer un nombre pair de joueurs : ")
                number_of_players = int(input())

    def add_players(players_list, player):
        """choix des joueurs à inscrire au tournoi"""
        number_of_players = len(players_list)
        add_player = input(
            f"{player} \n Voulez-vous ajouter ce joueur au tournoi : oui/non?"
            )
        if add_player == "oui":
            players_list.append(dict((x, y) for x, y in player))
            number_of_players += 1
        elif add_player == "non":
            pass
        else:
            print("merci de répondre par 'oui' ou 'non' uniquement")
        return players_list

    def closed_or_current_tournament():
        """choix d'un tournoi en cours ou terminé"""
        print("le tournoi que vous voulez afficher est-il :")
        print("1. En cours")
        print("2. Terminé")
        choice = input("Merci de saisir '1' ou '2' :  ")
        return choice

    def display_tournaments(tournaments_names):
        """choix d'"un tournoi"""
        for number, tournaments_names in enumerate(tournaments_names, start=1):
            print(f"{number} : {tournaments_names}")
        closed_choice = input(
            "Quel est le nom de tournoi dont"
            "vous souhaitez voir les détails? \n"
        )
        return closed_choice

    def no_current_tournament():
        print("pas de tournoi en cours actuellement")

    def no_tournament():
        print("Ce tournoi n'existe pas.")
