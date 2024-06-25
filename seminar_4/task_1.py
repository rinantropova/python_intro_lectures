# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# from collections import defaultdict

# values = input('Enter a string: ')
# new_str = list(map(str, values.split(" ")))
# print(new_str)
# # count = defaultdict(int)
# new_list = [] # new list to store rewritten values
#
# # for item in new_str:
# #     count[item] += 1
# #     if count[item] > 1:
# #         new_list.append(f'{item}_{count[item]-1}')
# #     else:
# #         new_list.append(item)
# #
# # print(new_list)
#
#
# # Another way with sets:
# seen = set() # set to track seen items
# for item in new_str:
#     if item in seen: # find the next available count for the duplicate
#         count = 1
#         new_item = f'{item}_{count}'
#         while new_item in seen:
#             count += 1
#             new_item = f'{item}_{count}'
#         new_list.append(new_item)
#         seen.add(new_item)
#     else:
#         new_list.append(item)
#         seen.add(item)
# print(new_list)


# Seminar solution:
input_string = "a a a b c a a d c d d"
words = input_string.split()
counts = {}
for word in words:
    if word not in counts:
        print(word, end=' ')
    else:
        print(f'{word}_{counts[word]}', end=' ')
    counts[word] = counts.get(word, 0) + 1


