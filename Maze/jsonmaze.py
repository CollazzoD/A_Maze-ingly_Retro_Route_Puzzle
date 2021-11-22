from Maze.maze import Maze, InvalidMaze
import json

class JsonMaze(Maze):
    def __init__(self):
        self.graph = {}
        self.objects = {}
        self.names = {}
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
        objects = [object['name'] for object in room['objects']]
        return objects
    
    # Given a dictionary which represents the map: 
    # 1 - create the graph with an "Adjacency List" representation
    # 2 - create a room_id/object_list dictionary
    # 3 - create a room_id/name dictionary
    def _createGraph(self, map):
        for room in map['rooms']:
            neighbours = self._getRoomNeighbours(room)
            self.graph[room['id']] = neighbours

            object_list = self._getRoomObjects(room)
            self.objects[room['id']] = object_list

            self.names[room['id']] = room['name']
    
    # Collect objects in the room if present abd remove them if found
    def collectObjects(self, room, objects):
        ret = []
        for object in objects:
            if object in self.objects[room]:
                ret.append(object)
                self.objects[room].remove(object)
        return ret

    def _validateRooms(self, json_map):
        try:
            rooms = json_map['rooms']
            for room in json_map['rooms']:
                self._validateRoom(room)
        except KeyError as err:
            raise(InvalidMaze(f"Map not well formatted -> {err}"))

    def _checkType(self, name, value, type):
        if not isinstance(value, type):
            raise(InvalidMaze(f"{name} shall be of type {type}"))

    def _validateRoom(self, room):
        try:
            self._checkType("room['id']", room['id'], int)
            self._checkType("room['name']", room['name'], str)

            # Check neighbours type
            for cardinal in self._cardinals:
                if cardinal in room:
                    self._checkType(f"room['{cardinal}']", room[cardinal], int)
            
            # Check objects type
            self._checkType("room['objects'", room['objects'], list)
            for object in room['objects']:
                self._checkType(f"room['objects'][{object['name']}]", object['name'], str)
        
        except KeyError as err:
            raise(InvalidMaze(f"Map not well formatted -> {err}"))
        except TypeError as err:
            raise(InvalidMaze(f"Map not well formatted -> {err}"))
                
            
    def _validateJson(self, json_map):
        self._validateRooms(json_map)
        
    # Load the map from a json file
    def fromFile(self, json_filename):
        try:
            with open(json_filename) as json_file:
                json_map = json.loads(json_file.read())
                self._validateJson(json_map)
                self._createGraph(json_map)
        except json.decoder.JSONDecodeError as err:
            raise(InvalidMaze("Not a valid json"))
        