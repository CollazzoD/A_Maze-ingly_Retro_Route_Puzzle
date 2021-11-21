import unittest
from Maze.maze import Maze

class TestMaze(unittest.TestCase):
    
    def test_maze_class_graph_existence(self):
        m = Maze()
        self.assertTrue(hasattr(m, 'graph'))

    def test_maze_class_graph_init_value(self):
        m = Maze()
        self.assertIsNone(m.graph)

if __name__ == '__main__':
    unittest.main()