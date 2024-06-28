# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все
# пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:         Вывод:
# 300           220 284


# def sum_divisors(num):
#     sum = 0
#     for k in range(1, num // 2 + 1):
#         if num % k == 0:
#             sum += k
#     return sum
#
#
# def find_pairs(k):
#     for i in range(1, k):
#         j = sum_divisors(i)
#         if i < j <= k and i == sum_divisors(j):
#             print(i, j)
#
#
# k = int(input('Enter number k: '))
# find_pairs(k)


# Seminar solution:
k = 1000


def get_sum(n):
    new_sum = 1
    for elem in range(2, n):
        if n % elem == 0:
            new_sum += elem
    return new_sum


def fill_array(k):
    res = list()
    for n in range(1, k+1):
        if n not in res:
            m = get_sum(n)
            if n == get_sum(m) and m != n:
                res.append(m)
                res.append(n)
    return res

print(fill_array(k))

