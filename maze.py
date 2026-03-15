from cell import Cell
import time  

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__rows = num_rows
        self.__cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for c in range(self.__cols):
            col = []
            for r in range(self.__rows):
                col.append(Cell(self.__win))
            self.__cells.append(col)
        
        if self.__win != None:

            for c in range(self.__cols):
                for r in range(self.__rows):
                    self.__draw_cell(c, r)

    def __draw_cell(self, i, j):

        if self.__win != None:

            x1 = self.__x1 + i * self.__cell_size_x
            y1 = self.__y1 + j * self.__cell_size_y
            x2 = x1 + self.__cell_size_x
            y2 = y1 + self.__cell_size_y

            self.__cells[i][j].draw(x1, y1, x2, y2)

            self.__animate()

    def __animate(self): 
        self.__win.redraw()
        time.sleep(.5)