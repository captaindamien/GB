"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево)
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police:
            return f"Вы включили сирену\n{self.name} поехала"
        return f"{self.name} поехала"

    def stop(self):
        return f"{self.name} остановилась"

    def turn_left(self):
        return f"{self.name} повернула влево"

    def turn_right(self):
        return f"{self.name} повернула вправо"

    def show_speed(self):
        return f"Скорость {self.name} составляет {self.speed} км/ч"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Вы превысили скорость! Снизбте скорость до 40 км/ч"
        else:
            return f"Скорость {self.name} составляет {self.speed} км/ч"


class SportCar(Car):
    def go(self):
        return f"Режим 'Шашечник' включен\n{self.name} поехала"

    def show_speed(self):
        if self.speed < 120:
            return f"Че так медленно?! Разгоняйся до 120 км/ч минимум!"
        else:
            return f"Скорость {self.name} составляет {self.speed} км/ч"


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Вы превысили скорость! Снизьте скорость до 40 км/ч"
        else:
            return f"Скорость {self.name} составляет {self.speed} км/ч"


class PoliceCar(Car):
    def werewolfs_with_straps(self):
        return f"Теперь вы можете нарушать ПДД\nТеперь вы можете брать взятки"


first_car = PoliceCar(70, "White", "Musorovoz", True)
print(first_car.go())
print(first_car.show_speed())
print(first_car.werewolfs_with_straps())
print("\n")
second_car = SportCar(90, "Red", "PushkaGonka", False)
print(second_car.go())
print(second_car.turn_left())
print(second_car.show_speed())
