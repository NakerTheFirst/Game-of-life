import ui
import tkinter as tk


class WindowInterface(ui.UserInterface):

    def _change_cell_colour(self, button):
        if button.cget("background") == "#fff":
            button.configure(bg="#1f1f1f")
        else:
            button.configure(bg="#fff")

    def view_menu(self, iters):

        # Root config
        root = tk.Tk()
        root.title("Game of Life")
        root.geometry("640x720")
        root.configure(bg="#302c2c")
        icon = tk.PhotoImage(file="icon.ico")
        root.iconphoto(False, icon)

        # Bottom part frame
        bottom_frame = tk.Frame(root, bg="#302c2c")
        bottom_frame.pack(side="bottom", fill="x", expand=True)

        # Buttons frame
        buttons_frame = tk.Frame(bottom_frame, bg="#302c2c")
        buttons_frame.pack(side="bottom", fill="x", pady=(0, 20))

        # Matrix canvas
        matrix_canvas = tk.Canvas(root, highlightthickness=0, bg="#777", width=540, height=560)
        matrix_canvas.pack(side="top", fill="both", padx=40, pady=(40, 20))

        # Quit button
        quit_button = tk.Button(buttons_frame, text="Quit", command=root.destroy, bg="#1f1f1f", fg="#fff",
                                highlightbackground="#1f1f1f",
                                border=0, padx=16, pady=10, activeforeground="#fff", activebackground="#1f1f1f")
        quit_button.pack(side="left", padx=20)

        # Start button
        start_button = tk.Button(buttons_frame, text="Start", bg="#1f1f1f", fg="#fff", highlightbackground="#1f1f1f",
                                 border=0, padx=16, pady=10, activeforeground="#fff", activebackground="#1f1f1f")
        start_button.pack(side="left", padx=20)

        # Center the buttons horizontally
        root.update_idletasks()
        button_width = quit_button.winfo_width()
        x = 320 - (button_width * 2 - 20)
        buttons_frame.place(x=x, y=0)

        # Draw the matrix based on input
        intervals_hor = self._matrix.get_rows()
        intervals_ver = self._matrix.get_cols()

        hor_delta = 560 / intervals_hor
        ver_delta = 560 / intervals_ver

        x0 = 0
        x1 = 560
        y0 = 0
        y1 = 0

        # Create horizontal matrix division
        for x in range(1, intervals_hor):
            y0 += ver_delta
            y1 = y0
            tk.Canvas.create_line(matrix_canvas, x0, y0, x1, y1, width=1, fill="#1f1f1f")

        x0 = 0
        x1 = 0
        y0 = 0
        y1 = 560

        # Create vertical matrix division
        for x in range(1, intervals_ver):
            x0 += hor_delta
            x1 = x0
            tk.Canvas.create_line(matrix_canvas, x0, y0, x1, y1, width=1, fill="#1f1f1f")

        cells = []

        x = 0
        y = 0
        w = hor_delta
        h = ver_delta

        for i in range(intervals_ver):
            for j in range(intervals_hor):
                cell = tk.Button(matrix_canvas, bg="#fff", width=int(w), height=int(h), borderwidth=1)
                cell.configure(command=lambda button=cell: self._change_cell_colour(button), activebackground=str(cell.cget("background")))
                cell.place(x=x, y=y)
                x += hor_delta
                cells.append(cell)
            y += ver_delta
            x = 0

        root.mainloop()

    def _run(self, iters):
        pass
