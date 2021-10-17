"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
with open(r"task_3_file.txt", "r") as employers:
    lines = employers.readlines()
    income = 0
    for word in lines:
        employee_info = word.split()
        income += int(employee_info[-1])
        if int(employee_info[-1]) < 20000:
            print(f"Сотрудник имеющий оклад ниже 20000 рублей: {employee_info[0]} {employee_info[1]}")

    print(f"Средняя величина дохода сотрудников: {income / len(lines):.2f} рублей")
