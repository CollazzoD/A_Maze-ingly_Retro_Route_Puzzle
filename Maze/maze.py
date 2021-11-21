import json
import logging

class Maze():
    def __init__(self):
        self.graph = {}
        self.objects = {}
        self._cardinals = ['north', 'south', 'west', 'east']

    # Given a dictionary which represents a room, return a list of room's neighbours
    def _getRoomNeighbours(self, room):
        neighbours = []
        for cardinal in self._cardinals:
            if cardinal in room:
                neighbours.append(room[cardinal])
        return neighbours

    # Given a dictionary which represents a room, return a list of room's objects 
    def _getRoomObjects(self, room):
        objects = room['objects']
        return objects
    
    # Given a dictionary which represents the map, create the graph
    # with an "Adjacency List" representation
    def _createGraph(self, map):
        for room in map['rooms']:
            neighbours = self._getRoomNeighbours(room)
            self.graph[room['id']] = neighbours

            object_list = self._getRoomObjects(room)

    # Given a dictionary which represents the map, create the whole Maze
    def _createMaze(self, map):
        self._createGraph(map)

    # Load the map from a json file
    def fromJson(self, json_filename):
        with open(json_filename) as json_file:
            json_map = json.loads(json_file.read())
            self._createMaze(json_map)
            