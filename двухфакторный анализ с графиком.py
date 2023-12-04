import pandas as pd
import pingouin as pg
import matplotlib.pyplot as plt

df = pd.read_csv('atherosclerosis.csv')
aov = pg.anova(dv='expr', between=['age', 'dose'], data=df)
print(aov)

# рассчитываем средние
means = df.groupby(by=['age', 'dose']).mean().expr.values
# рассчитываем доверительные интервалы
sems = [x*1.96 for x in df.groupby(by=['age', 'dose']).sem().expr.values]

# строим график
fig, ax = plt.subplots()
ax.set_xticks([2.25, 4.25])
ax.set_xticklabels(['низкая', 'высокая'])
ax.errorbar(x=[2.1, 4.1], y=means[:2], yerr=sems[:2], capsize=3,
            marker='s', color='black', linestyle='--')
ax.errorbar(x=[2.4, 4.4], y=means[2:], yerr=sems[2:],
            capsize=3, marker='s', color='brown')
ax.set_title('Экспрессия гена в зависимости от дозировки \n и возраста пациентов')
ax.grid()
ax.set_xlabel('Дозировка')
ax.set_ylabel('Уровень экспрессии')
ax.legend(['молодые', 'взрослые'], loc='upper center')
plt.show()