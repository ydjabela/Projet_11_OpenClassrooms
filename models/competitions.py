from model.datbase import Database


class Competitions_model(Database):

    def __init__(self, name=None, date=None, numberOfPlaces=None):
        self.name = name
        self.date = date
        self.numberOfPlaces = numberOfPlaces

    # -----------------------------------------------------------------------------------------------------------------#

    def load_competitions(self):
        return self.database_competitions()

