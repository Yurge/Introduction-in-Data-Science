import pandas as pd
import scipy.stats as ss
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

df = pd.read_csv('states.csv')
results = smf.ols(formula='poverty ~ metro_res + white + hs_grad + female_house', data=df).fit()
print(results.summary())

x, y, z = df['hs_grad'], df['poverty'], df['white']

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z)
ax.set_title('Связь бедности c уровнем образования \n'
             ' и процентом белого населения')
ax.set_xlabel('Среднее образование (%)')
ax.set_ylabel('Бедность (%)')
ax.set_zlabel('Белое население (%)')

plt.show()