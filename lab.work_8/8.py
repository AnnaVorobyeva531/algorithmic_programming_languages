#  Определение числа Фибонначчи
prew = cur = 1
element = input('Введите номер искомого элемента : ')
element = int(element)
for n in range(int(element - 2)):
    tmp = prew + cur
    prew = cur
    cur = tmp
print(str(element) + ' элемент последовательности равен ' + str(cur))


