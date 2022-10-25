from ..models.competitions import Competitions_model
import json


class Competitions(Competitions_model):

    def load_competition(self):
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

    def load_competition_by_name(self, competition_name):
        competitions = self.load_competition()
        try:
            foundCompetition = [c for c in competitions if c['name'] == competition_name][0]
            return foundCompetition
        except (TypeError, IndexError) as e:
            return None

    # -----------------------------------------------------------------------------------------------------------------#
