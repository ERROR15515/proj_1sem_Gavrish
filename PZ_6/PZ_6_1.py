# Дан целочисленный список размера 10.
# Вывести все содержащиеся в данном списке четные числа
# в порядке убывания их индексов, а так же их количество K

from random import randint      # Импортирогвание "random"

lst = [randint(0, 20) for i in range(10)]     # Ввод переменных
lst1 = []
print(lst)
pop = 0
sch = 9
k = 0

while pop < 10:     # Отбор и сортировка
    if lst[sch] % 2 == 0:
        lst1.append(lst[sch])
        k += 1
    pop += 1
    sch -= 1

lst.sort(reverse=True)
print(lst1)
print('Количество элементов:', k)
