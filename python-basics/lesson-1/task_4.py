user_number = int(input("Введите целое положительное число: "))
max_number = 0

while user_number > 10:
    last_number = user_number % 10
    user_number = user_number // 10
    if last_number > max_number:
        max_number = last_number

print(max_number)
