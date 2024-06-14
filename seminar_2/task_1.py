# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

n = int(input('Enter positive number: '))

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


# Simpler solution without function:
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)

"""
While loop - a loop with pre-condition. It means that if condition isn't true, we won't even enter the loop in the first 
place. To perform at least one iteration, condition should be true. We don't know a number of required iterations.
For loop - arithmetic loop. Here we know the number of iterations.
"""


# Recursion:
def fact_func(n, fact=1):
    if n == 1:
        return fact
    return fact_func(n - 1, fact * n)


print(fact_func(5))


if __name__ == "__main__":
    print(fact_func(5))

# we do something if the file/module is main. In case you import the file to other file, this piece of code won't
# work there.
