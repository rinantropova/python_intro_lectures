# Задача №2. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

from math import pi

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]  # list of tuples

# simple solution
square_area = []
for i in range(0, len(orbits)):
    if orbits[i][0] != orbits[i][1]:
        s = pi * orbits[i][0] * orbits[i][1]
        square_area.append(s)
# print(square_area)

max_orbit = 0
index = 0
for i in range(0, len(square_area) - 1):
    if square_area[i] > max_orbit:
        max_orbit = square_area[i]
        index = i
print(orbits[index])


# with function find_farthest_orbit(orbits)

def find_farthest_orbit(list_of_orbits):
    max_area = 0
    farthest_orbit = None

    for orbit in list_of_orbits:
        a, b = orbit
        if a != b:
            area = pi * a * b
            if area > max_area:
                max_area = area
                farthest_orbit = orbit
    return farthest_orbit


print(*find_farthest_orbit(orbits))


# more efficient way:
def find_farthest_orbit2(list_of_orbits):
    return max((orbit for orbit in list_of_orbits if orbit[0] != orbit[1]),
               key=lambda x: pi * x[0] * x[1],
               default=None)


print(find_farthest_orbit2(orbits))


# seminar's:
# lst = [1, 3, 3, 5]
# print(max(lst, key=lst.count))

def find_farthest_orbit3(orbits):
    return max((orbit for orbit in orbits if orbit[0] != orbit[1]), key=lambda orbit: pi * orbit[0] * orbit[1])


print(find_farthest_orbit3(orbits))



