# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

n = int(input('Enter natural number N: '))


def create_list(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]


my_list = create_list(n, 1, max_value=n)
print(my_list)

x = int(input('Enter natural number X, that you need to find: '))


def find_closest(nums, a):
    return min(nums, key=lambda num: abs(num - a))


closest_value = find_closest(my_list, x)
print(closest_value)
