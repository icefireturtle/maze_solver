
import draw
from maze import Maze
from draw import Window

window = Window(800, 600)

def get_maze_parameters():
    params = draw.Window.Form(window._Window__root)
    print(f"params {params.result}")
    if params.result:
        rows = params[0]
        cols = params[1]
        cell_size_x = params[2]
        cell_size_y = params[3]
        seed = params[4]
    else:
        rows = 5
        cols = 5
        cell_size_x = 50
        cell_size_y = 50
        seed = 1142
    return rows, cols, cell_size_x, cell_size_y, seed


def build_maze(x1, y1, rows, cols, cell_size_x, cell_size_y, win=None, seed=None):
    if x1 is None:
        x1 = 275
    if y1 is None:
        y1 = 150
    if win is None:
        win = window
    Maze(x1, y1, rows, cols, cell_size_x, cell_size_y, win, seed)
    
    win.wait_for_close()