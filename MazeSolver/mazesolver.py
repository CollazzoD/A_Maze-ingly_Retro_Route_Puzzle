from abc import ABC, abstractmethod

class MazeSolver(ABC):
    @abstractmethod
    def solve(self, map_filename, starting_room, objects_to_collect):
        pass