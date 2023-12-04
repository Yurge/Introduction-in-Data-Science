import pandas as pd
import scipy.stats as ss
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

df = pd.read_csv('states.csv')
results = smf.ols('poverty ~ hs_grad', data=df).fit()
print(results.summary())

x, y = df['hs_grad'], df['poverty']

b0 = ss.linregress(x, y).intercept
b1 = ss.linregress(x, y).slope
line = b0 + b1 * x

fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_title('Связь бедности и уровня \n образования')
ax.set_xlabel('Среднее образование (%)')
ax.set_ylabel('Бедность (%)')
ax.plot(x, line, c='black')

plt.show()