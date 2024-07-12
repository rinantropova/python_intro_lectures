"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача
перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
"""

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
# print(data)


# # Just for the reference for the next solution, to compare the results, I have used get_dummies method:
# print(pd.get_dummies(data['whoAmI']).astype(int))


"""
No get_dummies method solution:
"""
# # 1 - We create a dictionary to map unique values to column name
# unique_v = data['whoAmI'].unique()
# columns = {value: f'{value}' for value in unique_v}
#
# # 2 - Then we create new columns with binary encoding
# for value, column_name in columns.items():
#     data[column_name] = pd.Series(data['whoAmI'] == value).astype(int)
#
# # Display the result:
# print(data[list(columns.values())])


"""
Solution with function:
"""


def create_one_hot(data, column):
    unique_v = data[column].unique()
    binary_df = pd.DataFrame()

    new_columns = {value: f'{value}' for value in unique_v}
    for value, new_column_name in new_columns.items():
        binary_df[new_column_name] = pd.Series(data[column] == value).astype(int)

    return binary_df


print(create_one_hot(data, 'whoAmI'))
