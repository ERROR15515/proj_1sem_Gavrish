# Дан целочисленный список размера 10.
# Вывести все содержащиеся в данном списке четные числа
# в порядке убывания их индексов, а так же их количество K

from random import randint      # Импортирогвание "random"

lst = [randint(0, 9999) for i in range(10)]     # Ввод переменных
pop = 0
sch = 0
k = 0

while pop < 10:     # Отбор и сортировка
    if lst[sch] % 2 == 0:
        lst.sort(reverse=True)
        k += 1
    pop += 1
    sch += 1

print(lst)
print('Количество элементов:', k)
