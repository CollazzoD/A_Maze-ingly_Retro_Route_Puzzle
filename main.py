import sys
from Maze.maze import InvalidMaze
from Maze.jsonmaze import JsonMaze
from MazeSolver.bfsmazesolver import BFSMazeSolver
from tabulate import tabulate 

def pretty_printer(maze, maze_solver):
    header = ['ID', 'Room', 'Object collected']
    table = []
    for el in maze_solver.output:
        t = []
        t.append(el[0])
        t.append(maze.names[el[0]])
        if el[1]:
            t.append(','.join(el[1]))
        else:
            t.append('None')
        table.append(t)
    print(tabulate(table, headers=header))

if __name__ == "__main__":
    if (len(sys.argv) < 4):
        print('Expected parameters: json_filename (e.g. "json_files/map1.json") starting_room (e.g. 1) list_of_objects (separated by space; e.g. "Knife" "Potted Plant")')
        exit(0)

    json_filename = sys.argv[1]

    try:
        starting_room = int(sys.argv[2])
    except ValueError as err:
        print("Starting room must be an integer")
        exit(1)

    list_of_objects = [obj for obj in sys.argv[3:]]

    print("#################################")
    print(f"Map : {json_filename}")
    print(f"Starting room : {starting_room}")
    print(f"List of objects : {list_of_objects}")

    try:
        maze = JsonMaze()
        maze.fromFile(json_filename)

        maze_solver = BFSMazeSolver()
        solved = maze_solver.solve(maze, starting_room, list_of_objects)
    
        if solved:
            pretty_printer(maze, maze_solver)
        else:
            print("It does not exist a possible solution")

    except FileNotFoundError as err:
        print(f"File {json_filename} was not found in the specified path -> {err}")
    except InvalidMaze as err:
        print(f"Invalid Maze -> {err}")
    
    print("#################################")