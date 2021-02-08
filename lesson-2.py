time = int(input('Введите время в секундах: '))

print(f'{time // 60 // 60}:{time // 60 % 60:02}:{time % 60:02}')
