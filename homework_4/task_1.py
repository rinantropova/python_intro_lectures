# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input('Enter amount of elements for the first list: '))
m = int(input('Enter amount of elements for the second list: '))
first_list = []
sec_list = []
for value in range(n):
    value = int(input('Enter values for the first list: '))
    first_list.append(value)
print(first_list)
for value in range(m):
    value = int(input('Enter values for the second list: '))
    sec_list.append(value)
print(sec_list)

duplicates = list(set(first_list) & set(sec_list))
print(duplicates)