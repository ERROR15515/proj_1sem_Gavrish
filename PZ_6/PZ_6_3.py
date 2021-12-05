# Дан список размера N. Заменить каждый элемент списка
# на среднее арифметическое этого элемента и его соседей.

from random import randint  # Импортирогвание "random"


n = int(input('Введите размер списка:'))    # Ввод переменных
lst = [randint(0, 50) for i in range(n)]
lstt = []

n -= 1
print(lst)

hlp = round((lst[1] + lst[0]) / 2, 1)   # Расчет первых двух элементов
lstt.insert(0, hlp)

for i in range(n+1):
    if i < n and i != 0:
        hlp = round((lst[i]+lst[i-1]+lst[i+1])/3, 1)
        lstt.insert(i+1, hlp)

hlp = round((lst[n-1] + lst[n]) / 2, 1)   # Расчет последних двух элементов
lstt.insert(n, hlp)

print(lstt)
