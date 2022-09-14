import json


class Database:

    def database_club(self):
        with open('clubs.json') as c:
            listOfClubs = json.load(c)['clubs']
            return listOfClubs

    def database_competitions(self):
        with open('competitions.json') as comps:
            listOfCompetitions = json.load(comps)['competitions']
            return listOfCompetitions
