a = int(input("Введите результат в первый день: "))
b = int(input("Введите требуемый результат: "))
days = 0
while a <= b:
    a = a * 1.1
    days += 1
print(f"На {days} день спорстсмен достиг результата - не менее {b} км.")
