# Задача 2: Найдите сумму цифр трехзначного числа
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Enter 3-digits number: ')
number = int(input())
if number // 1000 != 0 or number // 100 == 0:
    print('Wrong number is entered, please change your input to 3-digits number!')
else:
    sum = 0
    while number > 0:
        sum = sum + number % 10
        number = number // 10
    print(sum)
