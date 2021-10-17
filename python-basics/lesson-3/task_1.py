# def division(var1, var2):
#     """
#     Вариант 1
#     Если чисто по условию задачи
#     """
#     if var1 == 0 or var2 == 0:
#         return "Деление на 0!"
#     else:
#         return round(int(var1) / int(var2), 2)
#
#
# user_var1 = int(input("Введите 1 число: "))
# user_var2 = int(input("Введите 2 число: "))
# print(division(user_var1, user_var2))


def division():
    """
    Вариант 2
    Так мне кажется интереснее, но без позиционных аргументов (которые требует условие задачи)
    """
    while True:
        user_var1 = input("Введите 1 число: ")
        user_var2 = input("Введите 2 число: ")
        try:
            return round(int(user_var1) / int(user_var2), 2)
        except ValueError:
            print("Вы ввели слово, а не число!")
            continue
        except ZeroDivisionError:
            print("Деление на 0!")


print(division())
