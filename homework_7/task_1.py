# Задача 1: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                         Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам        Парам пам-пам

poem = 'пара-ра-рам рам-пам-папам па-ра-па-дам'.split()

def count_vowels(words):
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    return sum(1 for char in word if char in vowels)

vowels = []
for word in poem:
    vowel_count = count_vowels(poem)
    vowels.append(vowel_count)

print(vowels)

if all(x == vowels[0] for x in vowels):
    print('Парам пам-пам')
else:
    print('Пам парам')


# 2
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дм'
words = stroka.split()


def vowels_counter(word):
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    return sum(1 for char in word if char in vowels)


def vowels_check(words):
    if len(words) <= 1:
        print('Количество фраз должно быть больше одной!')
        return

    vowels_lst = [vowels_counter(word) for word in words]

    if all(x == vowels_lst[0] for x in vowels_lst):
        print('Парам пам-пам')
    else:
        print('Пам парам')

vowels_check(words)


import sys

print(sys.executable)