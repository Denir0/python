#Два варианта решения, через список и через нумерованный список.
#
# my_list = input('Введите строку из нескольких слов через пробел: ').split()
#
# for el in my_list:
#     print(f'{my_list.index(el) + 1}. {el[:10]}')

my_list = input('Введите строку из нескольких слов через пробел: ').split()

for i, el in enumerate(my_list, 1):
    print(f'{i}. {el[:10]}')