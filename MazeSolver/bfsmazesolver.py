from MazeSolver.mazesolver import MazeSolver

class BFSMazeSolver(MazeSolver):
    def __init__(self):
        self.output = []

    def solve(self, map, starting_room, objects_to_collect):
        pass

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