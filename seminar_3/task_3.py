# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# 1:
new_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"},
        {" VIII": " S007 "}]
unique_values = {val for dic in new_dict for val in dic.values()}
print(unique_values)

# 2:
# all_values = [val for dic in new_dict for val in dic.values()]
# unique_values = set(all_values)
# print(unique_values)


# 3:
# from collections import defaultdict
# unique_values_dict = defaultdict(set)
#
# for dic in new_dict:
#         for key, value in dic.items():
#                 unique_values_dict[key].add(value)
#
# unique_values = set(val for values_set in unique_values_dict.values() for val in values_set)
# print(unique_values)