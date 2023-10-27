from typing import Callable, Any, Dict, Self

from tkinter import *

root = Tk()
root.title("machine accounting")
root.geometry("800x600")

# Create a list of options for the dropdown menu
options = ["грузовой", "пассажирский", "грузопассажирский", "специальный"]

# Create a StringVar to store the selected option
selected_option = StringVar(root)
selected_option.set(options[0])  # Set the default option

# Create the OptionMenu widget and add it to the window
option_menu = OptionMenu(root, selected_option, *options)
option_menu.pack()

# Add more widgets and event handlers here

root.mainloop()


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
    def __init__(self):
        self.numcar = self.set_numcar()
        self.manufacturer = self.set_manufacturer()
        self.the_lineup = self.set_lineup()
        self.year = self.set_year()
        self.purpose = self.set_purpose()


    def check_numcar(self, text:str) -> Any:
        '''Функция проверки корректности номера машины'''
        try:
            if len(text) >= 8\
                and text[0] in 'АВЕКМНОРСТУХ' and (0 <= int(text[1:4]) < 1000)\
                and text[4] in 'АВЕКМНОРСТУХ'\
                and text[5] in 'АВЕКМНОРСТУХ'and (0 <= int(text[-2:]) < 1000):
                    return 1
            else: raise Exception
        except Exception:
            print("ERROR: некорректный номер машины")

    def set_numcar(self)->Any:
        '''Сеттер номера машины'''
        num =  input("Номер машины: ")
        if self.check_numcar(num):
            return num

    def set_manufacturer(self):
        '''Сеттер производителя'''
        data = input("Производитель: ")
        return data

    def set_lineup(self):
        '''Сеттер модельного ряда'''
        pass

    def set_year(self):
        '''Сеттер года выпуска машины'''
        pass

    def set_purpose(self):
        '''Сеттер назначения машины'''
        data = input("Назначение: ")
        #выборка назначений из выходящего списка
        pass

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

Car()

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
