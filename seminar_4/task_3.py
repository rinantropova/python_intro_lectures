# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам. Примечание: Программные коды на следующих слайдах


'''Ваня:'''
# n = int(input())
# max_number = 1000
# while n != 0:
#     n = int(input())
#     if max_number > n:
#         max_number = n
# print(max_number)


'''Петя:'''
# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print(n)


# Mine:
seq = []
n = int(input())
seq.append(n)
while n < 0:
    n = int(input())
    if n != 0:
        seq.append(n)
print(seq)

max_el = seq[0]
for i in range(0, len(seq) - 1):
    if seq[i] > max_el:
        max_el = seq[i]
print(max_el)


# Seminar's:
n = int(input())
max_number = n
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)
