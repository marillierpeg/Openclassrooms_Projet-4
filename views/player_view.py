class ViewPlayer:
    """récupération des informations du joueur"""
    def __init__(self):
        pass

    def first_name(self):
        self.first_name = input("Prénom du joueur?")
        return self.first_name

    def last_name(self):
        self.last_name = input("Nom de famille du joueur?")
        return self.last_name

    def date_of_birth(self):
        self.date_of_birth = input(
            "Date de naissance du joueur? (format attendu : jj/mm/aaaa)"
            )
        # verifier le format
        return self.date_of_birth

    def ID(self):
        self.ID = input("Identifiant du joueur? (format attendu : AB12345)")
        # verifier le format
        return self.ID
