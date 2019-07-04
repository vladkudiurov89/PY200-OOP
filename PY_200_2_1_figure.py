# Реализуйте классы Figure, Rectangle, Ellipse. Нужен метод получения
# координат x, y, размеров фигур w и h, также нужно, чтобы можно было
# получить периметр и площадь фигуры. Интерфейс Figure определить из
# файла figure_painter.py, т.е. изучаете код, а затем пишете интерфейс класса
# Figure так, чтобы он работал. Для запускай файла figure_painter.py
# необходимо установить библиотеку pip install pyside2. (Тема 2. Слайды 44-47)
from abc import ABCMeta, abstractmethod, ABC


class Figure(metaclass=ABCMeta):
    def __init__(self, a, b, h, w):
        self.__a = a
        self.__b = b
        self.__h = h
        self.__w = w
        print("Figure")

    def a(self):
        return self.__a

    def b(self):
        return self.__b

    def h(self):
        return self.__h

    def w(self):
        return self.__w

    @abstractmethod
    def area(self):
        return

    @abstractmethod
    def perimeter(self):
        return


class Rectangle(Figure, ABC):
    def __init__(self, a, b, h, w):
        super().__init__(a, b, h, w)
        print("Rectangle")

    def area(self):
        return self.__a * self.__b

    def perimeter(self):
        return (self.__a * self.__b) * 2


import math


class Triangle(Figure, ABC):
    def __init__(self, a, b, alpha):
        super().__init__(a, b)
        self.__a = a
        self.__b = b
        self.__alpha = alpha
        print("Triangle")

    def area(self):
        return 0.5 * self.__a * self.__b * math.sin(self.__alpha)


class Ellipse(Figure, ABC):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.__a = a
        self.__b = b
        print("Ellipse")

    def area(self):
        return 3.14 * self.__a * self.__b
