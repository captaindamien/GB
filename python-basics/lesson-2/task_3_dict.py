month = int(input("Введите номер месяца: "))
dct = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето", 9: "осень",
       10: "осень", 11: "осень", 12: "зима"}

print(f"Выбранный месяц это {dct.values(month)}")
