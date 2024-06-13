# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2


import random

n = int(input('Enter number of coins: '))


def coins_list(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]


coins = coins_list(n, 0, 1)
print(coins)

count_tails = 0
count_heads = 0
for i in range(len(coins)):
    if coins[i] == 0:
        count_heads += 1
    else:
        count_tails += 1

if count_tails > count_heads:
    print(count_heads)
else:
    print(count_tails)
