import unittest
from MazeSolver.bfsmazesolver import BFSMazeSolver
from Maze.jsonmaze import JsonMaze

class TestBFSMazeSolver(unittest.TestCase):
    
    def test_BFSMazeSolver_class_output_existence(self):
        b = BFSMazeSolver()
        self.assertTrue(hasattr(b, 'output'))

    def test_BFSMazeSolver_class_output_init_value(self):
        b = BFSMazeSolver()
        self.assertListEqual(b.output, [])

    def test_BFSMazeSolver_class__BFS_with_map_1(self):
        test_graph = {
            1 : [2],
            2 : [1, 3, 4],
            3 : [2],
            4 : [2]
        }

        b = BFSMazeSolver()
        output = b._BFS(test_graph, 1)
        self.assertListEqual(output, [1, 2, 3, 4])

        output = b._BFS(test_graph, 2)
        self.assertListEqual(output, [2, 1, 3, 4])

    def test_BFSMazeSolver_class__BFS_with_map_2(self):
        test_graph = {
            1 : [2, 7],
            2 : [5, 1, 3, 4],
            3 : [2],
            4 : [6, 7, 2],
            5 : [2, 6],
            6 : [4, 5],
            7 : [4, 1]
        }

        b = BFSMazeSolver()
        output = b._BFS(test_graph, 4)
        self.assertListEqual(output, [4, 6, 7, 2, 5, 1, 3])

    def test_BFSMazeSolver_class__BFS_SP_with_map_1(self):
        test_graph = {
            1 : [2],
            2 : [1, 3, 4],
            3 : [2],
            4 : [2]
        }

        b = BFSMazeSolver()
        output = b._BFS_SP(test_graph, 1, 2)
        self.assertListEqual(output, [1, 2])

        output = b._BFS_SP(test_graph, 1, 3)
        self.assertListEqual(output, [1, 2, 3])

        output = b._BFS_SP(test_graph, 1, 4)
        self.assertListEqual(output, [1, 2, 4])

    def test_BFSMazeSolver_class__BFS_SP_with_map_2(self):
        test_graph = {
            1 : [2, 7],
            2 : [5, 1, 3, 4],
            3 : [2],
            4 : [6, 7, 2],
            5 : [2, 6],
            6 : [4, 5],
            7 : [4, 1]
        }

        b = BFSMazeSolver()
        output = b._BFS_SP(test_graph, 4, 3)
        self.assertListEqual(output, [4, 2, 3])

        output = b._BFS_SP(test_graph, 7, 2)
        self.assertListEqual(output, [7, 4, 2])

        output = b._BFS_SP(test_graph, 6, 1)
        self.assertListEqual(output, [6, 4, 7, 1])

    def test_BFSMazeSolver_class__navigateRoom(self):
        m = JsonMaze()
        m.fromFile("json_files/map1.json")

        b = BFSMazeSolver()

        b._navigateRoom(m, 2, [])
        self.assertListEqual(b.output, [[2, []]])

        b._navigateRoom(m, 3, [])
        self.assertListEqual(b.output, [[2, []], [3, []]])

        b._navigateRoom(m, 4, ['Potted Plant'])
        self.assertListEqual(b.output, [[2, []], [3, []], [4, ['Potted Plant']]])

        
    def test_BFSMazeSolver_class_solve_with_map_1(self):
        m = JsonMaze()
        m.fromFile("json_files/map1.json")

        expected_output = [ [2, []],
                            [1, []],
                            [2, []],
                            [3, ['Knife']],
                            [2, []],
                            [4, ['Potted Plant']]]
        b = BFSMazeSolver()
        solved = b.solve(m, 2, ['Knife', 'Potted Plant'])
        self.assertTrue(solved)
        self.assertListEqual(b.output, expected_output)

    def test_BFSMazeSolver_class__checkIfAllObjects_with_map_1(self):
        m = JsonMaze()
        m.fromFile("json_files/map1.json")

        objects_to_collect = ['Vibranium']
        b = BFSMazeSolver()
        self.assertFalse(b._checkIfAllObjects(m, objects_to_collect))

        objects_to_collect = ['Knife']
        self.assertTrue(b._checkIfAllObjects(m, objects_to_collect))

    def test_BFSMazeSolver_class_solve_with_map_2(self):
        m = JsonMaze()
        m.fromFile("json_files/map2.json")

        expected_output = [ [4, []],
                            [6, []],
                            [4, []],
                            [7, ['Potted Plant']],
                            [4, []],
                            [2, []],
                            [5, ['Pillow']],
                            [2, []],
                            [1, []],
                            [2, []],
                            [3, ['Knife']]]
        b = BFSMazeSolver()
        solved = b.solve(m, 4, ['Knife', 'Potted Plant', 'Pillow'])
        self.assertTrue(solved)
        self.assertListEqual(b.output, expected_output)
    
    def test_BFSMazeSolver_class_solve_with_map_2_early_stop(self):
        m = JsonMaze()
        m.fromFile("json_files/map2.json")

        expected_output = [ [4, []],
                            [6, []],
                            [4, []],
                            [7, ['Potted Plant']],
                            [4, []],
                            [2, []],
                            [5, ['Pillow']]]
        b = BFSMazeSolver()
        solved = b.solve(m, 4, ['Potted Plant', 'Pillow'])
        self.assertTrue(solved)
        self.assertListEqual(b.output, expected_output)

    def test_BFSMazeSolver_class_solve_with_map_3_multiple_objects_in_same_room(self):
        m = JsonMaze()
        m.fromFile("json_files/map3.json")

        expected_output = [ [1, ['Keys', 'Phone']]]
        b = BFSMazeSolver()
        solved = b.solve(m, 1, ['Keys', 'Phone'])
        self.assertTrue(solved)
        self.assertListEqual(b.output, expected_output)

    def test_BFSMazeSolver_class_solve_with_map_not_connected(self):
        m = JsonMaze()
        m.fromFile("json_files/map_not_connected.json")

        b = BFSMazeSolver()
        solved = b.solve(m, 1, ['Knife'])
        self.assertFalse(solved)

        solved = b.solve(m, 3, ['Knife'])
        self.assertTrue(solved)

if __name__ == '__main__':
    unittest.main()