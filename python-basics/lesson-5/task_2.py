"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def lines_count(file_name):
    with open(file_name, "r") as history_of_little_txt:
        lines = history_of_little_txt.readlines()
        print(f"Количество строк в файле {file_name}: {len(lines)}")
        count = 0
        for word in lines:
            count += 1
            print(f"Количество слов в {count} строке: {len(word.split())}")
        print("\n")


lines_count(r"task_2_file.txt")
lines_count(r"task_4_eng_file.txt")
