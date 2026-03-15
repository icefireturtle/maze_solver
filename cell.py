from draw import Line, Point

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
    
    def draw(self, x1, y1, x2, y2, fill_color="black"):
        
        if self.__win != None:
        
            self.__x1 = x1
            self.__y1 = y1
            self.__x2 = x2
            self.__y2 = y2

            if self.has_left_wall == True:
                wall_one = Point(self.__x1, self.__y1)
                wall_two = Point(self.__x1, self.__y2)
                wall_line = Line (wall_one, wall_two)
                self.__win.draw_line(wall_line, fill_color)

            if self.has_right_wall == True:
                wall_one = Point(self.__x2, self.__y1)
                wall_two = Point(self.__x2, self.__y2)
                wall_line = Line (wall_one, wall_two)
                self.__win.draw_line(wall_line, fill_color)

            if self.has_top_wall == True:
                wall_one = Point(self.__x1, self.__y1)
                wall_two = Point(self.__x2, self.__y1)
                wall_line = Line (wall_one, wall_two)
                self.__win.draw_line(wall_line, fill_color)

            if self.has_bottom_wall == True:
                wall_one = Point(self.__x1, self.__y2)
                wall_two = Point(self.__x2, self.__y2)
                wall_line = Line (wall_one, wall_two)
                self.__win.draw_line(wall_line, fill_color)

    def draw_move(self, to_cell, undo=False):
        if self.__win != None:

            if undo == False:
                fill_color = "red"
            else:
                fill_color = "gray"
            
            height = (self.__y1 + self.__y2) / 2
            width = (self.__x1 + self.__x2) / 2
            center = Point(width, height)

            to_height = (to_cell.__y1 + to_cell.__y2) / 2
            to_width = (to_cell.__x1 + to_cell.__x2) / 2
            to_center = Point(to_width, to_height)

            path = Line(center, to_center)

            self.__win.draw_line(path, fill_color)