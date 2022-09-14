from models.competitions import Competitions_model


class Competitions(Competitions_model):

    def loadCompetitions(self):
        return self.load_competitions()
