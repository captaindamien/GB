profit = int(input("Введите значение выручки фирмы в рублях: "))
loss = int(input("Введите значение издержки фирмы в рублях: "))

if profit > loss:
    print(f"Ваша рентабельность выручки = {int((profit / loss) * 100)}%")
    workers = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника = {'%.2f' % ((profit - loss) / workers)} рублей")
elif profit < loss:
    print(f"Вы понесли убытки в количестве = {int(loss - profit)} рублей")
else:
    print(f"Вы вышли в 0!")
