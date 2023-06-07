import tkinter as tk
from ui import UserInterface


class WindowInterface(UserInterface):

    def __init__(self, matrix):
        super().__init__(matrix)
        self.root = None
        self.cells = []
        self._iters_left = 0

    def _change_cell_state_and_colour(self, button, row, col):
        # Invert cell state in the matrix
        self._matrix.invert_cell_state(row, col)

        # Change cell colour in the GUI
        self._change_cell_colour(button)

    def _change_cell_colour(self, button):
        if button.cget("background") == "#fff":
            button.configure(bg="#1f1f1f")
        else:
            button.configure(bg="#fff")

    def start_game(self, iters):
        self._iters_left = iters
        self._update_game()

    def _update_game(self):
        if self._iters_left > 0:
            self._matrix.update()
            self.update_cells()
            self._iters_left -= 1
            self.root.after(1000, self._update_game)

    def update_cells(self):
        for i, j, cell in self.cells:
            cell_state = self._matrix.get_data()[i][j]
            cell_colour = "#1f1f1f" if cell_state == 1 else "#fff"
            cell.configure(bg=cell_colour)

    def view_menu(self, iters):
        self._init_root()
        bottom_frame = self._create_bottom_frame()
        buttons_frame = self._create_buttons_frame(bottom_frame)
        self._create_quit_button(buttons_frame)
        self._create_start_button(buttons_frame, iters)
        self._center_buttons_horizontally(buttons_frame)
        matrix_canvas = self._create_matrix_canvas()
        self._create_matrix_grid(matrix_canvas)
        self._create_cells(matrix_canvas)
        self.root.mainloop()

    def _init_root(self):
        self.root = tk.Tk()
        self.root.title("Game of Life")
        self.root.geometry("640x720")
        self.root.configure(bg="#302c2c")
        icon = tk.PhotoImage(file="icon.ico")
        self.root.iconphoto(False, icon)

    def _create_bottom_frame(self):
        bottom_frame = tk.Frame(self.root, bg="#302c2c")
        bottom_frame.pack(side="bottom", fill="x", expand=True)
        return bottom_frame

    def _create_buttons_frame(self, bottom_frame):
        buttons_frame = tk.Frame(bottom_frame, bg="#302c2c")
        buttons_frame.pack(side="bottom", fill="x", pady=(0, 20))
        return buttons_frame

    def _create_quit_button(self, buttons_frame):
        quit_button = tk.Button(buttons_frame, text="Quit", command=self.root.destroy, bg="#1f1f1f", fg="#fff",
                                highlightbackground="#1f1f1f",
                                border=0, padx=16, pady=10, activeforeground="#fff", activebackground="#1f1f1f")
        quit_button.pack(side="left", padx=20)

    def _create_start_button(self, buttons_frame, iters):
        start_button = tk.Button(buttons_frame, text="Start", command=lambda it=iters: self.start_game(iters),
                                 bg="#1f1f1f", fg="#fff", highlightbackground="#1f1f1f",
                                 border=0, padx=16, pady=10, activeforeground="#fff", activebackground="#1f1f1f")
        start_button.pack(side="left", padx=20)

    def _center_buttons_horizontally(self, buttons_frame):
        self.root.update_idletasks()
        button_width = buttons_frame.winfo_children()[0].winfo_width()
        x = 320 - (button_width * 2 - 20)
        buttons_frame.place(x=x, y=0)

    def _create_matrix_canvas(self):
        matrix_canvas = tk.Canvas(self.root, highlightthickness=0, bg="#777", width=540, height=560)
        matrix_canvas.pack(side="top", fill="both", padx=40, pady=(40, 20))
        return matrix_canvas

    def _create_matrix_grid(self, matrix_canvas):
        intervals_hor = self._matrix.get_rows()
        intervals_ver = self._matrix.get_cols()

        hor_delta = 560 / intervals_hor
        ver_delta = 560 / intervals_ver

        # Create horizontal matrix division
        for x in range(1, intervals_hor):
            y = x * ver_delta
            matrix_canvas.create_line(0, y, 560, y, width=1, fill="#1f1f1f")

        # Create vertical matrix division
        for x in range(1, intervals_ver):
            x = x * hor_delta
            matrix_canvas.create_line(x, 0, x, 560, width=1, fill="#1f1f1f")

    def _create_cells(self, matrix_canvas):
        intervals_hor = self._matrix.get_rows()
        intervals_ver = self._matrix.get_cols()

        hor_delta = 560 / intervals_hor
        ver_delta = 560 / intervals_ver

        for i in range(intervals_ver):
            for j in range(intervals_hor):
                # Get cell state from the matrix
                cell_state = self._matrix.get_data()[i][j]

                # Determine the initial cell colour based on the cell state
                cell_colour = "#1f1f1f" if cell_state == 1 else "#fff"

                x = j * hor_delta
                y = i * ver_delta
                cell = tk.Button(matrix_canvas, bg=cell_colour, width=int(hor_delta), height=int(ver_delta),
                                 borderwidth=1)
                cell.configure(
                    command=lambda button=cell, row=i, col=j: self._change_cell_state_and_colour(button, row, col),
                    activebackground=str(cell.cget("background"))
                )
                cell.place(x=x, y=y)
                # Append the cell to the instance variable cells
                self.cells.append((i, j, cell))
