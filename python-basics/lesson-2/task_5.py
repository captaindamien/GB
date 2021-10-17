lst = [7, 5, 3, 3, 2]
while True:
    user_number = int(input("(Введите 0000, если хотите завершить работу программы)\nВведите число, которое"
                            " хотите добавить в список: "))
    if user_number in lst:
        # находим положение (index) цифры совпадающей с введенным числом и прибавляем к ней количество чисел (count)
        # уже имеющихся в списке. Tак и находим место, где конец повторяющихся чисел]
        lst.insert(lst.index(user_number) + lst.count(user_number), user_number)
        print(f"Ваш список получился: {lst}\n")
    elif user_number not in lst:
        lst.append(user_number)
        lst.sort(reverse=True)
        print(f"Ваш список получился: {lst}\n")
    if user_number == 0000:
        break
