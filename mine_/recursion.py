# 1
temps = "-20 30 -40 50 10 -10".split()
# list of strings
temps_2 = [-20, 30, -40, 50, 10, -10]
warm_length = 0
max_length = 0
for elem in temps_2:
    num = int(elem)
    if num > 0:
        warm_length += 1
    else:
        warm_length = 0
    if warm_length > max_length:
        max_length = warm_length
print(max_length)


def weather_length(temp_list, warm_days=0, max_days=0):
    if len(temp_list) == 0:
        return max_days
    if temp_list[0] > 0:
        warm_days += 1
        max_days = max(max_days, warm_days)
    else:
        warm_days = 0
    return weather_length(temp_list[1:], warm_days, max_days)

print(weather_length(temps_2))
