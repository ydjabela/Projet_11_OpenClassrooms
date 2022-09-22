from models.club import Club_model
import json

# ---------------------------------------------------------------------------------------------------------------------#


class Club(Club_model):
    def loadClubs(self):
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



