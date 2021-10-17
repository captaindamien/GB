"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def valid(date_str):
        day, month, year = map(int, date_str.split('-'))
        if day <= 31 and month <= 12:
            return day, month, year


date = Date.date("03-11-2020")
val_date = Date.valid("03-11-2020")
print(val_date)
