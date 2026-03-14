from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Tkinter Window")
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running_state = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running_state = True
        while self.__running_state == True:
            self.redraw()
        
    def close(self):
        self.__running_state = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_one, point_two):
        self.point_one = point_one
        self.point_two = point_two

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_one.x, self.point_one.y, self.point_two.x, self.point_two.y, fill=fill_color, width=2)
        
class Cell:
    def __init__(self, window):
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
        

def main():
    window = Window(800, 600)
    #a = Point(100, 100)
    #b = Point(700, 594)
    a = 50
    b = 200
    c = 150
    d = 400
    w = 250
    x = 300
    y = 350
    z = 600
    #line = Line(a, b)
    cell = Cell(window)
    cell.draw(a, b, c, d)
    cell.draw(w, x, y, z)
    #window.draw_line(line, "red")
    window.wait_for_close()

main()
