# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# My solution:
values = input('Enter list of numbers, separated by comma: ')
k = int(input('Enter positive number k: '))
numbers = list(map(int, values.split(",")))
print(numbers)
print(f'k = {k}')


def rotate(arr, a):
    return arr[a:] + arr[:a]


rotated_numbers = rotate(numbers, k)
print(rotated_numbers)



# Seminar solution 1:
my_list = [1, 2, 3, 4, 5]
k = 3
new_list = my_list[k:] + my_list[:k]
print(new_list)


# Seminar solution with loops:
my_list = [1, 2, 3, 4, 5]
k = 3
for _ in range(k-1):
    last_el = my_list.pop()
    my_list.insert(0, last_el)

print(my_list)