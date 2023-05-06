from window_interface import WindowInterface
from console_interface import ConsoleInterface
import matrix
import time


class Engine:
    def __init__(self, rows, cols, interface_type):
        self.matrix = matrix.Matrix(rows, cols)
        self._rows = rows
        self._cols = cols

        # Set the interface type
        if interface_type.lower() == 'console':
            self.interface = ConsoleInterface(self.matrix)
        elif interface_type.lower() == 'window':
            self.interface = WindowInterface(self.matrix)
        else:
            raise ValueError("Invalid interface type. Please choose either 'console' or 'window'.")

    def initialise(self, iters):
        self.interface._initialise()
        self.interface._run(iters)
