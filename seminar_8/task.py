# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа не должна быть линейной

from csv import DictWriter, DictReader
from os.path import exists


class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_phone_data():
    flag = False
    while not flag:
        try:
            first_name = input('Enter the first name: ')
            if len(first_name) < 2:
                raise NameError('The first name is too short!')
            last_name = input('Enter the last name: ')
            if len(last_name) < 4:
                raise NameError('The last name is too short!')
            phone = input('Enter phone number: ')
            if len(phone) < 10:
                raise NameError('The phone number is too short!')
        except NameError as err:
            print(err)
        else:
            flag = True
    return [first_name, last_name, phone]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['First name', 'Last name', 'Phone number'])
        f_w.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'First name': lst[0], 'Last name': lst[1], 'Phone number': lst[2]}
    res.append(obj)
    standard_write(file_name, res)


def row_search(file_name):
    last_name = input('Enter a last name: ')
    res = read_file(file_name)
    for row in res:
        if last_name == row['Last name']:
            return row
    return 'Entry is not found.'


def delete_row(file_name):
    row_num = int(input('Enter a row number for removing: '))  # request an input data to proceed
    res = read_file(file_name)  # open the drawer in the closet
    res.pop(row_num - 1)  # change the data in the drawer
    standard_write(file_name, res)  # to put our drawer to the closet back


def standard_write(file_name, res):  # to put our drawer to the closet back
    with open(file_name, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['First name', 'Last name', 'Phone number'])
        f_w.writeheader()
        f_w.writerows(res)


def update_row(file_name):
    row_num = int(input('Enter a row number for update: '))
    res = read_file(file_name)
    data = get_phone_data()
    res[row_num - 1]['First name'] = data[0]
    res[row_num - 1]['Last name'] = data[1]
    res[row_num - 1]['Phone number'] = data[2]
    standard_write(file_name, res)


def copy_to_file(file_name, new_file_name):
    row_num = int(input('Enter a row number to copy to a new file: '))
    res = read_file(file_name)
    if row_num <= 0 or row_num > len(res):
        print('Invalid row number')
        return
    row_to_copy = res[row_num - 1]
    with open(new_file_name, 'w', encoding='utf-8') as new_data:
        f_w = DictWriter(new_data, fieldnames=['First name', 'Last name', 'Phone number'])
        f_w.writeheader()
        f_w.writerow(row_to_copy)
# I was thinking to use shutil module, but it seems like this module is more useful for copying the whole file. I
# checked, that it's also possible to use it here, but first I'll have to copy the whole file to the new one and then
# overwrite the new file with the input row. Chosen by me approach seems to me more suitable for the task to copy only
# one row (there is no any implication in the task that I should preserve metadata of the original file in the new
# one as well).




def main():  # main function, as a supervisor, initiates all the actions, that can be done with a file
    while True:
        command = input('Enter a command: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):  # exist check
                create_file(file_name)
            write_file(file_name, get_phone_data())
        elif command == 'r':
            if not exists(file_name):
                print('File does not exist, please create a file with command w.')
                continue
            print(read_file(file_name))
        elif command == 'f':
            if not exists(file_name):
                print('File does not exist, please create a file with command w.')
                continue
            print(row_search(file_name))
        elif command == 'd':
            if not exists(file_name):
                print('File does not exist, please create a file with command w.')
                continue
            delete_row(file_name)
        elif command == 'u':
            if not exists(file_name):
                print('File does not exist, please create a file with command w.')
                continue
            update_row(file_name)
        elif command == 'c':
            if not exists(file_name):
                print('File does not exist, please create a file with command w.')
                continue
            copy_to_file(file_name, new_file_name)


file_name = 'phone.csv'
new_file_name = 'copy.csv'
main()
