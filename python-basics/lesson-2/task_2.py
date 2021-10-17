user_lst = input("Введите любое количество чисел через пробел: ").split()
element = 0

for element in range(0, len(user_lst) - 1, 2):
    user_lst[element], user_lst[element + 1] = user_lst[element + 1], user_lst[element]

print(user_lst)
