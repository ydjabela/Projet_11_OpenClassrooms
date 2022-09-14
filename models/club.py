from models.database import Database


class Club_model(Database):

    def __init__(self, name=None, email=None, points=None):
        self.name = name
        self.email = email
        self.points = points

    # -----------------------------------------------------------------------------------------------------------------#

    def load_club(self):
        return self.database_json(data="clubs")

