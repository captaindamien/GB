"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def write_numbers(file_name, file_arg, u_input):
    with open(file_name, file_arg) as numbers_file:
        for number in u_input:
            numbers_file.write(f"{number} ")
    print(sum_numbers(user_numbers))


def sum_numbers(num):
    return sum([int(el) for el in num])


user_numbers = input("Введите числа через пробел: ").split()
write_numbers("task_5_file.txt", "w", user_numbers)
