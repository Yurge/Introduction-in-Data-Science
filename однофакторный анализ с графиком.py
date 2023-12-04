import pandas as pd
import pingouin as pg
import matplotlib.pyplot as plt

df = pd.read_csv('genetherapy.csv')
aov = pg.anova(data=df, dv='expr', between='Therapy')

print(aov)

# список средних значений
means = [x for x in df.groupby(by='Therapy').mean().expr.values]
# список se * 1,96
sems = [x*1.96 for x in df.groupby(by='Therapy').sem().expr.values]

name = ['A', 'B', 'C', 'D']
plt.errorbar(x=name, y=means, yerr=sems, ecolor='black', capsize=3,
             marker="s", markersize=4, mfc="white", mec='black', fmt='o')
plt.title('Уровень экспрессии гена при различной терапии')
plt.grid()
plt.xlabel('Терапия')
plt.ylabel('Уровень экспрессии')
plt.show()