"""Définit un joueur"""


class ModelPlayer:
    def __init__(self, first_name="",
                 last_name="",
                 birthday="",
                 ID="",
                 score=0
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.ID = ID
        self.score = score

    def __str__(self):
        return (f"Nom : {self.last_name}\n Prénom : {self.first_name}\n"
                "Date de naissance : {self.birthday} \n"
                "ID Joueur : {self.ID} \n"
                "Score Global : {self.score}"
                )

