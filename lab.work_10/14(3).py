import random

my_list = []
count = 0
# Создание листа с уникальными элементами
while count < 20:
    numbers = random.randrange(1, 55)

    if numbers not in my_list:
        my_list.append(numbers)
        count += 1
    else:
        print("Способ 1")
        print("Значение {0} уже встречалось".format(numbers))

my_list.sort()

print(my_list)

# Создание листа с уникальными элементами c использованием множества (set)
numbers = [1, 2, 2, 3, 3, 4, 5, 6, 9, 6, 5, 1, 1]


def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers


print("Способ 2")
print(get_unique_numbers(numbers))
