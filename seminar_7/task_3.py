# Задача №3. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод:                                         Вывод:
# values = [0, 2, 10, 6]                        same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

def same_by(func, obj):
    if not obj:
        return True

    first_value = func(obj[0])
    for item in obj:
        if func(item) != first_value:
            return False
    return True


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('‘same’')
else:
    print('‘different’')


# seminar's:
def same_by2(characteristic, objects):
    return len(set(map(characteristic, objects))) < 2


values2 = [0, 2, 10, 6]
if same_by2(lambda x: x % 2, values2):
    print('‘same’')
else:
    print('‘different’')
