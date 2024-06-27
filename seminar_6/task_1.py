# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:                 Вывод:
# 7                     3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1        (каждое число вводится с новой строки)

# n = int(input('Add number of elements for the first list: '))
first_list = [3, 1, 3, 4, 2, 4, 12]
# for value in range (0, n):
#     number = int(input('Add value to the list: '))
#     first_list.append(number)
# print(first_list)

# m = int(input('Add number of elements for the second list: '))
second_list = [4, 15, 43, 1, 15, 1]
# for value in range (0, m):
#     number = int(input('Add value to the list: '))
#     second_list.append(number)
# print(second_list)

def find_missing(a, b):
    seen_elements = set(b)
    result = [elem for elem in a if elem not in seen_elements]
    return result


missing_elements = find_missing(first_list, second_list)
print(missing_elements)

