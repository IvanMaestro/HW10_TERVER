# Провести дисперсионный анализ для определения того,
# есть ли различия среднего роста среди взрослых футболистов,
# хоккеистов и штангистов. Даны значения роста в трех группах
# случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

N_0 = 'Нет статистически значимых различий'
N_1 = 'Статистически значимые различия имеются, нулевая гипотеза отвергается'

football = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
powerlift = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
alfa = 0.05

p1 = stats.shapiro(football)[1]
p2 = stats.shapiro(hockey)[1]
p3 = stats.shapiro(powerlift)[1]
if p1 > alfa and p2 > alfa and p3 > alfa:
    print('Данные распределены нормально')
else:
    print('Распределение отлично от нормального')
# print(stats.shapiro(football))
# print(stats.shapiro(hockey))
# print(stats.shapiro(powerlift))
pvalue = stats.f_oneway(football, hockey, powerlift)[1]
# print(stats.f_oneway(football, hockey, powerlift))

if pvalue > alfa:
    print(N_0)
else:
    print(N_1)

plt.boxplot([football, hockey, powerlift], labels=["football", "hockey", "lifting"])
plt.show()
