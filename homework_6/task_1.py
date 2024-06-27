# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
#
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a1 = int(input('Enter the first element of the arithmetic progression: '))
d = int(input('Enter the difference of the arithmetic progression: '))
n = int(input('Enter the amount of elements of the arithmetic progression: '))


def arith_progression(a, d, n, new_list=[]):
    for i in range(1, n + 1):
        elem = a + (i - 1) * d
        new_list.append(elem)
    return new_list

progression = arith_progression(a1, d, n)
print(progression)


# recursion:
def progression_rec(first_el, diff, num, new_list=None):
    if new_list is None:
        new_list = []
    if num == 0:
        return new_list
    else:
        new_value = first_el + (num - 1) * diff
        new_list.insert(0, new_value)
    return progression_rec(first_el, diff, num - 1, new_list)

print(progression_rec(a1, d, n))