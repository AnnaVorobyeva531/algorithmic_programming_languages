from typing import Dict


class Dictionary:
    car_brand: Dict[int, str]

    def __init__(self):
        self.price_comfort = {5500: 'A', 6200: 'B', 7900: 'C', 8700: 'D'}  # словарь стоимости аренды
        self.car_brand = {1: 'Hyundai i10', 2: 'Ravon R2', 3: 'Chevrolet Aveo', 4: 'Renault Logan', 5: 'Toyota Corolla',
                          6: 'Mitsubishi Lancer', 7: 'Audi A4', 8: 'Toyota Camry'}  # словарь марок автомобилей
        self.car_comfort = {1: 'A', 2: 'A', 3: 'B', 4: 'B', 5: 'C', 6: 'C', 7: 'D',
                            8: 'D'}  # словарь: виды комфортности

    def show_all(self):
        for value in self.price_comfort:
            print(self.price_comfort[value])


customer_base = ['Смирнов Павел Викторович', 'Желтышев Максим Валерьевич', 'Сабурова Наталья Николаевна',
                 'Исаев Михаил Васильевич', 'Шестакова Марина Алексеевна', 'Миронов Иван Андреевич']  # список клиентов
client_age = {'Смирнов Павел Викторович': 43, 'Желтышев Максим Валерьевич': 33, 'Сабурова Наталья Николаевна': 31,
              'Исаев Михаил Васильевич': 28, 'Шестакова Марина Алексеевна': 47,
              'Миронов Иван Андреевич': 25}  # словарь возраста клиентов

command = 0
dictAuto = Dictionary()

while command < 5500:
    print("Введите сумму или (0) для выхода")
    command = int(input())
    price = command
    if 5500 <= price < 6200:
        print('Вам доступен автомобиль категории %s' % dictAuto.price_comfort[5500])
    elif 6200 <= price < 7900:
        print('Вам доступен автомобиль категории %s' % dictAuto.price_comfort[5500], ',', dictAuto.price_comfort[6200])
    elif 7900 <= price < 8700:
        print('Вам доступен автомобиль категории %s' % dictAuto.price_comfort[5500], ',', dictAuto.price_comfort[6200],
              ',', dictAuto.price_comfort[7900])
    elif price >= 8700:
        print('Вам доступен автомобиль категории %s' % dictAuto.price_comfort[5500], ',', dictAuto.price_comfort[6200],
              ',', dictAuto.price_comfort[7900], ',', dictAuto.price_comfort[8700])
    elif price == 0:
        continue
    else:
        print("На такую сумму нельзя арендовать автомобиль")
        continue

    print("Введите категорию комфортности автомобиля из списка чтобы выбрать марку автомобилей, или exit для выхода")
    comfort = str(input())
    if comfort == 'exit':
        break
    brand = comfort
    if brand == 'A':
        print(dictAuto.car_brand[1], ',', dictAuto.car_brand[2])
    elif brand == 'B':
        print(dictAuto.car_brand[3], ',', dictAuto.car_brand[4])
    elif brand == 'C':
        print(dictAuto.car_brand[5], ',', dictAuto.car_brand[6])
    elif brand == 'D':
        print(dictAuto.car_brand[7], ',', dictAuto.car_brand[8])

    print("Выберите марку автомобиля")
    brand = str(input())

    print("Пройдите регистрацию. Введите Ф.И.О. или exit для выхода")
    client = str(input())
    if client == 'exit':
        break
    if client in customer_base:
        print("Вы уже есть в списке. Автомобиль добавлен")
        print("Регистрация пройдена")
    else:
        print("Введите возраст")
        age = int(input())
        if age >= 18:
            customer_base.append(client)  # добавляем элемент в список
            print(customer_base)  # для проверки
            client_age[client] = age  # добавляем элементы в словарь
            print(client_age)  # для проверки
            print("Данные занесены в базу. Регистрация пройдена")
            continue
        else:
            print("Возрастное ограничение")
            continue

    continue
