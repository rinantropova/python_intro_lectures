# // Даны два файла, в каждом из которых находится запись
# // многочлена. Сформировать файл содержащий сумму
# // многочленов.

from csv import DictWriter, DictReader
from os.path import exists


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Number'])
        f_w.writeheader()


def get_data() -> int:
    number = input('Enter a number: ')
    return int(number)


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'Number': lst[0]}
    res.append(obj)
    standard_write(file_name, res)


def standard_write(file_name, res):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Number'])
        f_w.writeheader()
        f_w.writerows(res)


def main(file_name_1, file_name_2, last_file_name):
    create_file(file_name_1)
    write_file(file_name_1, [get_data()])

    create_file(file_name_2)
    write_file(file_name_2, [get_data()])

    create_file(last_file_name)
    res_1 = read_file(file_name_1)
    res_2 = read_file(file_name_2)
    sum_res = read_file(last_file_name)
    sum_res.append({'Number': int(res_1[0]['Number']) + int(res_2[0]['Number'])})
    write_file(last_file_name, sum_res)


file_name_1 = 'first_file.csv'
file_name_2 = 'second_file.csv'
last_file_name = 'summary.csv'
main(file_name_1, file_name_2, last_file_name)
