# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

ticket_num = 456234
first_part = ticket_num // 1000
second_part = ticket_num % 1000


def digits_sum(num):
    sum = 0
    while num > 0:
        sum = sum + num % 10
        num = num // 10
    return sum


sum_1 = digits_sum(first_part)
sum_2 = digits_sum(second_part)

if sum_1 == sum_2:
    print('Yes, it is your lucky ticket')
else:
    print('No, this ticket is regular')
