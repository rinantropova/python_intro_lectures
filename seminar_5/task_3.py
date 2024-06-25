# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

number = int(input('Enter a number: '))

def find_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return 'No'
    return 'Yes'


print(find_prime_num(number))

# recursion:
def find_prime_num2(n, i=2):
    if i < n:
        if n % i == 0:
            return 'No'
        return find_prime_num2(n, i+1)
    return 'Yes'

print(find_prime_num2(number))