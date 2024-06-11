# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# Fibonacci sequence:0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,...

fib_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
print('Enter positive number bigger than 1: ')
a = int(input())

if a <= 1:
    print('Incorrect number!')
else:
    for i in range(len(fib_seq)):
        if a == fib_seq[i]:
            print(i + 1)
    else:
        if a not in fib_seq:
            print('-1')





