main_characteristic = {}
accounting_info = []
# номер машины, от которого всё зависит
# TODO: во всем коде нельзя  ".keys", "isinstance()", "enumerate()", asci символы кроме букв и цифр прописать самоятельно
#       найти как реализовать поиск по файлу, удаление целого модуля из него и изменение одной характеристики
#       можно ли использовать методы классы в процедурном программировании?

pattern_mal_cargo = {'Количество паллет (шт)': [4, 6],
                     'Габариты': {'Длинa кузова(м)': [2, 4], 'Ширина кузова(м)':[1.8,2],'Высота кузова(м)':[1.8,2.4]},
                    'Масса(т)': [],
                    'Рабочий объем двигателя(л)': [],
                    'Максимальная скорость(км/ч)': []}

pattern_sr_cargo = {'Количество паллет (шт)': [12, 18],
                    'Габариты': {'Длинa кузова(м)': [3.5, 7.2], 'Ширина кузова(м)':[1.9, 2.45],'Высота кузова(м)':[1.9, 2.7]},
                    'Масса(т)': [],
                    'Рабочий объем двигателя(л)': [],
                    'Максимальная скорость(км/ч)': []}

pattern_bol_cargo = {'Количество паллет (шт)': [20, 33],
                     'Габариты': {'Длинa кузова(м)': [5.8, 8], 'Ширина кузова(м)':[2.3, 2.45],'Высота кузова(м)':[2.2, 2.7]},
                    'Масса(т)': [],
                    'Рабочий объем двигателя(л)': [],
                    'Максимальная скорость(км/ч)': []}

pattern_ochbol_cargo = {'Количество паллет (шт)': [33, 50],
                        'Габариты': {'Длинa кузова(м)': [13.6, 16], 'Ширина кузова(м)':[2.4, 2.5],'Высота кузова(м)':[2.5, 3.1]},
                        'Масса(т)': [],
                        'Рабочий объем двигателя(л)': [],
                        'Максимальная скорость(км/ч)': []}

pattern_cargo = {'Количество мест': [2,3],
                 'Грузоподъемность': {'малый (0.5-2т)': pattern_mal_cargo, 'средний (2-5т)': pattern_sr_cargo,
                                      'большой(5-16т)': pattern_bol_cargo, 'сверхтяжелый(от 16т)': pattern_ochbol_cargo}} #грузовой


#пассажирский
pattern_bus = {'Количество мест': [40, 150],
               'Габариты': {'Длинa кузова(м)': [4.5,20], 'Ширина кузова(м)':[1.5, 2.55],'Расстояние от подвески до земли(см)':[15, 20]},
               'Масса(т)': [10, 28],
               'Рабочий объем двигателя(л)': [2, 4.43],
               'Максимальная скорость(км/ч)': [60, 120]}
pattern_pas = {'Количество мест': [2, 8],
               'Габариты': {'Длинa кузова(м)': [3.8,6.1], 'Ширина кузова(м)':[1.5, 2.55],'Расстояние от подвески до земли(см)':[15, 20]},
               'Масса(т)': [1, 2.5],
               'Рабочий объем двигателя(л)': [1, 15],
               'Максимальная скорость(км/ч)': [60, 300]}
pattern_passenger = {'Тип пассажирского транспорта':{'автобус': pattern_bus,'легковой': pattern_pas}}

#грузопассажирский
pattern_cargo_passenger =  {'Количество мест': [5, 12],
                            'Габариты': {'Длинa кузова(м)': [2, 8], 'Ширина кузова(м)':[1.8, 2.5],'Расстояние от подвески до земли(см)':[15, 20]},
                            'Масса(т)': [4, 9],
                            'Рабочий объем двигателя(л)': [2,12],
                            'Максимальная скорость(км/ч)': [60, 95]}

#специальный
pattern_special = {'Количество мест': [],
                   'Габариты': {'Длинa кузова(м)': [], 'Ширина кузова(м)':[],'Расстояние от подвески до земли(см)':[]},
                   'Масса(т)': [],
                    'Рабочий объем двигателя(л)': [],
                    'Максимальная скорость(км/ч)': []}


body = {'однообъёмный': ['микроавтобус', 'минивэн'],
        'двухобъёмными': ['универсал', 'хэтчбек', 'минивэн', 'комби', 'лифтбек', 'фастбэк',
                                        'шутингбрейк', 'комби', 'внедорожник', 'кроссовер'],
        'трёхобъёмный': ['седан', 'купе', 'лимузин', 'хардтоп', 'кабриолет']}

info_pattern = {'Производитель': 'str',
                'Модельный ряд': 'str',
                'Номер машины': 'str',
                # 'Классификация кузова по объёмам': ['однообъёмный','двухобъёмными','трёхобъёмный'],
                # 'Тип кузова': {'Классификация кузова по объёмам': body},
                'Назначение' : {'грузовой': pattern_cargo , 'пассажирский': pattern_passenger,
                                'грузопассажирский': pattern_cargo_passenger, 'специальный': pattern_special},
                'Тип двигателя': ['бензиновые', 'дизельные', 'газовые', 'газодизельные', 'роторно-поршневые'],
                'Тип привода': ['задний', 'передний', 'полный'],
                'Тип коробки передач': ['механическая', 'автоматическая', 'роботизированная', 'вариативная (бесступенчатая)'],
                'Габариты': {'Длинa кузова(м)': [], 'Ширина кузова(м)':[],'Расстояние от подвески до земли(см)':[]}}
                #, #3 цифры
                # 'Масса': 'Назначение',
                # 'Рабочий объем двигателя': 'Назначение',
                # 'Максимальная скорость': 'Назначение'

counter = 0
while True:
    #меню
    print(f"\n MENU\n\
          \n Выйти из меню (0)\
          \n Добавление машины в учёт (1)\
          \n Удаление машины из учета (2)\
          \n Отображение всего учёта (3)\
          \n Изменение характеристик машины (4)\
          \n Сохранение изменений (5)")
    act = int(input("\n Выберите команду (введите её номер): "))

    if act == 0:
        break

    # добавление в учёт
    elif act == 1:
        print('\nВВОД ОСНОВНЫХ ХАРАКТЕРИСТИК\n')
        # info_temp = info_pattern.copy()
        info_temp = dict()
        for elem in info_pattern:
            info_temp[elem] = []
        # for characteristic in info_pattern.keys():
        for characteristic in info_pattern:
            #проверка ввода числа или текста
            while True:
                flag = 0
                if characteristic == 'Назначение':
                    list_nazn = []
                    for elem in info_pattern[characteristic].keys():
                        list_nazn.append(elem)
                    num_list = {choice[0]: choice[1] for choice in enumerate(list_nazn)}
                    flag = 1
                elif characteristic == 'Габариты':
                    break
                elif isinstance(info_pattern[characteristic], list):
                    num_list = {choice[0]: choice[1] for choice in enumerate(info_pattern[characteristic])}
                    flag = 1

                elif isinstance(info_pattern[characteristic], dict):
                    init_key = [i for i in info_pattern[characteristic].keys()]
                    characteristic_init = info_temp[init_key[0]]
                    num_list = {choice[0]: choice[1] for choice in enumerate(info_pattern[characteristic][init_key[0]][characteristic_init])}
                    flag = 1

                elif info_pattern[characteristic] == 'str':
                    while True:
                        info_temp[characteristic] = input( f'{characteristic}: ')
                        text = info_temp[characteristic]
                        spec = [chr(i) for i in range(33, 48)]+[chr(i) for i in range(58, 65)] + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]
                        for elem in text:
                            if elem in spec:
                                print('ERROR: можно вводить только буквы и цифры')
                                break
                        else:
                            try:
                                float(info_temp[characteristic])
                            except Exception:
                                flag = 2
                                break
                            else:
                                print("ERROR: текст должен содержать буквы\n")

                if flag == 1:
                    while True:
                        print(characteristic, ": ", *[num_list[i] + '(' + str(i+1) + ')' for i in num_list.keys()])
                        try:
                            num = int(input( f'{characteristic}: ')) - 1
                            if num+1 > len(num_list) or num + 1 <= 0:
                                raise Exception
                        except Exception:
                            print("ERROR: введите цифры из предложенного списка\n")
                        else:
                            info_temp[characteristic] = num_list[num]
                            break
                    if characteristic == 'Назначение':
                        root = info_temp['Назначение']
                        for elem in info_pattern['Назначение'].keys():
                            if elem == root:
                                dict_characteristic = info_pattern['Назначение'][elem]
                                break
                        for characteristic in dict_characteristic:
                            if characteristic == 'Габариты':
                                for elem in dict_characteristic[characteristic].keys():
                                    while True:
                                        try:
                                            info_temp[characteristic][elem] = float(input(f'  {elem}: '))
                                            if len(dict_characteristic[characteristic][elem]) == 2:
                                                if min(dict_characteristic[characteristic][elem]) <= info_temp[characteristic][elem]\
                                                    and max(dict_characteristic[characteristic][elem]) >= info_temp[characteristic][elem]:
                                                    pass
                                                else:
                                                    raise Exception
                                        except Exception:
                                            print("ERROR:  введите подходящее число для вашего автомобиля\n")
                                        else:
                                            break
                            elif isinstance(dict_characteristic[characteristic], dict):
                                keys_ch = [i for i in dict_characteristic[characteristic].keys()]
                                num_list = {choice[0]: choice[1] for choice in enumerate(keys_ch)}
                                while True:
                                    print(characteristic, ": ", *[num_list[i] + ' (' + str(i+1) + ')' for i in num_list.keys()])
                                    try:
                                        num = int(input( f'{characteristic}: ')) - 1
                                        if num+1 > len(num_list) or num + 1 <= 0:
                                            raise Exception
                                    except Exception:
                                        print("ERROR: введите цифры из предложенного списка\n")
                                    else:
                                        info_temp[characteristic] = num_list[num]
                                        break

                                cur_dict_char = dict_characteristic[characteristic][info_temp[characteristic]]
                                if isinstance(cur_dict_char, dict):
                                    pass
                                for elem in cur_dict_char.keys():
                                    if elem == 'Габариты':
                                        info_temp[elem]= {}
                                        for i_elem in cur_dict_char[elem]:
                                            while True:
                                                try:
                                                    info_temp[elem][i_elem] = float(input(f'  {i_elem}: '))
                                                    if len(cur_dict_char[elem][i_elem]):
                                                        if min(cur_dict_char[elem][i_elem]) <= info_temp[elem][i_elem]\
                                                            and max(cur_dict_char[elem][i_elem]) >= info_temp[elem][i_elem]:
                                                            pass
                                                        else:
                                                            raise Exception
                                                except Exception:
                                                    print("ERROR:  введите подходящее число для вашего автомобиля\n")
                                                else:
                                                    break
                                    else:
                                        while True:
                                            try:
                                                info_temp[elem] = float(input(f'  {elem}: '))
                                                if len(cur_dict_char[elem]) == 2:
                                                    if min(cur_dict_char[elem]) <= info_temp[elem]\
                                                    and max(cur_dict_char[elem]) >= info_temp[elem]:
                                                            pass
                                                    else:
                                                        raise Exception
                                            except Exception:
                                                print("ERROR:  введите подходящее число для вашего автомобиля\n")
                                            else:
                                                break
                                flag = 2

                            else:
                                while True:
                                    try:
                                        info_temp[characteristic] = float(input( f'{characteristic}: '))
                                        if len(dict_characteristic[characteristic]) == 2:
                                            if min(dict_characteristic[characteristic]) <= info_temp[characteristic]\
                                            and max(dict_characteristic[characteristic]) >= info_temp[characteristic]:
                                                pass
                                            else:
                                                raise Exception
                                    except Exception:
                                        print("ERROR: введите подходящее число для вашего автомобиля\n")
                                    else:
                                        break
                    break

                elif flag == 2:
                    break


                # if flag == 0:#любой тип для новых характеристик
                #     break
        accounting_info.append(info_temp)

    # удаление машины из учёта по производителю и модельному ряду
    elif act == 2:
        print("\nУДАЛЕНИЕ МАШИНЫ ИЗ УЧЁТА\n")
        while True:
            # удаление из словаря
            if flag == 1:
                break
            manufacturer = input("Введите производителя машины: ")
            try:
                float(info_temp[characteristic])
            except Exception:
                for i in accounting_info:
                    if manufacturer == i['Производитель']:
                        while True:
                            the_lineup = input("Введите модельный ряд: ")
                            try:
                                float(info_temp[characteristic])
                            except Exception:
                                if i['Модельный ряд'] == the_lineup:
                                    accounting_info.pop(accounting_info.index(i))
                                    flag = 1
                                    break
                                else:
                                    print("ERROR: Машины такого производителя и модельного не существует в учёте.")
                            else:
                                print("ERROR: Некорректный ввод.")
                else:
                    print("ERROR: Машины такого производителя не существует в учёте.")
            else:
                print("ERROR: Некорректный ввод.")

            #                      или
            # поиск по названию в файле, ошибка, если ненаход
            # если наход, то модель, поиск по названию и по модели
            # если наход, то запись строчек до находа и после пустой строки
                    # flag = 0
        # while True:
        #     if flag == 1:
        #         break
        #     manufacturer = input("Введите производителя машины: ")
        #     try:
        #         float(info_temp[characteristic])
        #     except Exception:
        #         print("ERROR: Название должно состоять из букв\n")

    elif act == 3:
        with open('accounting.txt', 'r', encoding='UTF8') as output_file:
            for s in output_file:
                print(s)

    #TODO
    # 1. выбор характеристики с помощью цикла, проверка на значение
    # 2. вставить код из 1ого для выбора
    elif act == 4:
        print("\nИЗМЕНЕНИЕ ХАРАКТЕРИСТИКИ МАШИНЫ\n")
        flag = 0
        #определение машины
        while True:
            if flag == 1:
                break
            manufacturer = input("Введите производителя машины: ")
            try:
                float(info_temp[characteristic])
            except Exception:
                for i in accounting_info:
                    if manufacturer == i['Производитель']:
                        while True:
                            the_lineup = input("Введите модельный ряд: ")
                            try:
                                float(info_temp[characteristic])
                            except Exception:
                                if i['Модельный ряд'] == the_lineup:
                                    cur_car = i
                                    flag = 1
                                    break
                                else:
                                    print("ERROR: Машины такого производителя и модельного не существует в учёте.")
                            else:
                                print("ERROR: Некорректный ввод.")
                else:
                    print("ERROR: Машины такого производителя не существует в учёте.")
            else:
                print("ERROR: Некорректный ввод.")
        while True:
            print("Выберите характеристику для изменения:\n\
                      1) Производитель\n\
                      2) Модельный ряд\n\
                      3) Назначение\n\
                      4) Количество мест\n\
                      5) Габариты\n\
                      6) Масса\n\
                      7) Рабочий объем двигателя\n\
                      8) Максимальная скорость")
            try:
                cur_characteristic = int(input('Введите номер характеристики для изменения:'))
                if 0 > cur_characteristic or cur_characteristic > 8:
                    raise Exception
            except Exception:
                print('ERROR: Введите корректный номер характеристики.')
            else:
                pass

            # if cur_characteristic:
            #     pass


        # print("Выберите характеристику для изменения:\n\
        #               1) Производитель\n\
        #               2) Модельный ряд\n\
        #               3) Назначение\n\
        #               4) Тип кузова\n\
        #               5) Тип двигателя\n\
        #               6) Тип привода\n\
        #               7) Тип коробки передач\n\
        #               8) Количество мест\n\
        #               9) Габариты\n\
        #               10) Масса\n\
        #               11) Рабочий объем двигателя\n\
        #               12) Максимальная скорость")
        # while True:
        #     try:
        #         num_ch = int(input())
        #     except Exception:
        #         pass
        #     else:
        #         if num_ch in range(1, 12+1):
        #             print(i[num_charac[num_ch]])
        #             i[num_charac[num_ch]] = input( f'{num_charac[num_ch]}: ')
        #             break
        #         else:
        #             print("ERROR: Характеристики с таким номером не существует.")

    elif act == 5:
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
        #форматировать всю инфу из списка
        #перезаписать

    else:
        print(f"\n\t Такой команды не существует!")


    #то есть пока не сохранился, файл не перезаписался
