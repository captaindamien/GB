"""
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:

a. Создать функцию write_order_to_json(), в которую передается 5 параметров —
товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;

b. Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import os
import json

DATA_PATH = r'data/task_2/'
RESULT_PATH = r'result/task_2/'
ITEMS_LIST = ['товар', 'количество', 'цена', 'покупатель', 'дата']
PRODUCTS_LIST = [
    ['Ноутбук', 5, 50000, 'Иванов И.И.', '25.10.2021'],
    ['Телефон', 15, 60000, 'Петров П.П.', '16.10.2021'],
    ['Планшет', 25, 70000, 'Сидоров С.С.', '07.10.2021'],
    ['Зарядка', 35, 80000, 'Котов К.К.', '01.10.2021'],
 ]


# функция для формирования списка словарей с данными из пользовательских данных
def fill_result_dict(product_list: list):
    result_list = []

    # перебор по всем спискам с данными
    for product in product_list:
        result_dict = {}

        # формирование словаря
        for i in range(len(product)):
            result_dict[f'{ITEMS_LIST[i]}'] = product[i]

        # добавление в список для записи
        result_list.append(result_dict)
    # вызов функции записи в json
    write_order_to_json(result_list)


# функция записи в json по json-шаблону
def write_order_to_json(result_list: list):
    # открытие json-шаблона
    with open(os.path.join(DATA_PATH, 'orders.json'), encoding='utf-8') as file:
        json_data = json.load(file)

    json_data['orders'] = result_list

    # запись в json-файл
    with open(os.path.join(RESULT_PATH, 'orders.json'), 'w', encoding='utf-8') as new_file:
        json.dump(json_data, new_file, indent=4, ensure_ascii=False)


fill_result_dict(PRODUCTS_LIST)
