import random

print("Добро пожаловать! Меня зовут Jack")
prompt = "Задайте свой вопрос или  введите exit для выхода"
question = " "
while question != "exit":
    print(prompt)
    question = input()
    answer = random.randint(0, 1)
    if question == 'exit':
        print("Надеюсь вы получили нужный ответ, до свидания!")
        continue
    elif answer == 0:
        print('Нет')
    else:
        print('Да')


