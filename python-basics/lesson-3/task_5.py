def split_sum():
    end_sum = 0
    while True:
        try:
            user_input = input("Для завершения программы введите 'q'\n"
                               "Введите любое кол-во чисел через пробел: ").split()
            for elements in user_input:
                elements = int(elements)
                end_sum += elements
            print(f"\nРезультат сложения ваших чисел: {end_sum}\n")
        except ValueError:
            print(f"\nРезультат сложения ваших чисел: {end_sum}")
            break


split_sum()
