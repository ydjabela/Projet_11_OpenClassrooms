from ..models.club import Club_model
import json

# ---------------------------------------------------------------------------------------------------------------------#


class Club(Club_model):

    def load_clubs(self):
        json_file = "clubs"
        clubs_list = list()
        with open("{}".format(json_file) + ".json") as c:
            clubs = json.load(c)[json_file]
            for club in clubs:
                clubs_list.append(Club_model(
                    name=club['name'],
                    email=club['email'],
                    points=club['points']
                ).__dict__)
        return clubs_list

    # -----------------------------------------------------------------------------------------------------------------#

    def load_clubs_by_name(self, club_name):
        clubs = self.load_clubs()
        try:
            foundClub = [c for c in clubs if c['name'] == club_name][0]
            return foundClub
        except IndexError:
                return None

    # -----------------------------------------------------------------------------------------------------------------#

    def load_clubs_by_email(self, club_email):
        clubs = self.load_clubs()
        try:
            foundClub = [c for c in clubs if c['email'] == club_email][0]
            return foundClub
        except IndexError:
            return None

    # -----------------------------------------------------------------------------------------------------------------#
