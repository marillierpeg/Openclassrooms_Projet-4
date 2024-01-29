"""Définit un joueur"""


class ModelPlayer:
    def __init__(self, first_name="",
                 last_name="",
                 date_of_birth="",
                 ID="",
                 current_score=0
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.ID = ID
        self.current_score = current_score

    def __str__(self):
        return f"Nom : {self.last_name} Prénom : {self.first_name}\
        Date de naissance : {self.date_of_birth}\
        ID Joueur : {self.ID} Score Global : {self.current_score}"

    def __repr__(self):
        return f"Nom : {self.last_name} Prénom : {self.first_name}\
        Date de naissance : {self.date_of_birth}\
        ID Joueur : {self.ID} Score Global : {self.current_score}"
