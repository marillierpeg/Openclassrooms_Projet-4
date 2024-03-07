class Match_View:

    def first_player(first_name, last_name, id, pawn_color):
        """affiche quel joueur jouera avec quels pions"""
        print(f"{first_name} {last_name} ID:{id} jouera avec les pions {pawn_color}")

    def scores():
        choice = input("Mettre à jour les scores de ce match? oui/non? ")
        return choice

    def match_list(match_list):
        print("Voici la liste des matchs de ce tour :")
        print(match_list)
