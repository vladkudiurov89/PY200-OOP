# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 2. Инкапсуляция, наследование, полиморфизм
# Абстрактные классы

# Лабораторная работа № 2.3 (6 ак.ч.)

# Слушатель (ФИО): Кудюров В.В.

# ---------------------------------------------------------------------------------------------

# 1
# Разработайте два абстрактных класса:
# - IReader с абстрактным методом read, который принимает строку с названием файла,
#   а возвращает словарь со ключами и их значениями или None;
# - IWriter с методом write, который принимает строку с названием файла и 
#   словарь со ключами и их значениями. Возвращает True, если запись успешно выполнена,
#   иначе False
# Метод IReader.read читает данные из файла
# Метод IWriter записывает данные в файла
# Наследуйтесь от класса IReader:
# - JSONReader: читает файл формата json;
# - CSVReader: читает файл формата csv;
# Наследуйтесь от класса IWriter:
# - JSONWriter: записывает файл формата json;
# - CSVWriter: записывает файл формата csv;
from abc import ABCMeta, abstractmethod
import csv
import json


class IReader(metaclass=ABCMeta):

    @abstractmethod
    def test_read(self, file_read):
        pass


class IWriter(metaclass=ABCMeta):

    @abstractmethod
    def test_write(self, file_read, file_write):
        pass


class CSVReader(IReader):
    def __init__(self):
        self.__csv_reader = []

    def test_read(self, new_file):
        with open(new_file, 'r') as csv_file:
            csv_read_file = csv.DictReader(csv_file, delimiter=';')
            for i in csv_read_file:
                self.__csv_reader.append(dict(i))
                return self.__csv_reader


class JSONReader(IReader):

    def test_read(self, new_file):
        with open(new_file, 'r') as json_file:
            json_read_file = json.load(json_file)
            return json_read_file


class JSONWriter(IWriter):

    def test_write(self, file, file_write):
        with open(file, 'w') as json_file:
            try:
                json.dump(file_write, json_file)
            except TypeError:
                return False
        return True


class CSVWriter(IWriter):

    def test_write(self, new_file, file_write):
        with open(file, 'w') as csv_file:
            try:
                csv_writer = csv.DictWriter(csv_file, delimeter=';', fieldnames=file_write.keys())
                csv_writer.writeheader()
                csv_writer.writerows(file_write)
            except TypeError:
                return False
        return True


# print(JSONReader().test_read('Yesterday.json'))
# print(CSVReader().test_read('Tomorrow.csv'))
# print(JSONWriter().test_write('test_write.json', {'time': 'morning', 'action': 'go to study'}))
# print(CSVWriter().test_write('test_write.csv', {'time': 'morning', 'action': 'go to study'}))

# 2
# Шаблон стратегия
# Класс ReadClient содержит ссылки на JSONReader и CSVWriter.
# Нужный драйвер чтения файла автоматически выбирается исходя из расширения файла .csv или .json.

class ReadClient:
    def __init__(self):
        self.__client_reader = {'json': JSONReader, 'csv': CSVReader}
        self.__client_name = None

    def test_read(self, elem):
        try:
            self.__client_name = self.__client_reader[elem.rsplit('.', 1)[1].lower()]
        except TypeError:
            print('')
        if self.__client_name is None:
            return False

        return self.__client_name.test_read(new_file=elem)


# 3
# Шаблон стратегия
# Класс WriteClient содержит ссылки на JSONWriter и CSVWriter.
# Нужный драйвер выбирает пользователь с помощью метода WriteClient.set_driver(driver_name)


class WriteClient:
    def __init__(self):
        self.__client_writers = {'json': JSONWriter(), 'csv': CSVWriter()}
        self.__client_name = None

    def test_write(self, elem, data):
        if self.__client_name is None:
            return 'File Error. Choose format json or csv'

        return self.__client_name.test_write(elem, data)

    def test_driver(self, driver_name):

        try:
            self.__client_name = self.__client_writers[driver_name]
        except TypeError:
            return 'File Error'
        return True


write_client = WriteClient()
print(write_client.test_driver('txt'))
print(write_client.test_write('test_write.json', {'time': 'morning', 'action': 'go to study'}))

# 4
# Интерактивное взаимодействие с ReadClient и WriteClient.
# С помощью input() пользователь может выбрать ReadClient или WriteClient.
# Далее пользователь пишет название файл. Если WriteClient, то запрашивает формат.
# Если ReadClient, то автоматически читает файл с нужным форматом и выводит на экран в виде словаря.
# Если WriteClient, то пользователь пишет словарь в виде строки, а затем передаётся в exec.


print('\n''What do you want:\n1-Read\n2-write')
action = input('Enter your action').lower()

if action is 1:
    reader_client = ReadClient()
    print(reader_client.test_read(input('Enter your act')))
elif action is 2:
    write_client = WriteClient()
    file = input('Enter your action')
    form = input('Enter json or csv ')
    dic = input('Enter choose date ')
    try:
        print(f'data = {dic}')
    except TypeError:
        print('TypeError')
    write_client.test_driver(dic)
    write_client.test_write('.'.join([file, dic]), data=data)

# Пример:
# s = input('Enter dict> ') # s = '{'a': 1, 'c': 'r'}
# exec(f'data = {s}')
# Переменная data - это словарь.
