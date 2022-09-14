from models.database import Database


# ---------------------------------------------------------------------------------------------------------------------#
class Competitions_model(Database):

    def __init__(self, name=None, date=None, numberOfPlaces=None):
        self.name = name
        self.date = date
        self.numberOfPlaces = numberOfPlaces

    # -----------------------------------------------------------------------------------------------------------------#

    def load_competitions(self):
        return self.database_json(data="competitions")

    # -----------------------------------------------------------------------------------------------------------------#

    def load_competitions_by_name(self):
        list_compe = self.database_json(data="competitions")
        print(list_compe)

    # -----------------------------------------------------------------------------------------------------------------#
