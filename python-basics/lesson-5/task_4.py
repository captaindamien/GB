"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый файл.
"""


def eng_rus_swap(orig_filename, dest_filename, dct):
    with open(orig_filename, "r") as eng_file:
        with open(dest_filename, "w", encoding="utf-8") as rus_file:
            for key, value in dct.items():
                lines = eng_file.readline().lower()
                lines = lines.replace(key, value).title()
                rus_file.write(lines)


d = {"one": "один", "two": "два", "three": "три", "four": "четыре"}
eng_rus_swap(r"task_4_eng_file.txt", r"task_4_rus_file.txt", d)
