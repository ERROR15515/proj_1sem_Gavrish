# Единицы длины пронумерованы следующим образом:
# 1 — дециметр, 2 — километр, 3 — метр, 4 — миллиметр, 5 — сантиметр.
# Дан номер единицы длины (целое число в диапазоне 1-5)
# и длина отрезка в этих единицах (вещественное число)
# Найти длину отрезка в метрах.

print('1 - дециметр')   # Пометки для выбора действия
print('2 - километр')
print('3 - метр')
print('4 - миллиметр')
print('5 - сантиметр')

a = input('Выберите единицу измерения: ')   # Выбор единиц измерения
while type(a) != int:   # Обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Введен неверный тип данных')
        a = input('Выберите единицу измерения: ')

    try:
        while (1 > a) or (a > 5):    #Ограничение в диапозоне от 1 до 5
            print("Введен неверный номер!")
            a = input("Выберите единицу измерения: ")
    except TypeError:
        continue

b = input('Введите значение: ')  # Ввод данных

while type(b) != float:  # Обработка исключений
    try:
        b = float(b)
    except ValueError:
        print('Введен неверный тип данных')
        b = input('Введите значение в метрах: ')

if a == 1:
    print(b / 10, 'м')
elif a == 2:
    print(b * 1000, 'м')
elif a == 3:
    print(b * 1, 'м')
elif a == 4:
    print(b / 1000, 'м')
elif a == 5:
    print(b / 100, 'м')
