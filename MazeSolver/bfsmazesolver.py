from MazeSolver.mazesolver import MazeSolver

class BFSMazeSolver(MazeSolver):
    def __init__(self):
        self.output = []

    # Navigate a room, collecting objects while passing and updating the maze
    # If an object is found, it is deleted from 'objects_to_collect'
    def _navigateRoom(self, maze, room, objects_to_collect):
        collected = maze.collectObjects(room, objects_to_collect)
        self.output.append([room, collected])
        for object in collected:
            objects_to_collect.remove(object)

    # Check if all objects_to_collect are in the maze
    # If not, there's not a possible solution
    def _checkIfAllObjects(self, maze, objects_to_collect):
        maze_objects = [object for sublist in maze.objects.values() for object in sublist]
        for to_collect in objects_to_collect:
            if to_collect not in maze_objects:
                return False
        return True

    # Try to solve the maze
    def solve(self, maze, starting_room, objects_to_collect):
        # If I don't have any object to collect, I don't have a solution
        if not objects_to_collect:
            return False

        # If I have to search for non existent objects, I can't have a solution
        if not self._checkIfAllObjects(maze, objects_to_collect):
            return False

        # Get a possible path to navigate all the maze
        path = self._BFS(maze.graph, starting_room)

        # First room
        self._navigateRoom(maze, starting_room, objects_to_collect)

        # Navigate the maze according to path
        for index in range(len(path) - 1):
            navigation = self._BFS_SP(maze.graph, path[index], path[index + 1])[1:]
            for room in navigation:
                self._navigateRoom(maze, room, objects_to_collect)
                # In this case, I can stop looking in the maze
                if not objects_to_collect:
                    return True

        # If for some reason I'm here, there's no possible solution
        return False

    # BFS implementation from Wikipedia pseudocode
    # https://en.wikipedia.org/wiki/Breadth-first_search
    def _BFS(self, graph, start):
        queue = []
        visited = []
        path = []
        
        visited.append(start)
        queue.append(start)

        while queue:
            v = queue.pop(0) 
            path.append(v)

            for neighbour in graph[v]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return path

    # BFS which gives shortest path from start to stop
    def _BFS_SP(self, graph, start, stop):
        queue = []
        visited = []
        parents = {}
        
        visited.append(start)
        queue.append(start)

        while queue:
            v = queue.pop(0) 

            if v == stop:
                return parents[stop] + [stop]

            for neighbour in graph[v]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    p = parents.get(v, [])
                    parents[neighbour] = p + [v]

        return []