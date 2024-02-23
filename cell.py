from interface import Point, Line, Window
class Cell:
    def __init__(self, p1 : Point, p4 : Point, 
                 top = True, left = True, right = True, bottom = True, color="black", 
                 visited = False, parent : Window = None):
        self.__parent = parent
        self.p1 = p1
        self.__p2 = Point(p4.x, p1.y)
        self.__p3 = Point(p1.x, p4.y)
        self.__p4 = p4
        
        self.has_top = top
        self.has_left = left
        self.has_right = right
        self.has_bottom = bottom

        self.visited = visited
        self.__color = color

    def draw(self):
        l1_2 = Line(self.p1, self.__p2)
        l1_3 = Line(self.p1, self.__p3)
        l2_4 = Line(self.__p2, self.__p4)
        l3_4 = Line(self.__p3, self.__p4)

        if self.has_top:
            self.__parent.draw_line(l1_2, self.__color)
        else:
            self.__parent.draw_line(l1_2, "white")

        if self.has_left:
            self.__parent.draw_line(l1_3, self.__color)
        else:
            self.__parent.draw_line(l1_3, "white")

        if self.has_right:
            self.__parent.draw_line(l2_4, self.__color)
        else:
            self.__parent.draw_line(l2_4, "white")
            
        if self.has_bottom:
            self.__parent.draw_line(l3_4, self.__color)
        else:
            self.__parent.draw_line(l3_4, "white")

    def draw_move(self, target_cell, undo = False):
        color = "red"
        if undo:
            color = "gray"
        
        self.__parent.draw_line(Line(self.get_center(), target_cell.get_center()), color)

    def get_center(self):
        distance_x = self.__p2.x - self.p1.x
        distance_y = self.__p3.y - self.p1.y
        return Point(self.p1.x + (distance_x / 2), self.p1.y + (distance_y / 2))