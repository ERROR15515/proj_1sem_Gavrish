# Средствами языка Python сформировать текстовый файл (.txt),
# содержащий последовательность из целых положительных и
# отрицательных чисел. Сформировать новый текстовый файл (.txt)
# следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Сумма элементов больших 10 во второй половине:

import random
n = 0
p = 0
a = []
f1 = open("file1.txt", "w", encoding="UTF-8")
for i in range(random.randint(10, 20)):
    a.append(random.randint(0, 20))
    f1.write(str(a[i]))
    f1.write(" ")
f1.close()

f2 = open('file2.txt', 'w', encoding="UTF-8")

m = len(a) // 2
for i in range(m, len(a)):
    if a[i] > 10:
        p += a[i]

b = min(a)
for i in reversed(range(len(a))):
    if a[i] == b:
        b = i
        break

f2.write('Исходные данные: ')
f2.write(str(a))
f2.write('\n')
f2.write('Количество элементов: ')
f2.write(str(len(a)))
f2.write('\n')
f2.write('Индекс последнего минимального элемента: ')
f2.write(str(b))
f2.write('\n')
f2.write('Сумма элементов больших 10 во второй половине: ')
f2.write(str(p))

f2.close()
