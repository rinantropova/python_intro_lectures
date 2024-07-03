# # 1
# b = lambda: 10
# print(b())

# # 2
# e = lambda: print(10)
# e()

# # 3
# b = lambda e, i: {e: i}
# print(b(1, 2)[1])

# # 4
# c = lambda a b: a + b
# print(c(1, 2))

# # 5
# d = lambda a, b: a + b
# print(d(1, 2, 3))

# # 6
# def pl(a):
#     return a + 10
#
# e = lambda a: pl(a)
#
# print(e(10))

# # 7
# (lambda x: (x + 3) * 5 / 2)(3)

# # 8
# from functools import reduce
# numbers = [1, 2, 3]
# print(reduce(lambda x, y: x + y, numbers))

# # 9
# import math
# d = lambda x: math.fabs(x)
# print(d(-5))

# # 10
# b = lambda: print("str")
# type(b())

# # 11
# c = lambda: print(1)
# print(print(1) == c())

# 12
e = lambda: 1
print(e() == True)
print(e() is True)
