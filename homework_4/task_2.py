# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

bushes_number = int(input('Enter the number of bushes in a circle: '))
berries = []
for value in range(bushes_number):
    value = int(input('Enter amount of berries for this bush: '))
    berries.append(value)
print(berries)

sums = []
for i in range(0, len(berries)):
    if i == 0:
        b_sum = berries[i] + berries[i+1] + berries[len(berries) - 1]
        sums.append(b_sum)
    elif i == len(berries) - 1:
        b_sum = berries[len(berries) - 1] + berries[len(berries) - 2] + berries[0]
        sums.append(b_sum)
    else:
        b_sum = berries[i] + berries[i+1] + berries[i-1]
        sums.append(b_sum)
print(sums)

max_berry = sums[0]
for i in range(0, len(sums)):
    if sums[i] > max_berry:
        max_berry = sums[i]
print(max_berry)
