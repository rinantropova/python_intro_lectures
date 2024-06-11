# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

print('Enter positive number: ')
n = int(input())


# def factorial(num):
#     res = 1
#     while num > 1:
#         res *= num
#         num -= 1
#     return res
#
#
# fact = factorial(n)
# print(fact)

#Simpler solution without function:
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)