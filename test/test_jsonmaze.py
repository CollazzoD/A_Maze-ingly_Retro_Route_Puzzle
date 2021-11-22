import unittest
from Maze.jsonmaze import JsonMaze
from Maze.maze import InvalidMaze

class TestMaze(unittest.TestCase):
    
    def test_maze_class_graph_existence(self):
        m = JsonMaze()
        self.assertTrue(hasattr(m, 'graph'))

    def test_maze_class_objects_existence(self):
        m = JsonMaze()
        self.assertTrue(hasattr(m, 'objects'))

    def test_maze_class_names_existence(self):
        m = JsonMaze()
        self.assertTrue(hasattr(m, 'names'))

    def test_maze_class_cardinal_existence(self):
        m = JsonMaze()
        self.assertTrue(hasattr(m, '_cardinals'))

    def test_maze_class_objects_init_value(self):
        m = JsonMaze()
        self.assertDictEqual(m.objects, {})

    def test_maze_class_graph_init_value(self):
        m = JsonMaze()
        self.assertDictEqual(m.graph, {})

    def test_maze_class_names_init_value(self):
        m = JsonMaze()
        self.assertDictEqual(m.names, {})

    # For this solution I'm forcing the cardinals to be in this exact order
    def test_maze_class__cardinals_init_value(self):
        m = JsonMaze()
        self.assertListEqual(m._cardinals, ['north', 'south', 'west', 'east'])


    def test_maze_class__getRoomNeighbours(self):
        m = JsonMaze()
        room = {'id': 1, 'north' : 2, 'west' : 3, 'east' : 4}
        self.assertListEqual(m._getRoomNeighbours(room), [2, 3, 4])

        room = {'id': 1, 'west' : 2, 'north' : 3, 'east' : 4}
        self.assertListEqual(m._getRoomNeighbours(room), [3, 2, 4])

        room = {'id': 1, 'west' : 3, 'south' : 2, 'north' : 1, 'east' : 4}
        self.assertListEqual(m._getRoomNeighbours(room), [1, 2, 3, 4])

    def test_maze_class__getRoomObjects(self):
        m = JsonMaze()

        objects_in = []
        objects_out = []
        room = {'id': 1, 'objects': objects_in}
        self.assertListEqual(m._getRoomObjects(room), objects_out)

        objects_in = [{'name': 'Knife'}]
        objects_out = ['Knife']
        room = {'id': 1, 'objects': objects_in}
        self.assertListEqual(m._getRoomObjects(room), objects_out)

        objects_in = [{'name': 'Knife'}, {'name': 'Potted Plant'}]
        objects_out = ['Knife', 'Potted Plant']
        room = {'id': 1, 'objects': objects_in}
        self.assertListEqual(m._getRoomObjects(room), objects_out)

    def test_maze_class_createGraph_with_map_1(self):
        map_test = {'rooms': [{'id': 1, 'name': 'Hallway', 'north': 2, 'objects': []}, {'id': 2, 'name': 'Dining Room', 'south': 1, 'west': 3, 'east': 4, 'objects': []}, {'id': 3, 'name': 'Kitchen', 'east': 2, 'objects': [{'name': 'Knife'}]}, {'id': 4, 'name': 'Sun Room', 'west': 2, 'objects': [{'name': 'Potted Plant'}]}]}
        test_graph = {
            1 : [2],
            2 : [1, 3, 4],
            3 : [2],
            4 : [2]
        }
        m = JsonMaze()
        m._createGraph(map_test)
        self.assertDictEqual(m.graph, test_graph)

    def test_maze_class_createGraph_with_map_2(self):
        map_test = {'rooms': [{'id': 1, 'name': 'Hallway', 'north': 2, 'east': 7, 'objects': []}, {'id': 2, 'name': 'Dining Room', 'north': 5, 'south': 1, 'west': 3, 'east': 4, 'objects': []}, {'id': 3, 'name': 'Kitchen', 'east': 2, 'objects': [{'name': 'Knife'}]}, {'id': 4, 'name': 'Sun Room', 'west': 2, 'north': 6, 'south': 7, 'objects': []}, {'id': 5, 'name': 'Bedroom', 'south': 2, 'east': 6, 'objects': [{'name': 'Pillow'}]}, {'id': 6, 'name': 'Bathroom', 'west': 5, 'south': 4, 'objects': []}, {'id': 7, 'name': 'Living room', 'west': 1, 'north': 4, 'objects': [{'name': 'Potted Plant'}]}]}
        test_graph = {
            1 : [2, 7],
            2 : [5, 1, 3, 4],
            3 : [2],
            4 : [6, 7, 2],
            5 : [2, 6],
            6 : [4, 5],
            7 : [4, 1]
        }
        m = JsonMaze()
        m._createGraph(map_test)
        self.assertDictEqual(m.graph, test_graph)

    def test_maze_class_collectObjects_method_one_object(self):
        map_test = {'rooms': [{'id': 1, 'name': 'Hallway', 'north': 2, 'objects': []}, {'id': 2, 'name': 'Dining Room', 'south': 1, 'west': 3, 'east': 4, 'objects': []}, {'id': 3, 'name': 'Kitchen', 'east': 2, 'objects': [{'name': 'Knife'}]}, {'id': 4, 'name': 'Sun Room', 'west': 2, 'objects': [{'name': 'Potted Plant'}]}]}
        test_graph = {
            1 : [2],
            2 : [1, 3, 4],
            3 : [2],
            4 : [2]
        }
        m = JsonMaze()
        m._createGraph(map_test)
        ret = m.collectObjects(3, ['Potted Plant'])
        self.assertListEqual(ret, [])

        ret = m.collectObjects(3, ['Knife', 'Potted Plant'])
        self.assertListEqual(ret, ['Knife'])
        self.assertListEqual(m.objects[3], [])

    def test_maze_class_collectObjects_method_multiple_objects(self):
        map_test = {'rooms': [{'id': 1, 'name': 'Hallway', 'north': 2, 'objects': []}, {'id': 2, 'name': 'Dining Room', 'south': 1, 'west': 3, 'east': 4, 'objects': []}, {'id': 3, 'name': 'Kitchen', 'east': 2, 'objects': [{'name': 'Knife'}, {'name': 'Spoon'}]}, {'id': 4, 'name': 'Sun Room', 'west': 2, 'objects': [{'name': 'Potted Plant'}]}]}
        test_graph = {
            1 : [2],
            2 : [1, 3, 4],
            3 : [2],
            4 : [2]
        }
        m = JsonMaze()
        m._createGraph(map_test)
        ret = m.collectObjects(3, ['Knife', 'Spoon'])
        self.assertListEqual(ret, ['Knife', 'Spoon'])
        self.assertListEqual(m.objects[3], [])

    def test_maze_class__validateGraph_method(self):
        m = JsonMaze()
        
        test_graph = {
            1 : [2, 3, 4],
            2 : []
        }

        m.graph = test_graph
        self.assertRaises(InvalidMaze, m._validateGraph)

    def test_maze_class__checkIfNotEmpty_method(self):
        m = JsonMaze()
        self.assertRaises(InvalidMaze, m._checkIfNotEmpty)

    def test_maze_class_fromFile_method_with_map_1(self):
        test_graph = {
            1 : [2],
            2 : [1, 3, 4],
            3 : [2],
            4 : [2]
        }
        m = JsonMaze()
        m.fromFile('json_files/map1.json')
        self.assertDictEqual(m.graph, test_graph)

        test_objects = {
            1 : [],
            2 : [],
            3 : ['Knife'],
            4 : ['Potted Plant']
        }
        self.assertDictEqual(m.objects, test_objects)

        test_names = {
            1 : 'Hallway',
            2 : 'Dining Room',
            3 : 'Kitchen',
            4 : 'Sun Room'
        }
        self.assertDictEqual(m.names, test_names)

    def test_maze_class_fromFile_method_with_map_2(self):
        test_graph = {
            1 : [2, 7],
            2 : [5, 1, 3, 4],
            3 : [2],
            4 : [6, 7, 2],
            5 : [2, 6],
            6 : [4, 5],
            7 : [4, 1]
        }
        m = JsonMaze()
        m.fromFile('json_files/map2.json')
        self.assertDictEqual(m.graph, test_graph)

        test_objects = {
            1 : [],
            2 : [],
            3 : ['Knife'],
            4 : [],
            5 : ['Pillow'],
            6 : [],
            7 : ['Potted Plant']
        }
        self.assertDictEqual(m.objects, test_objects)

        test_names = {
            1 : 'Hallway',
            2 : 'Dining Room',
            3 : 'Kitchen',
            4 : 'Sun Room',
            5 : 'Bedroom',
            6 : 'Bathroom',
            7 : 'Living room'
        }
        self.assertDictEqual(m.names, test_names)

    def test_maze_class__checkType_method(self):
        m = JsonMaze()
        name = "room"
        value = 1
        type = str

        self.assertRaises(InvalidMaze, m._checkType, name, value, type)

    def test_maze_class__validateRoom_method(self):
        m = JsonMaze()

        room = {'id' : "1", 'name' : "Test", 'north' : 2, 'objects' : []}
        self.assertRaises(InvalidMaze, m._validateRoom, room)

        room = {'id' : 1, 'name' : 121, 'north' : 2, 'objects' : []}
        self.assertRaises(InvalidMaze, m._validateRoom, room)

        room = {'id' : 1, 'name' : "Test", 'north' : "2", 'objects' : []}
        self.assertRaises(InvalidMaze, m._validateRoom, room)

        room = {'id' : 1, 'name' : "Test", 'north' : 2, 'objects' : "Error"}
        self.assertRaises(InvalidMaze, m._validateRoom, room)

        room = {'id' : 1, 'name' : "Test", 'north' : 2, 'objects' : [1]}
        self.assertRaises(InvalidMaze, m._validateRoom, room)

        room = {'name' : "Test", 'north' : 2, 'objects' : [1]}
        self.assertRaises(InvalidMaze, m._validateRoom, room)

    def test_maze_class__validateRooms_method(self):
        m = JsonMaze()

        rooms= {'room' : [{'id' : 1, 'name' : "Test", 'north' : 2, 'objects' : []}]}
        self.assertRaises(InvalidMaze, m._validateRooms, rooms)

        rooms= {'rooms' : [{'id' : "1", 'name' : "Test", 'north' : 2, 'objects' : []}]}
        self.assertRaises(InvalidMaze, m._validateRooms, rooms)

if __name__ == '__main__':
    unittest.main()