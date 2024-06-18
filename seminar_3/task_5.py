my_list = [10, 11, 20, 30, 55, 60]
# find even numbers on odd positions
for i in range(0, len(my_list), 2):
    if my_list[i] % 2 == 0:
        print(my_list[i], end=',')

# find even numbers on even positions
for i in range(1, len(my_list), 2):
    if my_list[i] % 2 == 0:
        print(my_list[i], end=',')
