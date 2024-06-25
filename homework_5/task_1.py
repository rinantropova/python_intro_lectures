# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = 3
b = 5
res = a ** b
print(res)


# recursion
def power(n, m):
    if m == 0:
        return 1
    elif m > 0:
        return n * power(n, m - 1)
    else:
        return 1 / n * power(n, m + 1)

print(power(a, b))


