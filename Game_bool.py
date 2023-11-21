from time import sleep
from tkinter import *
import random

from icecream import ic

HEIGHT = 400
WIDTH = 450
X0 = 50
Y0 = 50
R0 = 10
ic.enable()


# ic.disable()

class Bools:
    """Class Bools - свойства мячика
    x_koord: координата x центра мячика
    y_koord: координата y центра мячика
    r_bool:  радиус мячика
    dx:      смещение по оси x
    dy:      смещение по оси y
    number_bool: порядковый номер объекта Bools
    """

    def __init__(self):
        self.x_koord = None
        self.y_koord = None
        self.r_bool = None
        self.dx = None
        self.dy = None
        self.number_bool = None
        self.flag_bool = True
        self.items = []

    def create_bool(self):
        """Создание мячика"""
        self.number_bool: int = canvas.create_oval(self.x_koord - self.r_bool,
                                                   self.y_koord - self.r_bool,
                                                   self.x_koord + self.r_bool,
                                                   self.y_koord + self.r_bool,
                                                   fill="#80CBC4",
                                                   outline="#004D40",
                                                   width=2)

    def move_bool(self):
        """Перемещение мячика"""
        hc = canvas.winfo_height()
        wc = canvas.winfo_width()
        ic(self.number_bool, canvas.coords(self.number_bool))
        ic(hc, wc, R0, wc-R0, hc-R0)
        if canvas.coords(self.number_bool)[0] <= R0 or canvas.coords(self.number_bool)[2] >= wc-R0:
            self.dx = -1 * self.dx
        elif canvas.coords(self.number_bool)[1] <= R0 or canvas.coords(self.number_bool)[3] >= hc-R0:
            self.dy = -1 * self.dy
        canvas.move(self.number_bool, self.dx, self.dy)
        ic(self.number_bool, self.dx, self.dy)
        canvas.update()

    def erase_bool(self):
        """Удаление мячика"""
        canvas.delete(self.number_bool)


def close():
    canvas.destroy()
    root.destroy()


def main():
    """Главна программа"""
    root.title('Игра')
    root.geometry(f'{HEIGHT}x{WIDTH}')
    wcc = WIDTH * 0.95
    ic(wcc)
    hcc = HEIGHT * 0.95
    ic(hcc)
    canvas.config(bg="white", width=wcc, height=hcc)
    canvas.pack(anchor='center', expand=1, side='top')
    ic(canvas.winfo_height())
    ic(canvas.winfo_width())
    bool = Bools()

    for i in range(5):
        bool.x_koord = round(WIDTH * random.random())
        bool.y_koord = round(HEIGHT * random.random())
        bool.r_bool = R0
        bool.dx = 10
        bool.dy = 10
        bool.create_bool()
        ic(bool.number_bool, canvas.coords(bool.number_bool))
        bool.items.append(bool.number_bool)

    while True:
        for bool.number_bool in bool.items:
            bool.move_bool()
            sleep(0.002)


if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root)
    main()
    root.mainloop()
