from models.club import Club_model


class Club(Club_model):
    def loadClubs(self):
        return self.load_club()

