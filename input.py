class Input:
    def __init__(self):
        self.__rows = None
        self.__cols = None
        self.__ui_type = None

    def take_rows(self):
        user_rows = input("Enter number of rows: ")
        if Input.is_positive_int(user_rows):
            self.__rows = int(user_rows)

    def take_cols(self):
        user_cols = input("Enter number of columns: ")
        if Input.is_positive_int(user_cols):
            self.__cols = int(user_cols)

    @staticmethod
    def take_row_col_to_invert(invert):
        print("By default, the state of all the cells is initialised to 0.")
        print("Enter the row and column numbers of the cell to be inverted, separated by space. Indexed from 0.")
        print("In example: 2 1\nEnter a blank line to finish.")
        while True:
            try:
                row_col_input = input().strip()
                if not row_col_input:
                    break
                row, col = row_col_input.split()
                row, col = int(row), int(col)
                invert(row, col)
            except ValueError:
                print("Invalid input, please try again.")

    @staticmethod
    def is_positive_int(num):
        try:
            num = int(num)
        except ValueError:
            return False
        return isinstance(num, int) and num > 0

    def take_ui_type(self):
        self.__ui_type = input("Enter UI type: 'console' or 'window'\n")

    def is_ui_correct(self):
        if not (self.__ui_type.lower() == 'console' or self.__ui_type.lower() == 'window'):
            print("Input error: UI not defined correctly")
            self.take_ui_type()

    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols

    def get_ui_type(self):
        return self.__ui_type
