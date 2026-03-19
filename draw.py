from tkinter import Tk, BOTH, Canvas, messagebox, Button


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("The Mighty Maze")
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running_state = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.buttons()
        

    def buttons(self):
        btn_new_maze = Button(self.__root, text="New Maze", command=self.clicked, bg="white", font=("Arial", 12))
        btn_new_maze.pack(pady=10)

        btn_exit = Button(self.__root, text="Exit", command=self.safe_exit, bg="white", font=("Arial", 12))
        btn_exit.pack(pady=10)

    def clicked(self):
        print("Button clicked!")

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

    def safe_exit(self):
        if messagebox.askyesno("Exit", "Ready to exit?"):
            self.close()


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