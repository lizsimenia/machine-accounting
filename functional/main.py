# TODO: подключить файл со всеми словарями и брать инфу из него
import pattern_cars, pattern_characteristic
from typing import Callable, Any, Dict

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
    return 1

def is_digit(num:str) -> float:
    ''' Функция проверки ввода на число '''
    try:float(num)
    except Exception: print('ERROR: введите число\n')
    else: return float(num)

def is_word(text:str) -> bool:
    ''' Функция проверки ввода только букв'''
    return text.isalpha()

def check_a_num_choice(num:float, limit_1:float, limit_2=1) -> Any:
    '''Функция проверки числа на ограничения'''
    if num <= limit_1 and num  >= limit_2:
        return 1
    print("ERROR: введите корректное число\n")

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
    """
    Функция установки габаритов машины

    запрашивает длину, ширину, высоту
    или расстояние от подвески до земли
    """
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
    """
    Функция добавления характеристик с ограничениями,
    зависящие от назначения автомобили

    добавляет новые характеристики машине
    """
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


def adding():
    """
    Функция добавления машины в учёт

    задает и добавляет характеристики машины
    """
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
                                break
                        else:
                            break
        elif isinstance(info_temp[characteristic], list):
            info_temp[characteristic] = make_a_choice(characteristic, info_temp[characteristic])
        elif characteristic == 'Габариты':
            pass
        else:
            info_temp[characteristic] = input( f'{characteristic}: ')
    accounting_info.append(info_temp)



def removal():
    # TODO:
    """
    Функция удаления машины из учета

    удаляет все характеристики по номеру машины
    """
    while True:
        num = input("Введите номер машины: ")
        if check_num_car(num):
            break
    try:
        with open("accounting.txt", "r", encoding="UTF-8") as file:
            lines = file.readlines()

        paragraph_start = f"Номер машины: {num}\n"
        paragraph_end = "\n"

        start_index = None
        end_index = None

        for i, line in enumerate(lines):
            if line == paragraph_start:
                start_index = i
            elif line == paragraph_end:
                end_index = i
                break

        if start_index is not None and end_index is not None:
            del lines[start_index:end_index+1]
            with open("accounting.txt", "w", encoding="UTF-8") as file:
                file.writelines(lines)
        else:
            print("ERROR: ")

    except FileNotFoundError:
        raise FileNotFoundError("В учёте нет ни одного автомобиля.")

def display():
    """
    Функция вывода учёта машин

    выводит характеристики каждой машины

    :rtype: list
    :return:
    """
    with open('accounting.txt', 'r', encoding='UTF8') as output_file:
        for s in output_file:
            print(s)

def change(init_list):
    """
    Функция изменения характеристики машины в учёте

    задает и добавляет характеристики машины

    :rtype: list
    :return:
    """
    pass

def saving()->None:
    """
    Функция добавления машины в учёт

    задает и добавляет характеристики машины
    """
    with open('accounting.txt', 'w', encoding='UTF8') as output_file:
        for cars in accounting_info:
            for key, value in cars.items():
                if isinstance(value, dict):
                    output_file.write(key + ': '+'\n')
                    for i in value.keys():
                        output_file.write('  ' + i + ': ' + str(value[i]) +'\n')
                else:
                    output_file.write(key + ': ' +  str(value)+'\n')
            output_file.write("\n")

def menu():
    """
    Функция вызова меню

    выбирает одно из предложенных действий,
    выполняет соотвествующую функцию выбранного действия
    """
    print(f"\n MENU\n\
          \n Выйти из меню (0)\
          \n Добавление машины в учёт (1)\
          \n Удаление машины из учета (2)\
          \n Отображение всего учёта (3)\
          \n Изменение характеристик машины (4)\
          \n Сохранение изменений (5)")
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
        print(f"\n\t Такой команды не существует!")

accounting_info = []

while True:
    if menu() == 0:
        print("ВЫХОД ИЗ МЕНЮ")
        break
    else:continue
