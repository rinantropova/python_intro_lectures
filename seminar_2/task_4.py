#  Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random

number = int(input('Enter positive number: '))


def weights_list(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]


weights = weights_list(number, 1, 20)
print(weights)

max_weight = weights[0]
min_weight = weights[0]
for i in range(len(weights)):
    if weights[i] > max_weight:
        max_weight = weights[i]
    elif weights[i] < min_weight:
        min_weight = weights[i]

print(f'{min_weight} {max_weight}')
