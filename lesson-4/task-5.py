from functools import reduce

new_list = [el for el in range(100, 1001, 2)]
print(reduce(lambda a, b: a * b, new_list))
