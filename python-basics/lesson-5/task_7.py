"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json
with open(r"task_7_file.txt", "r", encoding="utf-8") as init_file:
    dct_firms = {}
    dct_average = {}
    res_lst = [dct_firms, dct_average]
    for line in init_file:
        lst = line.split()
        dct_firms[lst[0]] = int(lst[-2]) - int(lst[-1])
    average_profit = [value for value in dct_firms.values() if value > 0]
    dct_average["average_profit"] = sum(average_profit)
    print(res_lst)
    with open(r"task_7_json.json", "w") as json_file:
        json.dump(res_lst, json_file)
