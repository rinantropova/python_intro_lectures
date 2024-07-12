"""
Написать EDA (Exploratory Data Analysis) для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы
"""

import seaborn as sns
import matplotlib.pyplot as mpl

penguins = sns.load_dataset("penguins")
# penguins.head()
# 1
# sns.scatterplot(data=penguins, x="sex", y="body_mass_g")

# 2
# sns.scatterplot(data=penguins, x="body_mass_g", y="flipper_length_mm", size="bill_length_mm", hue="bill_length_mm",
#                 sizes=(10,100))

# sns.scatterplot(data=penguins, x="body_mass_g", y="bill_length_mm", hue="island", style="species")

# 3
# data_columns = ['species', 'island', 'bill_length_mm', "bill_depth_mm", 'flipper_length_mm', 'body_mass_g']
# graph = sns.PairGrid(penguins[data_columns], hue='body_mass_g', palette='deep')  # plot's options
# graph = graph.map_diag(mpl.hist)  # diagonal plots
# graph = graph.map_offdiag(mpl.scatter)  # other plots' options
# body_mass = {'light': 3000, 'light_heavy': 4000, 'medium': 5000, 'medium_heavy': 5500, 'heavy': 6000}
# graph = graph.add_legend(legend_data=body_mass, title='Body mass')  # legend

# 4
# sns.displot(data=penguins, x='flipper_length_mm', y='body_mass_g', cbar=True)
# data = penguins.pivot_table(index='species', columns='island', values='body_mass_g')  # to prepare data with columns
# # and lines and values
# sns.heatmap(data)
# mpl.xlabel('Island', size=14)
# mpl.ylabel('Penguins species', size=14)

# 5
# sns.displot(data=penguins, x='body_mass_g', kind='hist', col='sex', hue='species')

penguins['body_mass_g'].hist(bins=10)

mpl.show()
