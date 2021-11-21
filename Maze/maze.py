import json
import logging

class Maze():
    def __init__(self):
        self.graph = {}
        self._cardinals = ['north', 'south', 'west', 'east']

    # Given a dictionary which represents a room, return a list of neighbours
    def _getNeighbours(self, room):
        neighbours = []
        for cardinal in self._cardinals:
            if cardinal in room:
                neighbours.append(room[cardinal])
        return neighbours

    # Given a dictionary which represents the map, create the graph
    # with an "Adjacency List" representation
    def _createGraph(self, map):
        for room in map['rooms']:
            neighbours = self._getNeighbours(room)
            self.graph[room['id']] = neighbours

    # Given a dictionary which represents the map, create the whole Maze
    def _createMaze(self, map):
        self._createGraph(map)

    # Load the map from a json file
    def fromJson(self, json_filename):
        with open(json_filename) as json_file:
            json_map = json.loads(json_file.read())
            self._createMaze(json_map)
            