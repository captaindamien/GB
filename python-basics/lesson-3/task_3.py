def my_func(arg1, arg2, arg3):
    lst = [arg1, arg2, arg3]
    return sum(lst)-min(lst)


var1 = int(input("Введите 1 число: "))
var2 = int(input("Введите 2 число: "))
var3 = int(input("Введите 3 число: "))
print(my_func(var1, var2, var3))
