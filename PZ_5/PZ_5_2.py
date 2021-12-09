# Описать функцию AddLeftDigit(D, K),
# добавляющую к целому положительному числу K слева цифру D
# (D — входной параметр целого типа, лежащий в диапазоне 1-9, K —
# параметр целого типа,являющийся одновременно входным и выходным).
# С помощью этой функции последовательно добавить
# к данному числу K слева данные цифры D1 и D2,
# выводя результат каждого добавления.

def addleftdigit(d1, d2, k):     # Задание функциий
    print(int(str(d2) + str(k)))
    print(int(str(d1) + str(d2) + str(k)))
    exit(0)


def main():
    try:
        d1 = int(input('Введите целое D1(от 1 до 9): '))  # Ввод переменных
        if not((d1 < 10) and (d1 > 0)):
            print('Введено неверное значение!')
            return

        d2 = int(input('Введите целое D2(от 1 до 9): '))
        if not ((d2 < 10) and (d2 > 0)):
            print('Введено неверное значение!')
            return

        k = int(input('Введите целое число K: '))
        print(addleftdigit(d1, d2, k))
        exit(0)
    except ValueError:
        print('Введен неверный тип данных!')
        return


if __name__ == '__main__':
    while True:
        main()
