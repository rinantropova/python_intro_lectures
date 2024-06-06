# colors = ['red', '8898', 'blue']
# data = open('file.txt', 'a') # set a mode, in which we're gonna work in
# data.writelines(colors) # no separators
# data.close()


# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 3\n') 

# print(56)


#reading mode:
path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close