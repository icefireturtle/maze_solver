
import draw
from maze import Maze
from draw import Window

window = Window(800, 600)

def get_maze_parameters():
    params = draw.Window.Form(window._Window__root)
    print(f"params {params.result}")
    if params.result:
        rows = int(params.result[0])
        cols = int(params.result[1])
        cell_size_x = int(params.result[2])
        cell_size_y = int(params.result[3])
        seed = int(params.result[4]) if params.result[4] else None
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