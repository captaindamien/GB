"""
Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь
значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра
поместить в соответствующий список. Должно получиться четыре списка — например,
os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения данных
отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

c. Проверить работу программы через вызов функции write_to_csv().
"""
import csv
import os

DATA_PATH = r'data/task_1/'
RESULT_PATH = r'result/task_1/'
DATA_PATH_FILES = os.listdir(DATA_PATH)
SEARCH_ELEMENTS = ['Название ОС', 'Код продукта', 'Изготовитель системы', 'Тип системы']


# функция открытия файла
def get_data():
    result_data = []

    # перебор по всем файлам в директории DATA_PATH
    for filename in DATA_PATH_FILES:
        result_dict = {}

        with open(os.path.join(DATA_PATH, filename)) as file:
            file_reader = csv.reader(file)
            # перебор строк в файле
            for row in file_reader:
                # перебор элементов в строке файла
                for elem in row:
                    # разбиение по двоеточию
                    split_element = elem.split(':')
                    # проверка на совпадение первого элемента с искомыми
                    if split_element[0] in SEARCH_ELEMENTS:
                        # добавление в итоговый словарь (в значении удаляются пробелы спереди .strip())
                        result_dict[f'{split_element[0]}'] = f'{split_element[1].strip()}'

        result_data.append(result_dict)
    # вызов функции для записи итогового файла
    write_to_csv(result_data)


# функция записи итогового файла
def write_to_csv(result_data: list):
    with open(os.path.join(RESULT_PATH, 'result_csv.csv'), 'w', encoding='utf-8') as file:
        file_writer = csv.DictWriter(file, fieldnames=result_data[0].keys())  # указываем на заголовки
        file_writer.writeheader()
        # перебор словарей списка
        for data in result_data:
            file_writer.writerow(data)  # построчная запись данных в csv


get_data()
