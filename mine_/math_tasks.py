"""
Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise,
return their sum.
"""
# num_1 = int(input('Enter the first number: '))
# num_2 = int(input('Enter the second number: '))
#
# product = num_1 * num_2
# if product <= 1000:
#     print(product)
# else:
#     print(num_1 + num_2)


"""
Exercise 2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous
number.
"""
# print('Printing current and previous number in range (10):')
# for num in range(0,10):
#     current_number = num
#     if num == 0:
#         previous_number = current_number
#     else:
#         previous_number = current_number - 1
#     new_sum = current_number + previous_number
#     print(f'Current number: {current_number}; Previous number: {previous_number}; Sum: {new_sum}')


"""
Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
"""
# characters = input("Enter a string of characters: ")
# for i in range(0, len(characters) - 1):
#     if i % 2 == 0:
#         print(characters[i], end=" ")


"""
Exercise 4: Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:
remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.
remove_chars("pynative", 2) so output must be native. Here, we need to remove the first two characters from a string.
Note: n must be less than the length of the string.
"""


# def remove_chars(characters, n):
#     new_chars = ''
#     if n > len(characters):
#         print('Number n is too big, enter it again!')
#         return ''
#     else:
#         return characters[n:]
#
#
# character = input('Add a string of characters: ')
# n = int(input('Add a number n: '))
# print(remove_chars(character, n))


"""
Exercise 5: Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. If numbers are different then 
return False.
"""

num = input('Add numbers: ').split( )
lst_1 = list(map(int, num))


def check_same(lst):
    if lst[0] == lst[len(lst) - 1]:
        return True
    else:
        return False


print(check_same(lst_1))






