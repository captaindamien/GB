"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open(r"task_1_file.txt", "w") as file_obj:
    while True:
        user_input = input("Если хотите прекратить ввод, просто нажмите Enter."
                           "\nВведите данные: ")
        if user_input == "":
            break
        else:
            file_obj.writelines(f"{user_input}\n")
