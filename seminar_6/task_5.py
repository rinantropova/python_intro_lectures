def fill_list(num):
    res = [el for el in range(num)]
    return res


print(fill_list(5))


# generator:

def func(num):
    for el in range(num):
        yield el

for el in func(5):
    print(el, end=' ')

print()
for el in func(5):
    print(el, end=' ')

print()
print((el for el in range(5)))

print({el: el for el in range(5)})