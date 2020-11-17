import tkinter as tk
from setting import *


class LudoBoard:

    def __init__(self, master):
        self.canvas = tk.Canvas(master, width=Board.BOARD_WIDTH, height=Board.BOARD_HEIGHT, bg=Color.DEFAULT,
                                highlightthickness=0)
        self.side_bar = tk.Canvas(master, width=250, height=630, bg='white', highlightthickness=0)
        self.label = tk.Label(self.side_bar, text='Players:', bg='white', font=("Times", "23", "bold italic"))
        self.status_bar = tk.Label(master, text=Text.MADE_BY, bd=1, relief=tk.SUNKEN)

    def draw_rectangle(self, lx, ly, bx, by, color, width):
        self.canvas.create_rectangle(
            lx * Board.SQUARE_SIZE,
            ly * Board.SQUARE_SIZE,
            bx * Board.SQUARE_SIZE,
            by * Board.SQUARE_SIZE,
            fill=color,
            width=width)

    def draw_circle(self, x1, y1, x2, y2, color):
        self.canvas.create_oval(
            x1 * Board.SQUARE_SIZE,
            y1 * Board.SQUARE_SIZE,
            x2 * Board.SQUARE_SIZE,
            y2 * Board.SQUARE_SIZE,
            fill=color)

    def path(self):

        self.canvas.place(x=370, y=0)

        for i in range(6, 9):
            for j in range(15):
                if j not in range(6, 9) and (i != 7 or j == 0 or j == 14):
                    self.draw_rectangle(i + 0.5, j + 0.5, i + 1.5, j + 1.5, Color.DEFAULT, 1)
                    self.draw_rectangle(j + 0.5, i + 0.5, j + 1.5, i + 1.5, Color.DEFAULT, 1)
                else:
                    if j < 6:
                        self.draw_rectangle(i + 0.5, j + 0.5, i + 1.5, j + 1.5, Color.YELLOW, 1)
                        self.draw_rectangle(j + 0.5, i + 0.5, j + 1.5, i + 1.5, Color.GREEN, 1)
                    elif j > 8:
                        self.draw_rectangle(i + 0.5, j + 0.5, i + 1.5, j + 1.5, Color.RED, 1)
                        self.draw_rectangle(j + 0.5, i + 0.5, j + 1.5, i + 1.5, Color.BLUE, 1)

        for i, j in Board.POSITIVE_V:
            if i > j:
                self.draw_rectangle(i + 0.5, j + 0.5, i + 1.5, j + 1.5, Color.YELLOW, 1)
            else:
                self.draw_rectangle(i + 0.5, j + 0.5, i + 1.5, j + 1.5, Color.RED, 1)

        for j, i in Board.POSITIVE_H:
            if i > j:
                self.draw_rectangle(j + 0.5, i + 0.5, j + 1.5, i + 1.5, Color.GREEN, 1)
            else:
                self.draw_rectangle(j + 0.5, i + 0.5, j + 1.5, i + 1.5, Color.BLUE, 1)

    # def start(self):
    #     self.arrow_l = PhotoImage(file='Images/arrow_l.png')
    #     self.arrow_r = PhotoImage(file='Images/arrow_r.png')
    #     self.arrow_t = PhotoImage(file='Images/arrow_t.png')
    #     self.arrow_b = PhotoImage(file='Images/arrow_b.png')
    #     tk.Label(image=self.arrow_l, bg=Color.BLUE).place(x=915, y=343)
    #     tk.Label(image=self.arrow_t, bg=Color.RED).place(x=635, y=543)
    #     tk.Label(image=self.arrow_r, bg=Color.GREEN).place(x=435, y=263)
    #     tk.Label(image=self.arrow_b, bg=Color.YELLOW).place(x=715, y=63)

    def home(self):

        for i, j in Board.POINTS:

            if i == 0 and j == 0:
                self.draw_rectangle(i * 9 + 0.5, j * 9 + 0.5, i * 9 + 6.5, j * 9 + 6.5, Color.GREEN, 3)
            elif i == 0 and j == 1:
                self.draw_rectangle(i * 9 + 0.5, j * 9 + 0.5, i * 9 + 6.5, j * 9 + 6.5, Color.RED, 3)
            elif i == 1 and j == 0:
                self.draw_rectangle(i * 9 + 0.5, j * 9 + 0.5, i * 9 + 6.5, j * 9 + 6.5, Color.YELLOW, 3)
            else:
                self.draw_rectangle(i * 9 + 0.5, j * 9 + 0.5, i * 9 + 6.5, j * 9 + 6.5, Color.BLUE, 3)

            self.draw_rectangle(i * 9 + 1.25, j * 9 + 1.25, i * 9 + 5.75, j * 9 + 5.75, 'white', 0)

        for i, j in Board.POINTS:

            if i == 0 and j == 0:
                self.draw_rectangle(i * 9 + 1.65, j * 9 + 1.65, i * 9 + 3.3, j * 9 + 3.3, Color.GREEN, 0)
                self.draw_rectangle(i * 9 + 3.65, j * 9 + 3.65, i * 9 + 5.3, j * 9 + 5.3, Color.GREEN, 0)
                self.draw_rectangle(i * 9 + 1.65, j * 9 + 3.65, i * 9 + 3.3, j * 9 + 5.3, Color.GREEN, 0)
                self.draw_rectangle(i * 9 + 3.65, j * 9 + 1.65, i * 9 + 5.3, j * 9 + 3.3, Color.GREEN, 0)
            elif i == 0 and j == 1:
                self.draw_rectangle(i * 9 + 1.65, j * 9 + 1.65, i * 9 + 3.3, j * 9 + 3.3, Color.RED, 0)
                self.draw_rectangle(i * 9 + 3.65, j * 9 + 3.65, i * 9 + 5.3, j * 9 + 5.3, Color.RED, 0)
                self.draw_rectangle(i * 9 + 1.65, j * 9 + 3.65, i * 9 + 3.3, j * 9 + 5.3, Color.RED, 0)
                self.draw_rectangle(i * 9 + 3.65, j * 9 + 1.65, i * 9 + 5.3, j * 9 + 3.3, Color.RED, 0)
            elif i == 1 and j == 0:
                self.draw_rectangle(i * 9 + 1.65, j * 9 + 1.65, i * 9 + 3.3, j * 9 + 3.3, Color.YELLOW, 0)
                self.draw_rectangle(i * 9 + 3.65, j * 9 + 3.65, i * 9 + 5.3, j * 9 + 5.3, Color.YELLOW, 0)
                self.draw_rectangle(i * 9 + 1.65, j * 9 + 3.65, i * 9 + 3.3, j * 9 + 5.3, Color.YELLOW, 0)
                self.draw_rectangle(i * 9 + 3.65, j * 9 + 1.65, i * 9 + 5.3, j * 9 + 3.3, Color.YELLOW, 0)
            else:
                self.draw_rectangle(i * 9 + 1.65, j * 9 + 1.65, i * 9 + 3.3, j * 9 + 3.3, Color.BLUE, 0)
                self.draw_rectangle(i * 9 + 3.65, j * 9 + 3.65, i * 9 + 5.3, j * 9 + 5.3, Color.BLUE, 0)
                self.draw_rectangle(i * 9 + 1.65, j * 9 + 3.65, i * 9 + 3.3, j * 9 + 5.3, Color.BLUE, 0)
                self.draw_rectangle(i * 9 + 3.65, j * 9 + 1.65, i * 9 + 5.3, j * 9 + 3.3, Color.BLUE, 0)

    def create_panel(self):
        self.side_bar.place(x=0, y=0)
        self.label.place(x=65, y=0)
        self.side_bar.create_line(249, 0, 249, 630)
        self.side_bar.create_line(3, 280, 246, 280, dash=(4, 2))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create(self):
        self.path()
        self.home()
        # self.start()
        self.create_panel()

    def get_canvas(self):
        return self.canvas

    def get_frame(self):
        return self.side_bar