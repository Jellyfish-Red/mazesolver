from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, color):
        line.draw(self.__canvas, color)
    
    def draw_cell(self, cell):
        cell.draw()

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True

        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

# x = 0 is the left of the screen
# y = 0 is the top of the screen
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, a, b):
        self.__point_a = a
        self.__point_b = b

    def draw(self, canvas, color):
        canvas.create_line(self.__point_a.x, self.__point_a.y, self.__point_b.x, self.__point_b.y, fill = color, width = 2)