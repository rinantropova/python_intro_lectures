# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе. Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50.
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

import random

print('Enter amount of days for observation (from 1 to 100): ')
days = int(input())

if 1 > days > 1000:
    print('Incorrect value')


def mean_temp_list(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]


mean_temp = mean_temp_list(days, -50, 50)
print(mean_temp)

pos_count = 0
current_count = 0
for i in mean_temp:
    if i > 0:
        current_count += 1
        pos_count = max(pos_count, current_count)
    else:
        current_count = 0
print(pos_count)


