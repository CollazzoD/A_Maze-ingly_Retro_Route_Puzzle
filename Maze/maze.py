from abc import ABC, abstractmethod

class Maze(ABC):
    @abstractmethod
    # Method that open a file type representing a map and convert it into a Maze
    def fromFile(self, filename):
        pass

    @abstractmethod
    # Collect objects in the room if present and remove them if found
    def collectObjects(self, room, objects):
        pass