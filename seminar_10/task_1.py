"""
Задача №1. Решение в группах
1. Изобразите отношение households к population с помощью точечного графика
1. Визуализировать longitude по отношения к median_house_value, используя линейный график
2. Представить гистограмму по housing_median_age
3. Изобразить гистограмму по median_house_value с оттенком housing_median_age
"""

# import seaborn.objects
# from seaborn import histplot
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('california_housing_test.csv')

# # 1.
# # Mine:
# # pl = seaborn.objects.Plot(df, "households", "population")
# # pl.add(seaborn.objects.Dot())
#
# # Seminar's:
scatter_plot = sns.scatterplot(data=df, x='households', y='population')

scatter_plot.set_title('Relation between Households and Population')
scatter_plot.set_xlabel('Households')
scatter_plot.set_ylabel('Population')
# plt.show()


# 2.
# Mine:
# pl_1 = seaborn.objects.Plot(df, 'longitude', 'median_house_value', color='region', linestyle='event')
# pl_1.add(seaborn.objects.Line(), seaborn.objects.Agg())
# # Seminar's:
sns.relplot(data=df, x='longitude', y='median_house_value', kind='line')
# plt.show()

# # 3.
sns.histplot(data=df, x='housing_median_age')
# plt.show()

# 4.
sns.histplot(df, x='median_house_value', hue='housing_median_age')
plt.show()