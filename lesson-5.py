profit = int(input("Введите выручку: "))
cost = int(input("Введите издержки: "))
if profit > cost:
    print("Ваша фирма работает с прибылью.")
    print(f"Рентабельность выручки: {(profit - cost) / cost}")
    people = int(input("Введите число сотрудников: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника: {(profit - cost) / people}")
else:
    print("Ваша фирма работает в убыток!")
