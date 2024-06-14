# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

values = input('Enter list of numbers, separated by comma: ')
numbers = list(map(int, values.split(",")))
print(numbers)

unique_count = len(set(numbers))
print(unique_count)


