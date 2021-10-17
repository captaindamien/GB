"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod
from random import randint


class Cloth(ABC):
    @property
    @abstractmethod
    def formula(self):
        pass

    @staticmethod
    def sum_cloth(lst):
        result = 0
        for el in lst:
            result += el.formula
        return round(result, 2)


class Coat(Cloth):
    def __init__(self, v):
        self.v = v

    @property
    def formula(self):
        return round(self.v / 6.5 + 0.5, 2)


class Costume(Cloth):
    def __init__(self, h):
        self.h = h

    @property
    def formula(self):
        return 2 * self.h + 0.3


#  сгенерировал случайный размерный ряд для проверки
common_cloth = []
for count in range(0, 4, 2):
    common_cloth.append(Costume(randint(1, 15)))
    common_cloth.append(Coat(randint(1, 15)))

print(Cloth.sum_cloth(common_cloth))
