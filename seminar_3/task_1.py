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


# # Seminar solution:
my_list = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(my_list)))


# Seminar solution with while loop and try-except:
# new_list = []
# # flag = True
# while True:
#     try:
#         my_str = int(input('Enter a number, to stop input enter any symbol: '))
#     except ValueError:
#         print('You entered a string')
#         break
#     else:
#         new_list.append(my_str)
#
#
# print('Initial list: \n', new_list)
# print(len(set(new_list)))


# Seminar solution with for loop
my_list = [1, 1, 2, 0, -1, 3, 4, 4]
res = []
for el in my_list: # арифметический
    if el not in res:
        res.append(el)
print(len(res))
