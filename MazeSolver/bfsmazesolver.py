from MazeSolver.mazesolver import MazeSolver

class BFSMazeSolver(MazeSolver):
    def __init__(self):
        self.output = []

    def solve(self, map, starting_room, objects_to_collect):
        pass

    # BFS implementation from Wikipedia pseudocode
    def _BFS(self, graph, starting_node):
        queue = []
        visited = []
        path = []
        
        visited.append(starting_node)
        queue.append(starting_node)

        while queue:
            s = queue.pop(0) 
            path.append(s)

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return path