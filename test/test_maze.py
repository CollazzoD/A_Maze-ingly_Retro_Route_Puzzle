import unittest
import Maze.maze as Maze

class TestMaze(unittest.TestCase):
    
    def test_maze_class_existence(self):
        self.assertTrue(hasattr(Maze, 'Maze'), "Class Maze not found")

if __name__ == '__main__':
    unittest.main()