import ui
import time


class ConsoleInterface(ui.UserInterface):
    def _initialise(self):
        print("Enter the row and column numbers of the cells to be inverted, separated by space.")
        print("Enter a blank line to finish.")

        while True:
            try:
                row_col_input = input().strip()
                if not row_col_input:
                    break
                row, col = row_col_input.split()
                row, col = int(row), int(col)
                self._matrix.invert_cell_state(row, col)
            except ValueError:
                print("Invalid input, please try again.")

    def _run(self, iters):
        for i in range(iters):
            self._matrix._view()
            self._matrix.update()
            time.sleep(1.5)
