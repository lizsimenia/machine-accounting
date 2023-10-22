# purpose = {pattern_cargo, pattern_passenger, pattern_cargo_passenger,pattern_special}


class Parking:
    """
    Базовый класс, описывающий все машины на парковке

    Args:
    Methods:

    """
    parking = []

    def add(self, car):
        '''Функция добавления машины в учёт'''
        self.parking.append(car)

    def get(self):
        '''Функция геттер учёта'''
        return self.parking

    def remove_car(self, car):
        '''Функция удаления машины из учёта'''
        return self.parking.pop(car)


class Car:
    """
    Базовый класс, описывающий любую машину

    Args:
    Methods:

    """
    def __init__(self, num_car, manufacturer, the_lineup, year, purpose):
        self.manufacturer = manufacturer
        self.the_lineup = the_lineup
        self.year = year
        self.purpose = purpose

        self.characteristics = {}

    def get_characteristic(self, key):
        return self.characteristics.get(key)

    def set_characteristic(self):
        key = input("Какую характеристику изменить?")
        value = input("Введите новые данные:")
        self.characteristics[key] = value

    def remove_characteristic(self):
        key = input("Какую характеристику удалить? ")
        if key in self.characteristics:
            del self.characteristics[key]
            print(f"{key} удалена.")
        else:
            print("Характеристика не найдена.")

    def display_characteristics(self):
        print(f"\nХАРАКТЕРИСТИКИ {self.make} {self.model} ({self.year}):")
        for key, value in self.characteristics.items():
            print(f"{key}: {value}")

class CargoCar(Car):
    """
    Класс CargoCar (грузовой автомобиль). Родитель: Car

    Args:

    Methods:

    """
    pass

# class CargoCar(Car):
#     pass

# class CargoCar(Car):
#     pass

# class CargoCar(Car):
#     pass
