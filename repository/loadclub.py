import json


class Club:
    def loadClubs(self):
        with open('clubs.json') as c:
             listOfClubs = json.load(c)['clubs']
             return listOfClubs
