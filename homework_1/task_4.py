# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

print('Enter n pieces: ')
n = int(input())
print('Enter m pieces: ')
m = int(input())
print('Enter k pieces: ')
k = int(input())

if k < n * m and (k % m == 0 or k % n == 0):
    print('Yes')
else:
    print('No')