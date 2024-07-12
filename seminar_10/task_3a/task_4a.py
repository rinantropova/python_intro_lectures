"""
Задача №4. Решение в группах
1. Изобразить гистограмму по flipper_length_mm с оттенком height_group. Сделать анализ
"""
import matplotlib.pyplot as plt
from seaborn import histplot
from pandas import read_csv

penguins = read_csv('penguins.csv')
print(penguins)
histplot(penguins, x='flipper_length_mm', hue='height_group')
plt.show()