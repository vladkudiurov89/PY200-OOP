# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 2. Инкапсуляция, наследование, полиморфизм

# Лабораторная работа № 2.2 (1 ак.ч.)

# Слушатель (ФИО): Кудюров В.В.

# ---------------------------------------------------------------------------------------------

# 1
# Создайте следующую цепочку наследования
# A 
# |
# B
# |
# C
# Создайте объект C. Получите кортеж всех родителей
print('Задание № 1: НАЧАЛО')


class A:
    pass


class B(A):
    pass


class C(B, A):
    pass


print(C.__mro__)
print('Задание № 1: КОНЕЦ')

# 2
# Создайте следующую цепочку наследования
# A 
# | \
# B  C
# | /
# D
# Создайте объект D. Получите кортеж всех родителей
print('Задание № 2: НАЧАЛО')


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.__mro__)
print('Задание № 2: КОНЕЦ')

# 3
# Создайте следующую цепочку наследования
#  A 
# / \
# B  C
# |  |
# |  D
# | / 
# F
# Создайте объект F. Получите кортеж всех родителей
print('Задание № 3: НАЧАЛО')
print(' Cannot create a consistent method resolution order (MRO) for bases')
print('Задание № 3: КОНЕЦ')

# 4
# Создайте следующую цепочку наследования
# A 
# | 
# B  C
# \ / 
#  F
# Создайте объект A.
# Добавьте методов класс A f, который печатает атрибут (public name, protected _name и private __name)
# экземпляра класса A. Аналогичные атрибуты для классов B, C, F.
# Вызовите все методы из объектов классов A, B, C, F
print('Задание № 4: НАЧАЛО')


class A:
    name = 'name'
    _name = '_name'
    __name = '__name'

    @classmethod
    def public_name(cls):
        print(cls.name)

    @classmethod
    def protected_name(cls):
        print(cls.name)

    @classmethod
    def private__name(cls):
        print(cls.name)


class B(A):
    name = 'name'
    _name = '_name'
    __name = '__name'

    @classmethod
    def public_name(cls):
        print(cls.name)

    @classmethod
    def protected_name(cls):
        print(cls.name)

    @classmethod
    def private__name(cls):
        print(cls.name)

class C(B, A):
    name = 'name'
    _name = '_name'
    __name = '__name'

    @classmethod
    def public_name(cls):
        print(cls.name)

    @classmethod
    def protected_name(cls):
        print(cls.name)

    @classmethod
    def private__name(cls):
        print(cls.name)

class F:
    name = 'name'
    _name = '_name'
    __name = '__name'

    @classmethod
    def public_name(cls):
        print(cls.name)

    @classmethod
    def protected_name(cls):
        print(cls.name)

    @classmethod
    def private__name(cls):
        print(cls.name)


print('Задание № 4: КОНЕЦ')
