# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]


#SOlution without lambda:
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)



#Solution with lambda:

# def select(f, col):
#     return [f(x) for x in col] - same as function map

# def where(f, col):
#     return [x for x in col if f(x)] - same as function filter
        
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
print(res)
res = filter(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)