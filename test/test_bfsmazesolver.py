import unittest
from MazeSolver.bfsmazesolver import BFSMazeSolver

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

if __name__ == '__main__':
    unittest.main()