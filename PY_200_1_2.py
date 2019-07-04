# Разработка класса данных
# 7
import calendar


class Date:
    """Date
    Example:
    date = Date(2019, 5, 22)
    print(date)"""
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  #
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  #

    def __init__(self, year, month, day):
        """year:  int otherwise TypeError
        month: int 1 < month <= 12"""

        self.is_valid_date(year, month, day)
        self.__year = year
        self.__month = month
        self.__day = day

    def __str__(self):
        return self.date

    def __repr__(self):
        return f'Date({self.__year!r}, {self.__month!r}, {self.__day!r})'

    @staticmethod
    def is_leap_year(year):
        is_calendar = calendar.isleap(year)
        return is_calendar

    @classmethod
    def get_max_day(cls, year, month):
        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month - 1]

    @property
    def date(self):
        return f'{self.__day}.{self.__month}.{self.__year}'

    @classmethod
    def is_valid_date(cls, year, month, day):
        if not isinstance(year, int):
            raise TypeError('year must be int')
        if not isinstance(month, int):
            raise TypeError('month must be int')
        if not isinstance(day, int):
            raise TypeError('day must be int')

        if not 0 < month <= 12:
            raise ValueError('month must be 0 < month <= 12')

        if not 0 < day <= cls.get_max_day(year, month):
            raise ValueError('invalid day for this month and year')

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError('Date must be str')
        value = value.split('.')
        if len(value) != 3:
            raise ValueError('Invalid date format')

        try:
            day = int(value[0])
            month = int(value[1])
            year = int(value[2])
            self.is_valid_date(year, month, day)
        except:
            raise ValueError('Invalid date format')

        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        value = int(value)
        self.is_valid_date(self.__year, self.__month, value)
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        value = int(value)
        self.is_valid_date(self.__year, value, self.__day)
        self.__month = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        value = int(value)
        self.is_valid_date(value, self.__month, self.__day)
        self.__year = value

    def add_day(self, day):
        for _ in range(day):
            self.__day += 1
            cycle = self.__month + 1 if self.__month != 12 else 1
            leap_year = 1 if self.is_leap_year(self.__year) else 0
            if self.DAY_OF_MONTH[leap_year][cycle - 1] == self.__day:
                self.month += 1
                self.__day = 1
                if self.__month == 13:
                    self.__year = 1
                    self.__month = 1
                    self.__day = 1
                continue

    def add_month(self, month):
        for _ in range(month):
            if self.__month == 12:
                self.__year += 1
                self.__month = 1
                continue

            cycle = self.__month + 1 if self.__month != 12 else 1
            leap_year = 1 if self.is_leap_year(self.__year) else 0
            if self.DAY_OF_MONTH[leap_year][cycle - 1] < self.__day:
                self.month += 1
                self.__day = 1
                continue
            self.month += 1

    def add_year(self, year):
        if year > 0:
            for _ in range(year):
                if self.day == 29 and self.is_leap_year(year):
                    self.month = 3
                    self.day = 1
                self.__year += 1

    @staticmethod
    def date2_date1(date2, date1):
        pass
        # date2-date1


first_date = Date(2019, 6, 7)
print(first_date)
first_date.add_day(7)
print(first_date)
first_date.add_month(6)
print(first_date)
first_date.add_year(5)
print(first_date)