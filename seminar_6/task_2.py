# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:         Ввод:
# 5             5
# 1 2 3 4 5     1 5 1 5 1
# Вывод:        Вывод:
# 0             2
# (каждое число вводится с новой строки)

original = [1, 2, 3, 4, 5]
additional = [1, 5, 1, 5, 1]
one_more = [3, 4, 3, 4, 5, 4, 1, 2, 1]


def find_elem(one_list, count=0):
    for i in range(1, len(one_list) - 1):
        if one_list[i] > one_list[i - 1] and one_list[i] > one_list[i + 1]:
            count += 1
    return count


print(find_elem(original))
print(find_elem(additional))
print(find_elem(one_more))


def find_elem_rec(one_list, count=0):
    if len(one_list) == 2:
        return count
    elif one_list[1] > one_list[0] and one_list[1] > one_list[2]:
        count += 1
    return find_elem_rec(one_list[1:], count)


print(find_elem_rec(original))
print(find_elem_rec(additional))
print(find_elem_rec(one_more))
