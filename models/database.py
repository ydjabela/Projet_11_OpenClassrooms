import json


class Database:

    def database_json(self, data):
        with open("{}".format(data)+".json") as c:
            return json.load(c)[data]
