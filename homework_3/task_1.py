# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1


import random

n = int(input('Enter natural number N: '))


def create_list(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]


new_list = create_list(n, 1, max_value=n)
print(new_list)

x = int(input('Enter natural number X, that you need to find: '))

count = 0
for elem in new_list:
    if elem == x:
        count += 1

print(count)
