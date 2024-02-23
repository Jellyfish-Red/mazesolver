from interface import Window, Point, Line
from cell import Cell
from maze import Maze

def main() -> int:
    win = Window(800, 600)
    # test_lines(win)
    # test_cells(win)
    test_maze(win)
    win.wait_for_close()

def test_lines(window):
    p1 = Point(50, 50)
    p2 = Point(50, 150)
    p3 = Point(150, 50)
    p4 = Point(150, 150)

    l1_2 = Line(p1, p2)
    l1_3 = Line(p1, p3)
    l1_4 = Line(p1, p4)
    l3_4 = Line(p3, p4)

    window.draw_line(l1_2, "red")
    window.draw_line(l1_3, "blue")
    window.draw_line(l1_4, "orange")
    window.draw_line(l3_4, "green")

def test_cells(window):
    c1_1 = Point(50, 50)
    c1_4 = Point(150, 150)
    c2_1 = Point(150, 50)
    c2_4 = Point(250, 150)
    c3_1 = Point(50, 150)
    c3_4 = Point(150, 250)
    c4_1 = Point(150, 150)
    c4_4 = Point(250, 250)
    
    ct_1 = Point(305, 305)
    ct_4 = Point(345, 345)
    
    cb_1 = Point(355, 355)
    cb_4 = Point(395, 395)
    
    cl_1 = Point(405, 405)
    cl_4 = Point(445, 445)
    
    cr_1 = Point(455, 455)
    cr_4 = Point(495, 495)

    window.draw_cell(Cell(c1_1, c1_4, parent = window))
    window.draw_cell(Cell(c2_1, c2_4, parent = window))
    window.draw_cell(Cell(c3_1, c3_4, parent = window))
    window.draw_cell(Cell(c4_1, c4_4, parent = window))

    window.draw_cell(Cell(ct_1, ct_4, top = False, parent = window))
    window.draw_cell(Cell(cb_1, cb_4, bottom = False, parent = window))
    window.draw_cell(Cell(cl_1, cl_4, left = False, parent = window))
    window.draw_cell(Cell(cr_1, cr_4, right = False, parent = window))

    cell_1 = Cell(Point(400,  50), Point(450, 100), right = False, bottom = False, parent = window)
    cell_2 = Cell(Point(450,  50), Point(500, 100), left = False, parent = window)
    cell_3 = Cell(Point(400, 100), Point(450, 150), top = False, parent = window)
    window.draw_cell(cell_1)
    window.draw_cell(cell_2)
    window.draw_cell(cell_3)
    cell_1.draw_move(cell_2)
    cell_1.draw_move(cell_3, True)

def test_maze(window):
    m1 = Maze(10, 10, 10, 10, 10, 10, parent = window)
    m1.solve()

main()