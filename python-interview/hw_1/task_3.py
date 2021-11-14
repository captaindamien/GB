"""3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации (нуль
необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря. """
from time import time


def random_generator(first_num: int, second_num: int) -> str:
    random_list = []
    random_dict = {}

    for i in range(first_num, second_num + 1):
        sub = second_num - first_num
        time_number = int(time() * i)
        time_number %= sub

        if time_number != 0:
            random_list.append(time_number)
            random_dict[f'elem_{i}'] = time_number

    return f'{random_list}\n{random_dict}'


print(random_generator(100, 150))
