# Задача №3. Решение в группах
# 1. Определить какое максимальное и минимальное значение median_house_value
# 1. Показать максимальное median_house_value, где median_income = 3.1250
# 1. Узнать какая максимальная population в зоне минимального значения median_house_value

import pandas as pd

df = pd.read_csv('california_housing_test.csv')

# 1. максимальное и минимальное значение median_house_value
print(f'Min value = {df['median_house_value'].min()}, max value = {df['median_house_value'].max()}')

# 2. максимальное median_house_value, где median_income = 3.1250
print(type(df['median_house_value']))
print(df[df['median_income'] == 3.1250]['median_house_value'].max())

# 3. максимальная population в зоне минимального значения median_house_value
print(df[df['median_house_value'] == df['median_house_value'].min()]['population'].max())