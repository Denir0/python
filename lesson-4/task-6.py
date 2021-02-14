from itertools import count, cycle

for el in count(b := int(input())):
    if el > b + 20:
        break
    else:
        print(el)

i = 1
for el in cycle(input()):
    print(el)
    i += 1
    if i > 20:
        break
