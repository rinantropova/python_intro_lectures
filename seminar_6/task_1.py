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

# fourth_list = list(map(int, input('Enter numbers with a space between: ').split()))
# print(fourth_list)



def find_missing(a, b):
    seen_elements = set(b)
    result = [elem for elem in a if elem not in seen_elements]
    return result


missing_elements = find_missing(first_list, second_list)
print(missing_elements)


third_list = [elem for elem in first_list if elem not in second_list]
print(third_list)


res = filter(lambda elem: elem not in second_list, first_list)
print(', '.join(str(elem) for elem in res))


# Recursion:
def missing_find(num_1, num_2, num_3=[]):
    if len(num_1) == 0:
        return num_3
    if num_1[0] not in num_2:
        num_3.append(num_1[0])
    return missing_find(num_1[1:], num_2, num_3)


one_list = []
print(missing_find(first_list, second_list, one_list))

