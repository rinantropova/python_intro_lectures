# 1
# temps = "-20 30 -40 50 10 -10".split()
# # list of strings
# temps_2 = [-20, 30, -40, 50, 10, -10]
# warm_length = 0
# max_length = 0
# for elem in temps_2:
#     num = int(elem)
#     if num > 0:
#         warm_length += 1
#     else:
#         warm_length = 0
#     if warm_length > max_length:
#         max_length = warm_length
# print(max_length)
#
#
# def weather_length(temp_list, warm_days=0, max_days=0):
#     if len(temp_list) == 0:
#         return max_days
#     elif temp_list[0] > 0:
#         warm_days += 1
#         max_days = max(max_days, warm_days)
#     else:
#         warm_days = 0
#     return weather_length(temp_list[1:], warm_days, max_days)
#
# print(weather_length(temps_2))




# 2
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
numbers = [5, 7, 12, 9, 4, 8]
# count = 0
# for i in range(1, len(numbers)):
#     curr_elem = numbers[i]
#     prev_elem = numbers[i - 1]
#     if curr_elem > prev_elem:
#         count += 1
#
# print(count)
#
def count_elem(nums, counter=0):
    if len(nums) == 1:
        return counter
    elif nums[1] > nums[0]:
        counter += 1
        # print(counter)
    return count_elem(nums[1:], counter)


print(count_elem(numbers))



def count_elem_2(num):
    if len(num) == 1:
        return 0
    elif num[1] > num[0]:
        return 1 + count_elem_2(num[1:])
    else:
        return count_elem_2(num[1:])


print(count_elem_2(numbers))