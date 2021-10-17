"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class ZeroErr(ZeroDivisionError):
    def __init__(self, txt):
        super().__init__(txt)


user_number_1 = int(input("Введите число-делитель: "))
user_number_2 = int(input("Введите делимое число: "))

try:
    if user_number_2 == 0:
        raise ZeroErr("Делимое равно нулю!")
except ZeroErr as err:
    print(err)
else:
    print(user_number_1 / user_number_2)
