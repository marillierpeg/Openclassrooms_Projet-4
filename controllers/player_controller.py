from views.player_view import ViewPlayer


class ControllerPlayer:

    def create_player(self):
        first_name = ViewPlayer.first_name()
        last_name = ViewPlayer.last_name()
        date_of_birth = ViewPlayer.date_of_birth()
        ID_joueur = ViewPlayer.ID()
        return first_name, last_name, date_of_birth, ID_joueur

    def __str__(self):
        return f"prénom : {self.first_name}, nom : {self.last_name}"
