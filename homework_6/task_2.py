# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]


def find_index(one_list, min_d, max_d):
    new_list = []
    for i in range(0, len(one_list)):
        if min_d <= one_list[i] <= max_d:
            new_list.append(i)
    return new_list


print(find_index(array, -5, 0))


# recursion:
def find_index_rec(one_list, min_d, max_d, index=0, new_list=None):
    if new_list is None:
        new_list = []
    if index >= len(one_list):
        return new_list
    elif min_d <= one_list[index] <= max_d:
        new_list.append(index)
    return find_index_rec(one_list, min_d, max_d, index + 1, new_list)


print(find_index_rec(array, -5, 0))
