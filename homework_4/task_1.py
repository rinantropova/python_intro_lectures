# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# n = int(input('Enter amount of elements for the first list: '))
# m = int(input('Enter amount of elements for the second list: '))
# first_list = []
# sec_list = []
# for value in range(n):
#     value = int(input('Enter values for the first list: '))
#     first_list.append(value)
# print(first_list)
# for value in range(m):
#     value = int(input('Enter values for the second list: '))
#     sec_list.append(value)
# print(sec_list)
#
# duplicates = list(set(first_list) & set(sec_list))
# print(duplicates)



var1 = '5 5'
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'
converted_1 = var2.split()
list_1 = [int(num) for num in converted_1]
print(set(list_1))

converted_2 = var3.split()
list_2 = [int(num) for num in converted_2]
print(set(list_2))

duplicates = list(set(list_1) & set(list_2))
print(duplicates[0])
print(duplicates[len(duplicates)-1])
for i in range(0, len(duplicates)-1):
    for j in range(i, len(duplicates) - 1):
        if duplicates[j] > duplicates[j+1]:
            temp = duplicates[j]
            duplicates[j] = duplicates[j+1]
            duplicates[j+1] = temp
            print(duplicates)

print(duplicates)