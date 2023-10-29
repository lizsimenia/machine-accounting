import pattern_cars, pattern_characteristic
from typing import Callable, Any, Dict
from accounting import *
path = 'C:/Users/Li Za/Desktop/study/engineering/labs/cars/functional/accounting.py'

def check_num_car(text:str) -> bool:
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

def is_no_spec(text:str) -> Any:
    ''' Функция проверки ввода на отсутствие спец символов'''
    spec = [chr(i) for i in range(33, 48)]+[chr(i) for i in range(58, 65)] +\
    [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]
    for elem in text:
        if elem in spec:
            print('ERROR: можно вводить только буквы и цифры')
            return 0
    return 1

def is_digit(num:str) -> float:
    ''' Функция проверки ввода на число '''
    try:float(num)
    except Exception: print('ERROR: введите число')
    else: return float(num)

def is_word(text:str) -> bool:
    ''' Функция проверки ввода только букв'''
    alfa = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    return all(i in alfa for i in text)

def check_a_num_choice(num:float, limit_1:float, limit_2=1) -> Any:
    '''Функция проверки числа на ограничения'''
    if num <= limit_1 and num  >= limit_2:
        return 1
    print("ERROR: введите корректное число")

def search_num(num:str) -> int:
    '''Функция нахождения машины по ее номеру'''
    index_num, index= 0, None
    with open(path, "r", encoding="UTF-8") as file:
        for line in file:
            index_num += 1
            if num in line:
                index = index_num
                break
    return index

def unique_num(num:str)->bool:
    '''Функция проверки единственности номера'''
    try:
        index = search_num(num)
        return index == None
    except Exception:
        return 1

def find_characteristic(num:str) -> Any:
    '''Функция нахождения характеристик по номеру машины'''
    try:
        index = search_num(num)
        if index is not None:
            with open(path, "r", encoding="UTF-8") as file:
                return index-1, file.readlines()
        else:
            print("ERROR: автомобиля с таким номером не существует")
    except FileNotFoundError:
        raise FileNotFoundError("В учёте нет ни одного автомобиля.")

def choose_feature(num:str) -> int:
    """
    Функция выбора одной из характеристик машины для изменения
    """
    print("Выберите характеристику для изменения:")
    variable_name = f'car_{num}'
    car = globals()[variable_name]
    list_features = []

    num= 0
    pattern_car = None
    for i, feature in enumerate(car):
        if feature == 'Назначение':
            pattern_car_init = pattern_characteristic.info_pattern['Назначение'][car['Назначение']]
        elif feature == 'Тип пассажирского транспорта':
            pattern_car = pattern_cars.pattern_passenger['Тип пассажирского транспорта'][car['Тип пассажирского транспорта']]
            continue
        elif feature == 'Грузоподъемность':
            pattern_car= pattern_cars.pattern_cargo['Грузоподъемность'][car['Грузоподъемность']]
            continue
        if i >= 4:
            num+=1
            if feature == "Габариты":
                print(feature)
                for elem in car['Габариты']:
                    print(f"{elem} ({num})")
                    list_features.append(elem)
                    num += 1
                    if elem == 'Расстояние от подвески до земли(см)':
                        num -= 1
            else:
                list_features.append(feature)
                print(f"{feature} ({num})")

    while True:
        choice = input("Введите номер характеристики: ")
        if is_digit(choice):
            if check_a_num_choice(int(choice), len(list_features)-1):
                if pattern_car == None:
                    pattern_car = pattern_car_init
                return pattern_car, pattern_car_init, list_features, int(choice)-1, car

def make_a_choice(key:str, data:None) -> int:
    """
    Функция задания характеристики из списка

    выбирает характеристику из предложенных
    с помощью ввода числа

    """
    num_list = {choice[0]: choice[1] for choice in enumerate(data)}
    print(key, ": ", *[num_list[i] + '(' + str(i+1) + ')' for i in num_list.keys()])
    while True:
        num = input( f'{key}: ')
        if is_digit(num):
            if check_a_num_choice(int(num), len(num_list)) != None:
                choice = num_list[int(num)-1]
                break
    return choice

def set_size(dict_characteristic:Dict, info_temp:Dict, characteristic:str) -> None:
    '''Функция установки габаритов машины'''
    for elem in dict_characteristic[characteristic].keys():
        while True:
            info_temp[characteristic][elem] = input(f'  {elem}: ')
            if is_digit(info_temp[characteristic][elem]):
                if len(dict_characteristic[characteristic][elem]) == 2:
                    if check_a_num_choice(float(info_temp[characteristic][elem]),
                                        max(dict_characteristic[characteristic][elem]),
                                        min(dict_characteristic[characteristic][elem])):
                           break
                else:
                    break

def spec_add_char(info_temp: Dict, root: str)-> None:
    '''Функция добавления характеристик с ограничениями'''
    dict_characteristic = root
    for characteristic in dict_characteristic:
        if characteristic == 'Габариты':
            set_size(dict_characteristic, info_temp, characteristic)

        elif isinstance(dict_characteristic[characteristic], dict):
            info_temp[characteristic] = make_a_choice(characteristic,
                                        [i for i in dict_characteristic[characteristic].keys()])

            cur_dict_char = dict_characteristic[characteristic][info_temp[characteristic]]
            for elem in cur_dict_char.keys():
                if elem == 'Габариты':
                    set_size(cur_dict_char, info_temp, elem)
                else:
                     while True:
                        info_temp[elem] = input(f'  {elem}: ')
                        if is_digit(info_temp[elem]):
                            if len(cur_dict_char[elem]) == 2:
                                if check_a_num_choice(float(info_temp[elem]),
                                        max(cur_dict_char[elem]),
                                        min(cur_dict_char[elem])):
                                          break
                            else:
                                break
        elif isinstance(dict_characteristic[characteristic], list):
            while True:
                info_temp[characteristic] = input(f'{characteristic}: ')
                if is_digit(info_temp[characteristic]):
                    if len(dict_characteristic[characteristic]) == 2:
                        if check_a_num_choice(float(info_temp[characteristic]),
                                              max(dict_characteristic[characteristic]),
                                            min(dict_characteristic[characteristic])):
                            break
                    else:
                        break


def adding()->None:
    '''Функция добавления машины в учёт'''
    info_temp = pattern_characteristic.info_pattern.copy()
    for characteristic in pattern_characteristic.info_pattern.keys():
        if characteristic == 'Назначение':
            info_temp[characteristic] = make_a_choice(characteristic, pattern_characteristic.info_pattern[characteristic])
            for elem in pattern_characteristic.info_pattern['Назначение'].keys():
                if elem == info_temp[characteristic]:
                    spec_add_char(info_temp, pattern_characteristic.info_pattern['Назначение'][elem])
                    break
        elif info_temp[characteristic] == 'str':
                while True:
                    info_temp[characteristic] = input( f'{characteristic}: ')
                    if is_no_spec(info_temp[characteristic]):
                        if characteristic == 'Производитель':
                            if is_word(info_temp[characteristic]):
                                break
                            else:
                                print("ERROR: название производителя может состоять только из букв")
                        elif characteristic == 'Номер машины':
                            if check_num_car(info_temp[characteristic]):
                                if unique_num(info_temp[characteristic]):
                                    break
                                else: print("ERROR: машина с таким номером существует в файле.")
                        else:
                            break
        elif isinstance(info_temp[characteristic], list):
            info_temp[characteristic] = make_a_choice(characteristic, info_temp[characteristic])
        elif characteristic == 'Габариты':
            pass
        else:
            info_temp[characteristic] = input( f'{characteristic}: ')
    accounting_info.append(info_temp)


def removal()->None:
    '''Функция удаления машины из учета'''
    while True:
        num = input("Введите номер машины: ")
        if check_num_car(num):
            if find_characteristic(num):
                index, lines = find_characteristic(num)
                del lines[index]
                with open(path, "w", encoding="UTF-8") as file:
                    file.writelines(lines)
                    break

def display()->None:
    '''Функция вывода учёта машин'''
    with open('accounting.txt', 'r', encoding='UTF8') as output_file:
        for s in output_file:
            print(s)

def change()->None:
    '''Функция изменения характеристики машины в учёте'''
    flag = 0
    while True:
        if flag == 1:
            break
        num = input("Введите номер машины: ")
        if check_num_car(num):
            if find_characteristic(num):
                index, lines = find_characteristic(num)
                pattern_car, pattern_car_init, list_features, index_feature, car= choose_feature(num)
                print("Внесите измненения:")
                feature = list_features[index_feature]
                try:
                    key = pattern_car_init[feature]
                    while True:
                        new_data = input(f'{feature}: ')
                        if is_digit(new_data):
                            if len(key) == 2:
                                if check_a_num_choice(float(new_data), max(key), min(key)):
                                    car[feature] = new_data
                                    new_line = str(car)
                                    break
                            else:
                                car[feature] = new_data
                                new_line = str(car)
                                break
                except Exception:
                    try:
                        key = pattern_car[feature]
                        while True:
                            new_data = input(f'{feature}: ')
                            if is_digit(new_data):
                                if len(key) == 2:
                                    if check_a_num_choice(float(new_data), max(key), min(key)):
                                        car[feature] = new_data
                                        new_line = str(car)
                                        break
                                else:
                                    car[feature] = new_data
                                    new_line = str(car)
                                    break
                    except Exception:
                        try:
                            key = pattern_car['Габариты'][feature]
                            while True:
                                new_data = input(f'{feature}: ')
                                if is_digit(new_data):
                                    if len(key) == 2:
                                        if check_a_num_choice(float(new_data), max(key), min(key)):
                                            car['Габариты'][feature] = new_data
                                            new_line = str(car)
                                            break
                                    else:
                                        car['Габариты'][feature] = new_data
                                        new_line = str(car)
                                        break
                        except Exception:
                            key = feature
                            car[feature] = make_a_choice(key, pattern_characteristic.info_pattern[feature])
                            new_line = str(car)
                lines[index-1] = f'car_{num} = ' + new_line+'\n'
                with open(path, "w", encoding="UTF-8") as file:
                    file.writelines(lines)

                flag = 1



def saving()->None:
    '''Функция сохранения информации о машине в файл'''
    with open(path, 'r', encoding='UTF8') as output_file:
        lines = output_file.readlines()
    with open(path, 'a', encoding='UTF8') as output_file:
        for cars in accounting_info:
            flag = 0
            for line in lines:
                if f'car_{cars["Номер машины"]}' in line:
                    flag = 1
                    break
            if flag == 0:
                output_file.write(f'car_{cars["Номер машины"]} = {str(cars)}\n')
                output_file.write('\n')

def menu():
    """
    Функция вызова меню

    выборка одного из предложенных действий,
    выполение соотвествующей функции выбранного действия
    """
    print(f"\n MENU\n\
          \n Выйти из меню (0)\
          \n Добавление машины в учёт (1)\
          \n Удаление машины из учета (2)\
          \n Отображение всего учёта (3)\
          \n Изменение характеристик машины (4)\
          \n Сохранение изменений (5)")
    try:
        act = int(input("\n Выберите команду (введите её номер): "))
        if act == 0:
            return 0
        elif act == 1:
            print("\nДОБАВЛЕНИЕ МАШИНЫ В УЧЁТ\n")
            adding()
        elif act == 2:
            print("\nУДАЛЕНИЕ МАШИНЫ ИЗ УЧЁТА\n")
            removal()
        elif act == 3:
            print("\nОТОБРАЖЕНИЕ ВСЕГО УЧЁТА\n")
            display()
        elif act == 4:
            print("\nИЗМЕНЕНИЕ ХАРАКТЕРИСТИКИ МАШИНЫ\n")
            change()
        elif act == 5:
            print("\nСОХРАНЕНИЕ ИЗМЕНЕНИЙ\n")
            saving()
        else:
            raise Exception
    except:
        print(f"\n\t Такой команды не существует!")

accounting_info = []

while True:
    if menu() == 0:
        print("ВЫХОД ИЗ МЕНЮ")
        break
    else:continue
