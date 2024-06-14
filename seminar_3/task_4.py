# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


values = input('Enter list of numbers, separated by comma: ')
numbers = list(map(int, values.split(",")))
print(numbers)

count = 0
for i in range(1, len(numbers)):
    curr_elem = numbers[i]
    prev_elem = numbers[i - 1]
    if curr_elem > prev_elem:
        count += 1

print(count)



