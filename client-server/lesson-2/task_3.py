"""
Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
Для этого:

a. Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
отсутствующим в кодировке ASCII (например, €);

b. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
а также установить возможность работы с юникодом: allow_unicode = True;

c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import os
import yaml

DATA_PATH = r'data/task_3/'
RESULT_PATH = r'result/task_3/'
DATA = {'first': [1, 2, 3],
        'second': 100,
        'third': {"one": 1,
                  "two": 2,
                  "three": 3}
        }


def write_yaml(data):
    with open(os.path.join(RESULT_PATH, 'result_yaml.yaml'), 'w', encoding='utf-8') as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)


def read_yaml():
    with open(os.path.join(RESULT_PATH, 'result_yaml.yaml'), 'r', encoding='utf-8') as file:
        yaml_reader = yaml.load(file, Loader=yaml.FullLoader)
    print(yaml_reader)


write_yaml(DATA)
read_yaml()

