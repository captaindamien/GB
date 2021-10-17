"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"Имя сотрудника: {self.name} {self.surname}"

    def get_position(self):
        return f"Должность сотрудника: {self.position}"

    def get_total_income(self):
        return f"Зарплата: {self._income['wage'] + self._income['bonus']}"


worker_2 = Position("Егор", "Карпушин", "Инженер-программист", {"wage": 50000, "bonus": 30000})
print(worker_2.get_full_name())
print(worker_2.get_position())
print(worker_2.get_total_income())
print("\n")
worker_2 = Position("Николай", "Свиридов", "Программист", {"wage": 50000, "bonus": 53000})
print(worker_2.get_full_name())
print(worker_2.get_position())
print(worker_2.get_total_income())
