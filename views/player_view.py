import datetime
import re


class ViewPlayer:
    """affiche le menu joueurs"""
    def display_players_menu():
        print("Menu Joueurs :")
        print("1 : Inscrire un joueur")
        print("2 : Afficher la liste de tous les joueurs")
        print("3 : Retour au menu principal")
        player_choice = input(
            "Saisir le numéro du menu auquel vous souhaiter accéder :"
            )
        return player_choice

    def players_max():
        print("nombre maximum de joueurs atteint")

    def first_name():
        """récupération du prénom du joueur"""
        first_name = input("Prénom du joueur?")
        return first_name

    def last_name():
        """récupération du nom du joueur"""
        last_name = input("Nom de famille du joueur?")
        return last_name

    def date_of_birth():
        """récupération de la date de naissance du joueur"""
        while True:
            format_date = "%d-%m-%Y"
            date_of_birth = input(
                "Date de naissance du joueur? (format attendu : jj-mm-aaaa)"
                )
            try:
                datetime.datetime.strptime(date_of_birth, format_date)
                return date_of_birth
            except ValueError:
                print("merci d'entrer une date valide")

    def ID():
        """récupération de l'ID du joueur"""
        while True:
            ID = input("Identifiant du joueur? (format attendu : AB12345)")
            if re.match(r'[a-zA-Z]{2}[0-9]{5}$', ID):
                return ID
            else:
                print("ID non valide")
