from input import Input
from matrix import Matrix
from window_interface import WindowInterface
from console_interface import ConsoleInterface


class Engine:
    def __init__(self):
        self.__input = Input()
        self.__matrix = None
        self.__ui = None

    def run(self):
        self.__input.take_rows()
        self.__input.take_cols()
        self.__input.take_ui_type()

        # Instantiate matrix and chosen interface objects
        self.__matrix = Matrix(self.__input.get_rows(), self.__input.get_cols())

        if self.__input.get_ui_type() == "console":
            self.__ui = ConsoleInterface(self.__matrix)
        elif self.__input.get_ui_type() == "window":
            self.__ui = WindowInterface(self.__matrix)

        self.__ui.view_menu(iters=10)
