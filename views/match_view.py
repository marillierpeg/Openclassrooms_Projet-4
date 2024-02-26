class Match_View:

    def match_menu():
        """affiche le menu match"""
        print("Menu Match")
        print("1 : Enregistrer les scores des matchs")
        print("2 : Retour au menu principal")
        match_choice = input("Saisir le numéro du menu auquel vous souhaiter accéder : ")
        return match_choice

    def first_player(first_name, last_name, id, pawn_color):
        """affiche quel joueur jouera avec quels pions"""
        print(f"{first_name} {last_name} ID:{id} jouera avec les pions {pawn_color}")
