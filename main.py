from draw import Window
from maze import Maze

def main():
    window = Window(800, 600)
    """a = Point(100, 100)
    b = Point(700, 594)
    a = 50
    b = 200
    c = 150
    d = 400
    w = 250
    x = 300
    y = 350
    z = 600
    #line = Line(a, b)
    #cell_one = Cell(window)
    #cell_two = Cell(window)
    #cell_one.draw(a, b, c, d)
    #cell_two.draw(w, x, y, z)
    #cell_one.draw_move(cell_two)
    #window.draw_line(line, "red")"""
    x1=250
    y1=150
    rows=5
    cols=5
    cell_size_x=50
    cell_size_y=50
    maze = Maze(x1, y1, rows, cols, cell_size_x, cell_size_y, window)
    window.wait_for_close()

main()
