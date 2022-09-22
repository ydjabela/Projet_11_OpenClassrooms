from models.competitions import Competitions_model
import json


class Competitions(Competitions_model):

    def loadCompetitions(self):

        json_file = "competitions"
        competitions_list = []
        with open("{}".format(json_file) + ".json") as c:
            competitions = json.load(c)[json_file]
            for competition in competitions:
                competitions_list.append(Competitions_model(
                    name=competition['name'],
                    date=competition['date'],
                    numberOfPlaces=competition['numberOfPlaces']
                ).__dict__)
        return competitions_list

        # -----------------------------------------------------------------------------------------------------------------#

