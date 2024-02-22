from interface import Window, Point, Line

def main() -> int:
    win = Window(800, 600)
    test_lines(win)
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


main()