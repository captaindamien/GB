def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    return 1 / result


var1 = float(input("Введите положительное действительное число: "))
var2 = int(input("Введите целое отрицательное число: "))
print(my_func(var1, var2))
