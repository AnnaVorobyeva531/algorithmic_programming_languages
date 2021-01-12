# 1) Заменить все "х" на "у"
print("Task-1")
source_string = "jhdy  xxyxy jjxcyy xx"
new_string = " "
for x in source_string:
    if x == "x":
        new_string += "y"
    else:
        new_string += x
print(source_string)
print(new_string)

# 2) Сосчитать произведение чисел, кратных 3 и 5
print("Task-2")
numbers = [1, 5, 8, 4, 33, 8, 2, 9, 3, 55]
product_numbers = 1
for x in numbers:
    if x // 3 == x / 3 or x //5 == x / 5:
        product_numbers *= x
print(product_numbers)


# 3) Заменить все буквы "х" на "у" в исходной строке без исользования дополнительной
print("Task-3")
source_string = "xxx jnkyyxyx xxxhjb xyx"
new_string = source_string.replace('x', 'y')
print(source_string)
print(new_string)







