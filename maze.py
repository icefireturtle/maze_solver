from cell import Cell
import time  
import random

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
            seed=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__rows = num_rows
        self.__cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        if seed is not None:
           random.seed(seed)
        self.__seed = seed
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
        
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

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
        time.sleep(.1)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__cols-1][self.__rows-1].has_bottom_wall = False
        self.__draw_cell(self.__cols-1, self.__rows-1) 
    
    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        while True:

            unvisited = []            

            if i - 1 >= 0:
                neighbor_left = self.__cells[i - 1][j]
                if not neighbor_left.visited:
                    unvisited.append((i-1, j))

            if i + 1 < self.__cols:
                neighbor_right = self.__cells[i + 1][j]
                if not neighbor_right.visited:
                    unvisited.append((i+1, j))

            if j - 1 >= 0:
                neighbor_up = self.__cells[i][j - 1]
                if not neighbor_up.visited:
                    unvisited.append((i, j-1))

            if j + 1 < self.__rows:
                neighbor_down = self.__cells[i][j + 1]
                if not neighbor_down.visited:
                    unvisited.append((i, j+1))

            if unvisited == []:
                self.__draw_cell(i, j)
                return

            random.shuffle(unvisited)
            next_cell = unvisited[0]

            if next_cell == (i, j-1):
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j-1].has_bottom_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(i, j-1)
            
            if next_cell == (i, j+1):
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j+1].has_top_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(i, j+1)

            if next_cell == (i-1, j):
                self.__cells[i][j].has_left_wall = False
                self.__cells[i-1][j].has_right_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(i-1, j)

            if next_cell == (i+1, j):
                self.__cells[i][j].has_right_wall = False
                self.__cells[i+1][j].has_left_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(i+1, j)

            ni, nj = next_cell
            self.__break_walls_r(ni, nj)

    def __reset_cells_visited(self):
        for c in range(self.__cols):
            for r in range(self.__rows):
                self.__cells[c][r].visited = False
        
