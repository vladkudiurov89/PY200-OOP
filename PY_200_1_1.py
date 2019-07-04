# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Кудюров Владислав

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class Glass:

    def __init__(self, capacity_volume, occupied_volume):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    @staticmethod
    def glass_error(occupied_volume, capacity_volume):
        if not isinstance(capacity_volume, int):
            raise TypeError('capacity_volume must be int')
        if not isinstance(occupied_volume, int):
            raise TypeError("occupied_volume must be int")

        if not 0 < capacity_volume or capacity_volume > 500:
            raise TypeError('Invalid object,must be 0 < capacity_volume < 500')
        if not 0 < occupied_volume or occupied_volume > 500:
            raise ValueError('Invalid value,must be 0 < occupied_volume < 500')


glass = Glass(400, 200)
print(f"Capacity{glass.capacity_volume}\nCurrent:{glass.occupied_volume}")

# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.

glass_1 = Glass(500, 100)
glass_2 = Glass(500, 0)
glass_2.occupied_volume = 400
print(f"glass_1:Capacity:{glass_1.capacity_volume}\nglass_1:Current:{glass_1.occupied_volume}")
print(f"glass_2:Capacity{glass_2.capacity_volume}\nglass_2:Current:{glass_2.occupied_volume}")


# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class GlassDefaultArg:
    def __init__(self, occupied_volume=0):
        self.occupied_volume = occupied_volume

    @classmethod
    def error(cls, occupied_volume):

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError('Invalid object,capacity_volume must be int')
        if occupied_volume < 0 or occupied_volume > 500:
            raise ValueError('Invalid value,occupied_volume must be > 0')


glass_1_3 = GlassDefaultArg()
glass_2_3 = GlassDefaultArg(200)
print(f"glass_1_3: Current:{glass_1_3.occupied_volume}")
print(f"glass_1_3: Current:{glass_2_3.occupied_volume}")


# 4. Создайте класс GlassDefaultListArg (нужен только __init__)
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?


class GlassDefaultListArg:

    def __init__(self, capacity_volume, occupied_volume=None):
        if occupied_volume is None:
            occupied_volume = []
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        occupied_volume.append(capacity_volume)


glass_4_1 = GlassDefaultArg(1)
print(f"glass_4_1: Current:{glass_4_1.occupied_volume}")
glass_4_2 = GlassDefaultArg(2)
print(f"glass_4_1: Current:{glass_4_2.occupied_volume}")
glass_4_3 = GlassDefaultArg(3)
print(f"glass_4_1: Current:{glass_4_3.occupied_volume}")


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.

class GlassAddRemove:

    def __init__(self, water=0, occupied_volume=0):
        self.occupied_volume = occupied_volume
        self.water = water
        print(dir(self))

    @classmethod
    def glass_error(cls, occupied_volume, water):
        if not isinstance(occupied_volume, int):
            raise TypeError("occupied_volume must be int")
        if not isinstance(water, int):
            raise TypeError('water must be int')
        if not 0 < occupied_volume or occupied_volume > 500:
            raise ValueError('Invalid value,must be 0 < occupied_volume < 500')
        if not 0 < water or water > 500:
            raise TypeError('Invalid object,must be 0 < water < 500')

    def add_water(self, water):
        self.occupied_volume += water
        return self.occupied_volume

    def remove_water(self, water):
        self.occupied_volume -= water
        return self.occupied_volume


glass_5 = GlassAddRemove(0, 300)
print(f"glass_5(occupied_volume): Current:{glass_5.occupied_volume}")
print(f"glass_5(add_water(150)): Current:{glass_5.add_water(150)}")
print(f"glass_5(remove_water(150)): Current:{glass_5.remove_water(150)}")

# 6. Создайте три объекта типа GlassAddRemove,
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.


glass_6_1 = GlassAddRemove(100, 200)
print(glass_6_1.__dir__())
glass_6_2 = GlassAddRemove(200, 300)
print(glass_6_2.__dir__())
glass_6_3 = GlassAddRemove(300, 400)
print(glass_6_3.__dir__())

# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.

glass_7_1 = GlassAddRemove(100, 200)
print(type(glass_7_1))
glass_7_2 = GlassAddRemove(200, 300)
print(type(glass_7_2))
glass_7_3 = GlassAddRemove(300, 400)
print(type(glass_7_3))

# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.
glass_8_1 = Glass
print(f'glass_8_1_id:{id(glass_8_1)}')
glass_8_2 = Glass
print(f'glass_8_2_id:{id(glass_8_2)}')
glass_8_3 = Glass
print(f'glass_8_3_id:{id(glass_8_3)}')


# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.

class d:
    def __init__(f, a=2):
        f.a = a

    def print_me(p):
        print(p.a)


d.print_me(d())


# С нарушениями PEP 8,корректно.


# # 10. Исправьте


class A:
    def __init__(self, a):
        if 10 < a < 50:
            return
        self.a = a


# Объясните так реализовывать __init__ нельзя?
# Лишнее ";", можно, но не желательно

# 11. Циклическая зависимость (стр. 39-44)


class Node:
    def __init__(self, prev, next_=None):
        self.__prev = prev
        self.__next = next_

    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev

    def __str__(self):
        ...

    def __repr__(self):
        ...


class LinkedList:

    def __init__(self, node):
        self.head = node

    def insert(self, node, index=0):
        '''Insert Node to any place of LinkedList
        node - Node index - position of node'''
        count = 1
        if index == 0:
            node.set_next(self.head)
        else:
            node = self.head
            while node.next is not None:
                if count == index:
                    node.set_next(node.next)
                    node.set_next(node)
                    return
                node = node.set_next()
                count += 1



    def append(self, node):
        '''Append Node to tail of LinkedList node - Node'''
        node_1 = Node(node)
        node_1.next = self.head
        self.head = node_1


    # def clear(self):
    #     '''Clear LinkedList'''
    #     return
    #
    # def find(self, node):
    #
    #
    # def remove(self, node):
    #     ...
    #
    # def delete(self, index):
        ...
