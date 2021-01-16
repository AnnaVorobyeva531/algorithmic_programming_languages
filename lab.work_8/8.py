#  Определение числа Фибонначчи
prew = cur = 1
element = input('Введите номер искомого элемента : ')
element = int(element)
for n in range(int(element - 2)):
    tmp = prew + cur
    prew = cur
    cur = tmp
print(str(element) + ' элемент последовательности равен ' + str(cur))

# Генератор списка рядом Фибонначчи
print("Введите размер списка")
dimension = int(input())


def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


data = list(fibonacci(dimension))
print(data)

