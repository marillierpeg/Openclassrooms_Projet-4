import datetime
import re


class ViewPlayer:
    """affiche le menu joueurs"""
    def display_players_menu():
        print("Menu Joueurs :")
        print("1 : Inscrire un joueur")
        print("2 : afficher la liste de tous les joueurs")
        print("3 : retour au menu principal")
        player_choice = input(
            "Saisir le numéro du menu auquel vous souhaiter accéder :"
            )
        return player_choice

    """récupération des informations du joueur"""
    def first_name():
        first_name = input("Prénom du joueur?")
        return first_name
    
    def last_name():
        last_name = input("Nom de famille du joueur?")
        return last_name

    def date_of_birth():
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
        while True:
            ID = input("Identifiant du joueur? (format attendu : AB12345)")
            if re.match(r'[a-zA-Z]{2}[0-9]{5}$', ID):
                return ID
            else:
                print("ID non valide")
