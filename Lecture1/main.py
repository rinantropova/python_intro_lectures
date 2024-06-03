# a = 5
# b = 5.89
# c = 'hello'

# print("{} - {} - {}".format(a, b, c))




# print('Enter first row')
# a = int(input())
# b = int(input('Enter new number: '))

# print(a, '+', b, '=', a + b)



# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))



# a = 5.89956
# b = 6.67575
# print(round(a*b, 3))



# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5


# a = 1 > 4
# print(a) # False
# —------------------------------------
# a = 1 < 4 and 5 > 2
# print(a) # True
# # —------------------------------------
# a = 1 == 2
# print(a) # False
# # —------------------------------------
# a = 1 != 2
# print(a) # True
# # —------------------------------------
# a = 'qwe'
# b = 'qwe'
# print(a == b) # True
# # —------------------------------------
# a = 1 < 3 < 5 < 10
# print (a) # True


# username = input("Enter the name: ")
# if username == 'Masha':
#     print("Yey, this is Masha!")
# elif username == 'Marina':
#     print("I've been waiting for you so long, Marina!")
# elif username == "Ilnar":
#     print("Ilnar is great")
# else:
#     print("Hi,", username)




# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa) # 9




# i = 0
# while i < 5:
  
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)




# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1




# a = 'qwerty'
# for i in a:
#     print(i)




# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)





# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# # print(len(text)) # 39
# # print('ещё' in text) # True
# # print(text.lower()) # съешь ещё этих мягких французских булок
# # print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок



text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[20:])
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...
print(text)