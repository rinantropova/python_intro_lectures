# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)


# d['w'] = 'werty'
# print(d['q'])


dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента

# dictionary[895] = 98998
# print(dictionary)

# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))
    # print(item)
print(dictionary.items())
# for (k,v) in dictionary.items():
#     print(k, v)