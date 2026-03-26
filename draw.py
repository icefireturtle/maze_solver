import random
import tkinter as tk
from tkinter import Entry, Label, Tk, BOTH, Canvas, messagebox, Button, Frame, simpledialog
import builder


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("The Mighty Maze")
        self.current_maze_seed = "1142"
        self.__text_frame = Frame(self.__root, bg="#d9d9d9", padx=10, pady=10)
        self.__text = Label(self.__text_frame, text="Welcome to the Mighty Maze Solver!\nWatch as it is solved in real time!", bg="#d9d9d9", font=("Arial", 14))
        self.__current_maze_text = Label(self.__text_frame, text=f"Current Maze: {self.current_maze_seed}", bg="#d9d9d9", font=("Arial", 12))
        self.__text.pack()
        self.__current_maze_text.pack()
        self.__text_frame.pack()
        self.__labels = ["Rows", "Cols", "Cell Size X", "Cell Size Y", "Seed"]
        self.__entries = [Entry(self.__root) for _ in self.__labels]
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running_state = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__frame = Frame(self.__root, bg="#d9d9d9", padx=10, pady=10)
        self.buttons()

    def buttons(self):
        btn_new_maze = Button(self.__frame, text="New Maze", command=self.new_maze, bg="white", font=("Arial", 12))

        btn_exit = Button(self.__frame, text="Exit", command=self.safe_exit, bg="white", font=("Arial", 12))
        
        btn_new_maze.grid(row=1, column=1, padx=10, pady=10)
        btn_exit.grid(row=1, column=2, padx=10, pady=10)

        self.__frame.pack()

    def set_current_maze_text(self, text):
        self.current_maze_seed = text
        self.__current_maze_text.config(text=f"New Maze Generated.\nCurrent Maze: {self.current_maze_seed}")

    def new_maze(self):
        if messagebox.askquestion("Creating New Maze", "Are you sure you want to generate another maze?"):
            self.__canvas.delete("all")
            """x1=250
            y1=150
            rows=5
            cols=5
            cell_size_x=50
            cell_size_y=50
            seed_entry = simpledialog.askstring("Enter Seed Value", "Enter a seed value for the maze (leave blank for random):")
            if not seed_entry:
                seed = random.randint(0, 5000)
            else:
                seed = seed_entry
            self.set_current_maze_text(str(seed))
            self.redraw()
            builder.build_maze(x1, y1, rows, cols, cell_size_x, cell_size_y, None, seed) """
            params = builder.get_maze_parameters()
            builder.build_maze(None, None, params[0], params[1], params[2], params[3], None, params[4])
            
        
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

    class Form(simpledialog.Dialog):

        def body(self, window):
            Label(window, text="Rows:").grid(row=0, column=0, sticky="e")
            Label(window, text="Columns:").grid(row=1, column=0, sticky="e")
            Label(window, text="Cell Size X:").grid(row=2, column=0, sticky="e")
            Label(window, text="Cell Size Y:").grid(row=3, column=0, sticky="e")
            Label(window, text="Seed:").grid(row=4, column=0, sticky="e")

            self.entry_rows = Entry(window)
            self.entry_cols = Entry(window)
            self.entry_size_x = Entry(window)
            self.entry_size_y = Entry(window)
            self.entry_seed = Entry(window)

            self.entry_rows.grid(row=0, column=1, padx=5, pady=5)
            self.entry_cols.grid(row=1, column=1, padx=5, pady=5)
            self.entry_size_x.grid(row=2, column=1, padx=5, pady=5)
            self.entry_size_y.grid(row=3, column=1, padx=5, pady=5)
            self.entry_seed.grid(row=4, column=1, padx=5, pady=5)
        
            return self.entry_rows

        def validate(self):
            return True
        
        def apply(self):
            self.result = (
                self.entry_cols.get().strip(), 
                self.entry_rows.get().strip(), 
                self.entry_size_x.get().strip(), 
                self.entry_size_y.get().strip(), 
                self.entry_seed.get().strip()
                )

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

