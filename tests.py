import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_two(self):
        num_cols = 4
        num_rows = 3
        m2 = Maze(400, 300, num_rows, num_cols, 20, 20)
        self.assertEqual(
            len(m2._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._Maze__cells[0]),
            num_rows,
        )
    
    def test_broken_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        entrance_has_top = False
        exit_has_bottom = False
        m3 = Maze(100, 100, num_rows, num_cols, 25, 25)
        self.assertEqual(
            len(m3._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m3._Maze__cells[0]),
            num_rows,
        )
        self.assertEqual(
            m3._Maze__cells[0][0].has_top_wall,
            entrance_has_top,
        )
        self.assertEqual(
            m3._Maze__cells[4][4].has_bottom_wall,
            exit_has_bottom,
        )

    def test_reset_visited(self):
        num_cols = 3
        num_rows = 3
        m4 = Maze(0, 0, num_rows, num_cols, 50, 50)
        self.assertEqual(
            len(m4._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m4._Maze__cells[0]),
            num_rows,
        )
        for col in m4._Maze__cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )

if __name__ == "__main__":
    unittest.main()