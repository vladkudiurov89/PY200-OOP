# 1. В Python нет возможности объявления константных переменных. Реализуйте
# с помощью @property константный атрибут. Пусть класс возвращает число
# пи. Попытайтесь применить @property к @staticmethod и @classmethod. Если
# не получается, то примените к обычному методу. (Тема 1. Слайды 1-43)


class Pi:
    @property
    def test_pi(self):
        return 3.14


const_pi = Pi()
print(f'pi_character:{const_pi.test_pi}')


# Создайте классы A и B(A). a. В классе А создайте атрибуты класса, атрибуты
# объекта, @staticmethod, @classmethod и методов со всеми видами областями
# видимости. b. Продемонстрируете их видимость внутри класса, вне класса и в
# классе потомке. c. Получите доступ вне класса к псевдозащищённым
# псевдоприватным атрибутам и методам. (Тема 2. Слайды 1-43)


class A:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def get_car(self):
        return f'{self.__name__}_{self.name}, {self.model}'

    @classmethod
    def test_add_name(cls, car):
        name, model = car
        return cls(name, model)

    @staticmethod
    def test_add_model(model):
        return model


car_name_a = A.test_add_name(["Opel", "astra"])
print(f'Car name:{car_name_a.name}\nCar model:{car_name_a.model}')
print(car_name_a.__str__())


class B(A):
    def __init__(self, name, model):
        super().__init__(name, model)


car_name_b = B.test_add_name(["BMV", 7])
print(f'Car name:{car_name_b.name}\nCar model:{car_name_b.model}')
print(car_name_b.__str__())


class C(B, A):
    def __init__(self, name, model):
        super().__init__(name, model)


car_name_c = C.test_add_name(["Porshe", 911])
print(f'Car name:{car_name_c.name}\nCar model:{car_name_c.model}')
print(car_name_c.__str__())

# В Python 3 все классы являются классами нового стиля. Классы нового стиля
# – это классы, которые являются наследниками от класса object. Убедитесь,
# что класс А является наследником от object. (Тема 2. Слайды 48-52)


print(C.__mro__)

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


class Rectangle(Figure, ABC):
    def __init__(self, a, b, h, w):
        super().__init__(a, b, h, w)
        print("Rectangle")

    def area(self):
        return self.__a * self.__b


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
