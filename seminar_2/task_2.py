# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# Fibonacci sequence:0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,...

fib_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
a = int(input('Enter positive number bigger than 1: '))

# My solution:
if a <= 1:
    print('Incorrect number!')
else:
    for i in range(len(fib_seq)):
        if a == fib_seq[i]:
            print(i + 1)
    else:
        if a not in fib_seq:
            print('-1')

# Seminar solution:
fib_pr, fib_next = 0, 1
position = 2
while fib_next < a:
    fib_pr, fib_next = fib_next, fib_pr + fib_next
    position += 1
if fib_next == a:
    print(position)
else:
    print(-1)


# Recursion:
def fib_func(num, prev_num=0, next_num=1, pos=2):
    if next_num == num:
        return pos
    elif next_num < num:
        return fib_func(num, next_num, prev_num + next_num, pos + 1)
    else:
        return -1


print(fib_func(a))
