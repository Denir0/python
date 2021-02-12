# Функция
def my_function(x, y):
    try:
        return int(x) / int(y)
    except ZeroDivisionError:
        print("На ноль делить нельзя!")

# Вывод
print(my_function(input(), input()))
