# def sum_numbers(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     print(sum)

# sum_numbers(5)



# def sum_numbers(n, y = 'hello'):
#     print(y)
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum
#     # print('stop')


# a = sum_numbers(5, 'qwerty')
# print(a)



# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('q', 'e', 't'))
# print(sum_str('q', 'e', 't', 'f', 't'))
# print(sum_str(1, 8, 9))



# import module1
# print(module1.max1(5, 9))


# from module1 import max1 #from module1 import *   = import all functions from the file
# print(max1(10, 9))

import module1 as m1
print(m1.max1(10,9))