num = int(input('Введите число: '))
const = num
maximum = const % 10  # Максимум
while const:
    last_num = const % 10
    if maximum == 9:  # Больше 9 не будет, программа может закончится тут
        break
    if last_num > maximum:  # Если число больше максимума то перезаписываем его
        maximum = last_num
    const = const // 10  # Убираем последнее число

print(maximum)  # Выводит наибольшее число
