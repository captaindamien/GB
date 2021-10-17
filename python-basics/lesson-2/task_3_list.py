month = int(input("Введите номер месяца: "))
lst = ["зима", "весна", "лето", "осень"]
# решил побаловаться "ифами"
if month <= 2 or month == 12:
    print(f"Выбранный месяц это {lst[0]}")
elif 2 < month < 6:
    print(f"Выбранный месяц это {lst[1]}")
elif 5 < month < 9:
    print(f"Выбранный месяц это {lst[2]}")
elif 8 < month < 12:
    print(f"Выбранный месяц это {lst[3]}")
