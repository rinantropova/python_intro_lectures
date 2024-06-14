# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

s = int(input('Enter sum of 2 hidden numbers: '))
p = int(input('Enter product of 2 hidden numbers: '))


def find_nums(sum_value, product_value):
    discriminant = sum_value ** 2 - 4 * product_value
    if discriminant < 0:
        return None
    x_1 = (sum_value + discriminant ** 0.5) // 2
    x_2 = (sum_value - discriminant ** 0.5) // 2
    return f'{int(x_2)} {int(x_1)}'


result = find_nums(s, p)
if result:

    print(result)
else:
    print("No real solutions exist")