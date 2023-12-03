import tkinter as tk
from random import randint

# from icecream import ic


# WIDTH - Ширина рабочего окна
WIDTH = 650
# HEIGHT - Высота рабочего окна
HEIGHT = 650
R0 = 10


# ic.enable()
# ic.disable()


class Balls:
    """Class Balls - свойства мячика
    x_koord: координата x центра мячика
    y_koord: координата y центра мячика
    r_ball:  радиус мячика
    dx:      смещение по оси x
    dy:      смещение по оси y
    number_ball: порядковый номер объекта Balls
    """

    def __init__(self):
        self.r_ball = randint(R0, HEIGHT // 13)
        self.x_koord = randint(R0+10, WIDTH - R0)
        self.y_koord = randint(R0+10, HEIGHT - R0)
        self.dx = randint(+2, +5)
        self.dy = randint(+2, +5)
        self.number_ball = canvas.create_oval(self.x_koord - self.r_ball,
                                              self.y_koord - self.r_ball,
                                              self.x_koord + self.r_ball,
                                              self.y_koord + self.r_ball,
                                              fill="#80CBC4",
                                              outline="#004D40",
                                              width=2)

    def move_ball(self):
        """Перемещение мячика"""

        if self.x_koord + self.r_ball > WIDTH or self.x_koord - self.r_ball <= 0:
            self.dx = -self.dx
        if self.y_koord + self.r_ball > HEIGHT or self.y_koord - self.r_ball <= 0:
            self.dy = -self.dy

        self.x_koord += self.dx
        self.y_koord += self.dy

    def show_ball(self):
        """Отрисовка после смещения"""
        canvas.move(self.number_ball, self.dx, self.dy)

    def erase_ball(self):
        """Удаление мячика"""
        canvas.delete(self.number_ball)


def canvas_click_handler(event):
    print('x=', event.x, 'y=', event.y)


def tick():
    for ball in balls:
        ball.move_ball()
        ball.show_ball()
    root.after(50, tick)


def close():
    canvas.destroy()
    root.destroy()


# def main():
#     """Главна программа"""
#     global root, canvas, balls
#     global number_ball, x_koord, y_koord, r_ball, dx, dy
root = tk.Tk()
root.title('Игра')
x = int((root.winfo_screenwidth() - WIDTH) / 2)
y = int((root.winfo_screenheight() - HEIGHT) / 2)
root.geometry(str(WIDTH) + 'x' + str(HEIGHT) + '+' + str(x) + '+' + str(y))
root.resizable(False, False)
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='coral')
canvas.pack(anchor='center', fill=tk.BOTH)
canvas.bind('<Button-1>', canvas_click_handler)
root.update_idletasks()

balls = [Balls() for _ in range(25)]
tick()
root.mainloop()


# if __name__ == '__main__':
#     main()
