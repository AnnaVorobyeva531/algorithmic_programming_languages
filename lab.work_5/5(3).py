from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#  Сравнения строки со строками из списка
female_names = ['Айлин', 'Айнагуль', 'Айнур', 'Айсель', 'Айсун', 'Айсылу', 'Аксинья', 'Алана', 'Алевтина', 'Александра',
                'Алексия', 'Алёна', 'Алеста', 'Алина', 'Алиса', 'Алия', 'Алла', 'Алсу']

a = process.extract("Алёна", female_names, limit=6)
print(a)


#  Нечеткое сравнение строк
def compare(str_1, str_2):
    ngrams = [
        str_1[i:i + 3] for i in range(len(str_1))
    ]
    count = 0
    for ngram in ngrams:
        count += str_2.count(ngram)
        return count / max(len(str_1), len(str_2))


print(compare('Австрия', 'Австралия'))
print(compare('Класс', 'Классификация'))

#  Сравнение, совпадения букв в одном слове с буквами в другом.
w1 = set(input('Введите 1-е слово'))
w2 = set(input('Введите 2-е слово'))

print('These words have {} common letters'.format(len(w1.intersection(w2))))
