from time import sleep
from tkinter import *
import random

from icecream import ic

HEIGHT = 400
WIDTH = 450
X0 = 50
Y0 = 50
R0 = 10
DX = 10
DY = 10

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
        self.dx = []
        self.dy = []
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
        ic(self.number_bool)
        if canvas.coords(self.number_bool)[0] < R0:
            self.dx[self.number_bool-1] = DX
        if canvas.coords(self.number_bool)[2] > wc-R0:
            self.dx[self.number_bool-1] = -1 * DX
        if canvas.coords(self.number_bool)[1] < R0:
            self.dy[self.number_bool-1] = DY
        if canvas.coords(self.number_bool)[3] > hc - R0:
            self.dy[self.number_bool-1] = -1 * DY
        canvas.move(self.number_bool, self.dx[self.number_bool-1], self.dy[self.number_bool-1])
        ic(self.number_bool, self.dx[self.number_bool-1], self.dy[self.number_bool-1])
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
    wcc = int(WIDTH * 0.95)
    hcc = int(HEIGHT * 0.95)
    canvas.config(bg="white", width=wcc, height=hcc)
    canvas.pack(anchor='center', expand=1, side='top')
    bool = Bools()

    for i in range(2):
        bool.x_koord = round(random.randint(DX+1, wcc-1))
        ic(bool.x_koord)
        bool.y_koord = round(random.randint(DY+1, hcc-1))
        ic(bool.y_koord)
        bool.r_bool = R0
        # bool.dx[i] = DX
        # bool.dy[i] = DY
        bool.dx.append(DX)
        bool.dy.append(DY)
        bool.create_bool()
        ic(bool.number_bool, canvas.coords(bool.number_bool))
        bool.items.append(bool.number_bool)

    ic(bool.dx, bool.dy, bool.items)

    while True:
        for bool.number_bool in bool.items:
            ic(bool.number_bool)
            bool.move_bool()
            sleep(0.002)


if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root)
    main()
    root.mainloop()
