# Задача 2: Найдите сумму цифр трехзначного числа
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Enter 3-digits number: ')
number = int(input())

# Solution 1
if number // 1000 != 0 or number // 100 == 0:
    print('Wrong number is entered, please change your input to 3-digits number!')
else:
    total_sum = 0
    while number > 0:
        total_sum = total_sum + number % 10
        number //= 10
    print(total_sum)

# Solution 2
# def sum_of_digits(number):
#     number_str = str(number)
#
#     sum = 0
#
#     for digit in number_str:
#         sum += int(digit)
#     return sum


# res = sum_of_digits(number)
# print(res)


