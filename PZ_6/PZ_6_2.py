# Дан список размера N. Найти количество участков, на которых его элементы
# монотонно возрастают.

import random   # Импортирогвание "random"

n = input("Введите размер списка: ")    # Ввод переменных
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Введено неверное значение.")
        n = input("Введите размер списка: ")
a = [random.randint(0, 20) for i in range(n)]
print(a)
t = 0

for i in range(n):
    if a[i] < a[i+1]:
        t += 1
    if n - i == 2:
        break

print(t)
