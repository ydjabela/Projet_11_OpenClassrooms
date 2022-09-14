import json


class Competitions:

    def loadCompetitions(self):
        with open('competitions.json') as comps:
             listOfCompetitions = json.load(comps)['competitions']
             return listOfCompetitions
