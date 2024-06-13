# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input('Enter number N: '))

numbers = []
exponent = 0
while 2 ** exponent <= n:
    numbers.append(2 ** exponent)
    exponent += 1

print(numbers)


