# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где a0= 0, a1= 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

def fibonacci(num):
    if num in [1, 2]:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


def find_num(ind):
    return fibonacci(ind + 1)


# fib_seq = []
# for i in range(1, 8):
#     fib_seq.append(fibonacci(i))
# print(fib_seq)
# print(fibonacci(7))
print(find_num(7))

# Seminar's solution:
# 0 1  1 2 3 5 8 13 21 34 55 89
a = 7
fibo_p, fibo_n = 0, 1
for i in range(0, a):
    fibo_p, fibo_n = fibo_n, fibo_p + fibo_n
print(f'{a}th number = {fibo_n}')


def fibo_find(n, prev=0, nex=1):  # everything before the cycle is the arguments in the recursive function
    # base case:
    if n == 0:
        return nex
    # step of recursion:
    return fibo_find(n - 1, prev=nex, nex=prev + nex)

print(fibo_find(a))
