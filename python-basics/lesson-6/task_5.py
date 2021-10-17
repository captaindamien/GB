"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки."


class Pen(Stationary):
    def draw(self):
        return f"У вас в руке {self.title}. Вы пишете синей пастой."


class Pencil(Stationary):
    def draw(self):
        return f"У вас в руке {self.title}. Вы рисуете скетч."


class Handle(Stationary):
    def draw(self):
        return f"У вас в руке {self.title}. Вы подводите заметки."


handle = Handle("ручка")
print(handle.draw())
pencil = Pencil("карандаш")
print(pencil.draw())
pen = Pen("карандаш")
print(pen.draw())
