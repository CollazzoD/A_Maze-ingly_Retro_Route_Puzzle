from MazeSolver.mazesolver import MazeSolver

class BFSMazeSolver(MazeSolver):
    def __init__(self):
        self.output = []

    # Navigate a room, collecting objects while passing and updating the maze
    def _navigateRoom(self, maze, room, objects_to_collect):
        collected = maze.collectObjects(room, objects_to_collect)
        self.output.append([room, collected])
        for object in collected:
            objects_to_collect.remove(object)

    def solve(self, maze, starting_room, objects_to_collect):
        # Get a path to navigate all the maze
        path = self._BFS(maze.graph, starting_room)

        # First room
        self._navigateRoom(maze, starting_room, objects_to_collect)

        if not objects_to_collect:
            return

        # Navigate the maze according to path
        for index in range(len(path) - 1):
            navigation = self._BFS_SP(maze.graph, path[index], path[index + 1])[1:]
            for room in navigation:
                self._navigateRoom(maze, room, objects_to_collect)
                if not objects_to_collect:
                    return

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