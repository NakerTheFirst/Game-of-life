import ui
import time
from input import Input


class ConsoleInterface(ui.UserInterface):
    def view_menu(self, iters):
        # Taking input for which cell to invert, inverting
        Input.take_row_col_to_invert(self._matrix.invert_cell_state)

        # Printing the matrix's elements
        for i in range(iters):
            rows, cols, data = self._matrix.get_rows(), self._matrix.get_cols(), self._matrix.get_data()
            for x in range(rows):
                for j in range(cols):
                    if j != cols - 1:
                        print(data[x][j], end=" ")
                    else:
                        print(data[x][j])
            print()

            self._matrix.update()
            time.sleep(1.5)
