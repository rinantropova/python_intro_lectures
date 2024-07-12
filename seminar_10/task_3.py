"""
Задача №3. Решение в группах
1. Создать новый столбец в таблице с пингвинами, который будет отвечать за показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)
"""

import seaborn as sns
import matplotlib.pyplot as mpl

penguins = sns.load_dataset("penguins")

def length_group(x):
    if x < 35:
        return 'low'
    elif 35 <= x <= 42:
        return 'middle'
    else:
        return 'high'


penguins['height_group'] = penguins['bill_length_mm'].apply(length_group)
print(penguins[penguins['height_group'] == 'low'])