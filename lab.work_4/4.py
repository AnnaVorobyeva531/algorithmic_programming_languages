import numpy as np

# Найти сумму ряда от 0 - 100
print("Task-1")
x = np.array(range(0, 100))
print(x.sum())

# Найти сумму ряда от 0 - input()
print("Task-2")
print("Введите число")
n = int(input())
a = np.array(range(n))
print(a.sum())

# Найти среднее среди 100 случайных чисел
print("Task-3")
k = np.random.randint(1000, size=100)
print(k)
print(np.mean(k))
