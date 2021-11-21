from abc import ABC, abstractmethod

class Maze(ABC):
    @abstractmethod
    def fromFile(self, json_filename):
        pass

    @abstractmethod
    def collectObjects(self, room, objects):
        pass