my_tuple = input('Введите значения списка через пробел: ').split()
for el in range(1, len(my_tuple), 2):
    my_tuple.insert(el - 1, my_tuple.pop(el))

print(my_tuple)
