import unittest
from Maze.maze import Maze

class TestMaze(unittest.TestCase):
    
    def test_maze_class_graph_existence(self):
        m = Maze()
        self.assertTrue(hasattr(m, 'graph'))

    def test_maze_class_graph_init_value(self):
        m = Maze()
        self.assertDictEqual(m.graph, {})

    def test_maze_class_fromJson_method_existence(self):
        m = Maze()
        self.assertTrue(hasattr(m, 'fromJson'))

    def test_maze_class_fromJson_method_with_map_1(self):
        test_graph = {
            1 : [2],
            2 : [1, 3, 4],
            3 : [2],
            4 : [2]
        }
        m = Maze()
        m.fromJson('json_files/map1.json')
        self.assertDictEqual(m.graph, test_graph)

    def test_maze_class_fromJson_method_with_map_2(self):
        test_graph = {
        1 : [2, 7],
        2 : [5, 1, 3, 4],
        3 : [2],
        4 : [6, 7, 2],
        5 : [2, 6],
        6 : [4, 5],
        7 : [4, 1]
        }
        m = Maze()
        m.fromJson('json_files/map2.json')
        self.assertDictEqual(m.graph, test_graph)

if __name__ == '__main__':
    unittest.main()