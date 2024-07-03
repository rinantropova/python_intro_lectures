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

# 6
def pl(a):
    return a + 10

e = lambda a: pl(a)

print(e(10))