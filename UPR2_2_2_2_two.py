import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats as sc
import statistics as st
from scipy.stats import binom
import seaborn as sb

s = np.random.normal(0.5, 0.1, 100)
print(s)

X_i = np.array(s)
X_ii = pd.Series(s)

# numpy
print()
print('--------------Numpy ---------------')
print("Матожидание ->", np.average(X_i))
print("Дисперсия ->", round(np.var(X_i), 3))
print("СКО ->", round(np.std(X_i), 3))
print("Медиана ->", np.median(X_i))
print('--------------Numpy ---------------')
print()

# Scipy
print()
print('--------------Scipy---------------')
A = sc.mode(X_i)
print(A)
Z = sc.describe(X_i)
print("dispersia", Z)
Dispersia = Z.variance
print(Dispersia)
print('Матожидание ->', Z.mean)
print('Дисперсия ->', round(Dispersia, 3))
print('СКО ->', round(pow(Dispersia, 1 / 2), 3))
print('Медиана ->', st.median(X_i))
print('Мода ->', A.mode)
print('--------------Scipy---------------')
print()

# Pandas
print()
Mat = X_ii.mean()
Dispersia = X_ii.var()
SKO = X_ii.std()
Mediana = X_ii.median()
Moda = X_ii.mode()
print('--------------Pandas---------------')
print("Матожидание ->", Mat)
print("Дисперсия ->", round(Dispersia, 3))
print("СКО ->", round(SKO, 3))
print("Медиана ->", Mediana)
print('Мода ->')
print(Moda)
print('--------------Pandas---------------')
print()

# Вывод графика ФПР
weights = np.ones_like(np.array(s))/float(len(np.array(s)))
plt.hist(s, weights=weights, bins = 10)
plt.grid()
sb.displot(X_i, kde=True, bins = 10)
plt.grid()

'''X = np.cumsum(weights)
plt.figure()
plt.plot(s, X)
plt.grid()'''
#Сохранение графика ФПР
plt.savefig('ФПР.png')
plt.show()
#Сохранение массива в файл
np.savetxt('Array.txt', X_i)
