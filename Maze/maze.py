import json
import logging

class Maze():
    def __init__(self):
        self.graph = {}
        self.cardinals = ['north', 'south', 'west', 'east']

    def fromJson(self, json_filename):
        with open(json_filename) as json_file:
            json_map = json.loads(json_file.read())
            for room in json_map['rooms']:
                neighbours = []
                for cardinal in self.cardinals:
                    if cardinal in room:
                        neighbours.append(room[cardinal])
                self.graph[room['id']] = neighbours