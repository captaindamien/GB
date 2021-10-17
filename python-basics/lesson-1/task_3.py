user_number = str(input("Введите целое положительное число от 1 до 9: "))
decade = user_number + user_number
hundred = user_number + user_number + user_number

print(f"Сумма чисел в формате 'n + nn + nnn', где n - ваше число = {int(user_number) + int(decade) + int(hundred)}")
