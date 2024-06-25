# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


number = '3 4'


def reverse1(data):
    new_data = ''
    for s in reversed(data):
        new_data += s
    return new_data


print(reverse1(number))


# recursion:
def reverse2(data, new_data=''):
    if len(data) == 0:
        return new_data
    return reverse2(data[:-1], new_data + data[-1])


print(reverse2(number))
