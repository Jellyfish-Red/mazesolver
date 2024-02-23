import unittest
from interface import Window, Point
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells_matrix(self):
        num_rows = 10
        num_columns = 12

        m1 = Maze(0, 0, num_rows, num_columns, 10, 10)
        self.__verify_maze_matrix(m1, num_rows, num_columns, 0, 0, 10, 10)

        num_rows = 10
        num_columns = 10
        m2 = Maze(0, 0, num_rows, num_columns, 10, 10)
        self.__verify_maze_matrix(m2, num_rows, num_columns, 0, 0, 10, 10)

        num_rows = 1000
        num_columns = 1000
        m3 = Maze(0, 0, num_rows, num_columns, 10, 10)
        self.__verify_maze_matrix(m3, num_rows, num_columns)

    def __verify_maze_matrix(self, maze, expected_rows, expected_columns, 
                             start_x, start_y, cell_size_x, cell_size_y):
        self.assertEqual(
            len(maze.cells),
            expected_columns,
            msg = "Verify number of columns is correct"
        )
        self.assertEqual(
            len(maze.cells[0]),
            expected_rows,
            msg = "Verify number of rows is correct"
        )

        for i in range(expected_columns):
            for j in range(expected_rows):
                expected_p1 = Point(start_x + (i * cell_size_x),
                                    start_y + (j * cell_size_y))
                # print("Verifying positon [" + str(i) + "][" + str(j) + "]")
                self.assertEqual(
                    maze.cells[i][j].p1.x,
                    expected_p1.x,
                    msg = "p1.x of matrix position cells[" + str(i) + "][" + str(j) + "]"
                )
                self.assertEqual(
                    maze.cells[i][j].p1.y,
                    expected_p1.y,
                    msg = "p1.y of matrix position cells[" + str(i) + "][" + str(j) + "]"
                )

    def test_maze_draw_cells(self):
        num_rows = 10
        num_columns = 12
        w1 = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_columns, 20, 20, parent = w1)
        self.__verify_maze_matrix(m1, num_rows, num_columns, 0, 0, 20, 20)


if __name__ == '__main__':
    unittest.main()