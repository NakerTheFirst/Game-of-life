class Matrix:
    def __init__(self, rows, cols):
        self.__rows: int = rows
        self.__cols: int = cols
        self.__data: list = [[0] * cols for _ in range(rows)]

    def _view(self):
        rows = len(self.__data)
        cols = len(self.__data[0])
        for x in range(rows):
            for i in range(cols):
                if i != cols - 1:
                    print(self.__data[x][i], end=" ")
                else:
                    print(self.__data[x][i])
        print()

    def invert_cell_state(self, row, col):
        if self.__data[row][col] == 0:
            self.__data[row][col] = 1
        else:
            self.__data[row][col] = 0

    def get_active_neighs_num(self, row, col):
        active = 0
        for r in range(max(row - 1, 0), min(row + 2, self.__rows)):
            for c in range(max(col - 1, 0), min(col + 2, self.__cols)):
                if r == row and c == col:
                    continue
                if self.__data[r][c] == 1:
                    active += 1
        return active

    def update(self):
        # Create a new matrix to store the next generation
        new_data = [[0 for _ in range(len(self.__data[0]))] for _ in range(len(self.__data))]

        # Loop through each cell in the matrix
        for i in range(self.__rows):
            for j in range(self.__cols):
                # Get the number of active neighbors for the current cell
                active_neighs = self.get_active_neighs_num(i, j)

                # Apply the rules of Conway's Game of Life
                if self.__data[i][j] == 1 and (active_neighs == 2 or active_neighs == 3):
                    new_data[i][j] = 1
                elif self.__data[i][j] == 0 and active_neighs == 3:
                    new_data[i][j] = 1
        self.__data = new_data

    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols

    def get_data(self):
        return self.__data
