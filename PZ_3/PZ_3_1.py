# Даны два целых числа: A, B.
# Проверить истинность высказывания:
# «Каждое из чисел A и B нечетное».

a = input('Введите число a: ')  # Ввод данных
b = input('Введите число b: ')

while type(a) != int:   # Обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Введен неверный тип данных!')
        a = input('Введите число а: ')

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Введен неверный тип данных!')
        b = input('Введите число b: ')

if a % 2 != 0 and b % 2 != 0:
    print('Условие выполнено!')
else:
    print('Условие не выполнено!')
