from maze import Maze
from draw import Window

window = Window(800, 600)

def build_maze(x1, y1, rows, cols, cell_size_x, cell_size_y, win=None, seed=None):
    if win is None:
        win = window
    Maze(x1, y1, rows, cols, cell_size_x, cell_size_y, win, seed)
    
    win.wait_for_close()