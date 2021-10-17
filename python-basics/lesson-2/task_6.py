#  РЕШЕНИЕ НОМЕР 1 САМОЕ ПРОСТОЕ И ЧИТАЕМОЕ
# lst, name_lst, price_lst, quantity_lst, unit_lst = [[] for i in range(5)]
# quit_message = 0
# count = 0
#
# while quit_message != 'no':
#     dct = {"название": input("Введите название товара: "), "цена": input("Введите цену товара: "),
#            "количество": input("Введите количество товара: "), "ед": input("Введите измерение единицы товара: ")}
#     tpl = (count + 1, dct)
#     lst.append(tpl)
#     count += 1
#
#     name_lst.append(dct["название"])
#     price_lst.append(dct["цена"])
#     quantity_lst.append(dct["количество"])
#     unit_lst.append(dct["ед"])
#
#     quit_message = input('\nХотите внести еще один товар? Нажмите "Enter" для продолжения'
#                          ' или Введите "NO" для выхода из программы: \n').lower()
#
# dct_result = {"название": name_lst, "цена": price_lst, "количество": quantity_lst, "ед": unit_lst}
#
# print(f"\nСтруктура списка: {lst}")
# print(f"Аналитика списка: {dct_result}")

#  РЕШЕНИЕ НОМЕР 2
lst_keys = ["название", "цена", "количество", "ед."]
lst_result, lst_values, lst_name, lst_price, lst_quantity, lst_unit = [[] for k in range(6)]

quit_message = None
count = 1

while quit_message != 'no':
    for i in range(len(lst_keys)):
        lst_values.append(input(f'"{lst_keys[i].title()} товара": '))

    dct = dict(zip(lst_keys, lst_values))
    tpl = (count, dct)
    lst_result.append(tpl)
    count += 1
    # Не могу ничего придумать, чтобы НЕ создавать много списков для аналитики
    # Хочется чтобы код был максимально поддержмиваемый, а по итогу чтобы добавить еще один ключ
    # Нужно не просто поправить lst_keys, но и создать еще 1 список для сбора по новому ключу и т.д.
    lst_name.append(lst_values[0])
    lst_price.append(lst_values[1])
    lst_quantity.append(lst_values[2])
    lst_unit.append(lst_values[3])

    lst_values.clear()
    quit_message = input('\nХотите внести еще один товар? Нажмите "Enter" для продолжения'
                         ' или Введите "NO" для выхода из программы: \n').lower()

dct_result = {lst_keys[0]: lst_name, lst_keys[1]: lst_price, lst_keys[2]: lst_quantity, lst_keys[3]: lst_unit}

print(f"\nСтруктура списка: {lst_result}")
print(f"Аналитика списка: {dct_result}")
