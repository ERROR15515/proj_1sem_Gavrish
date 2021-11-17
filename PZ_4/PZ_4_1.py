# Даны два целых числа A и B (A < B).
# Найти сумму квадратов всех целых чисел
# от A до B включительно.

b = input('Введите число B(должно быть больше A): ')  # Ввод переменных

while type(b) != int:  # обработка исключений
    try:
        b = int(b)
    except ValueError:
        print('Введено неверное значение!')
        b = input('Введите число B(должно быть больше A): ')

a = input('Введите число A: ')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Введено неверное значенеие!')
        a = input('Введите число A: ')
    if a > b:
        print('Введено неверное значение!')
        a = input('Введите число A: ')
    else:
        continue

c = 0

while a <= b:
    print('Квадрат числа', a, ':', a ** 2)
    c += a ** 2
    a += 1

print(c)

