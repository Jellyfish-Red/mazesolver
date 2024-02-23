import random
from time import sleep
from interface import Point
from cell import Cell

class Maze:
    def __init__(self, start_x, start_y, rows, columns, cell_size_x, cell_size_y, parent = None, seed = None):
        self.__parent = parent
        self.__start_x = start_x
        self.__start_y = start_y
        self.__rows = rows
        self.__columns = columns
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y

        if seed is not None:
            self.__seed = random.seed(seed)
        else:
            self.__seed = random.seed()

        self.cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)

    def __create_cells(self):
        for i in range(self.__columns):
            column = []
            for j in range(self.__rows):
                column.append(self.__create_cell(i, j))
            self.cells.append(column)
        
        for column in self.cells:
            for cell in column:
                self.__draw_cell(cell)

    def __create_cell(self, i, j):
        p1 = Point((i * self.__cell_size_x) + self.__start_x, (j * self.__cell_size_y) + self.__start_y)
        p4 = Point(p1.x + self.__cell_size_x, p1.y + self.__cell_size_y)

        # print("Creating cell at p1 of (" + str(p1.x) + ", " + str(p1.y) + ")")

        return Cell(p1, p4, parent = self.__parent)

    def __draw_cell(self, cell):
        if self.__parent is None:
            return
        cell.draw()
        self.__animate()

    def __animate(self):
        if self.__parent is None:
            return
        self.__parent.redraw()
        sleep(0.01)

    def __break_entrance_and_exit(self):
        entrance_cell = self.cells[0][0]
        entrance_cell.has_top = False
        if self.__parent is not None:
            entrance_cell.draw()

        exit_cell = self.cells[self.__columns - 1][self.__rows - 1]
        exit_cell.has_bottom = False
        if self.__parent is not None:
            exit_cell.draw()
    
    def __break_walls_r(self, i, j):
        self.cells[i][j].visited = True

        visitable = []
        for direction in range(4): # N, S, W, E
            match direction:
                case 0: # North
                    if j <= 0:
                        continue
                    if self.cells[i][j - 1].visited:
                        continue

                    visitable.append(0)

                case 1: # South
                    if j >= self.__rows - 1:
                        continue
                    if self.cells[i][j + 1].visited:
                        continue

                    visitable.append(1)
                    
                case 2: # West
                    if i <= 0:
                        continue
                    if self.cells[i - 1][j].visited:
                        continue

                    visitable.append(2)
                    
                case 3: # East
                    if i >= self.__columns - 1:
                        continue
                    if self.cells[i + 1][j].visited:
                        continue

                    visitable.append(3)
        
        if len(visitable) == 0:
            self.cells[i][j].draw()
            return
        
        for loop in range(random.randrange(0, len(visitable)) + 1):

            match visitable[random.randrange(0, len(visitable))]:
                case 0: # North
                    self.cells[i][j].has_top = False
                    self.cells[i][j - 1].has_bottom = False
                    self.cells[i][j].draw()
                    self.cells[i][j - 1].draw()
                    self.__break_walls_r(i, j - 1)

                case 1: # South
                    self.cells[i][j].has_bottom = False
                    self.cells[i][j + 1].has_top = False
                    self.cells[i][j].draw()
                    self.cells[i][j + 1].draw()
                    self.__break_walls_r(i, j + 1)
                    
                case 2: # West
                    self.cells[i][j].has_left = False
                    self.cells[i - 1][j].has_right = False
                    self.cells[i][j].draw()
                    self.cells[i - 1][j].draw()
                    self.__break_walls_r(i - 1, j)
                    
                case 3: # East
                    self.cells[i][j].has_right = False
                    self.cells[i + 1][j].has_left = False
                    self.cells[i][j].draw()
                    self.cells[i + 1][j].draw()
                    self.__break_walls_r(i + 1, j)