# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

values = input('Enter list of numbers, separated by comma: ')
k = int(input('Enter positive number k: '))
numbers = list(map(int, values.split(",")))
print(numbers)
print(f'k = {k}')


def rotate(arr, a):
    return arr[a:] + arr[:a]


rotated_numbers = rotate(numbers, k)
print(rotated_numbers)
