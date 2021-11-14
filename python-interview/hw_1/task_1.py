"""1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB. Первый и второй множитель должны
задаваться в виде аргументов функции. Значения каждой строки таблицы должны быть представлены списком,
который формируется в цикле. После этого осуществляется вызов внешней lambda-функции, которая формирует на основе
списка строку. Полученная строка выводится в главной функции. Элементы строки (элементы таблицы умножения) должны
разделяться табуляцией.
"""


def multiply_table(length: int, height: int):
    multiply_list: list = []

    for i in range(1, length + 1):
        multiply_list.append('\n')
        for j in range(1, height + 1):
            multiply_list.append(str(i * j))

    result_str(multiply_list)


result_str = lambda convert_table: print('\t'.join(convert_table))

multiply_table(9, 9)
