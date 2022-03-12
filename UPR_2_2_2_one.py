import numpy as np
import pandas as pd
from scipy import stats as sc
import statistics as st

X_i = np.array([22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34])
X_ii = pd.Series([22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34])

# Numpy
print('--------------Numpy ---------------')
print('Матожидание ->', np.average(X_i))
print('Дисперсия ->', round(np.var(X_i), 3))
print('СКО ->', round(np.std(X_i), 3))
print('Медиана ->', np.median(X_i))
(trash, index, counts) = np.unique(X_i, return_index=True, return_counts=True)
mode = X_i[index[np.argmax(counts)]]
print('Мода ->', mode)
print('--------------Numpy ---------------')
print()

# Scipy
print('--------------Scipy---------------')
A = sc.mode(X_i)
Z = sc.describe(X_i)
Dispersia = Z.variance
print('Матожидание ->', Z.mean)
print('Дисперсия ->', Dispersia)
print('СКО ->', round(pow(Dispersia, 1 / 2), 3))
print('Медиана ->', st.median(X_i))
print('Мода ->', A.mode)
print('--------------Scipy---------------')
print()

# Pandas
print('--------------Pandas---------------')
Mat = X_ii.mean()
Dispersia = X_ii.var()
SKO = X_ii.std()
Mediana = X_ii.median()
Moda = X_ii.mode()
print("Матожидание ->", Mat)
print("Дисперсия ->", Dispersia)
print("СКО ->", round(SKO, 3))
print("Медиана ->", Mediana)
print('Мода ->')
print(Moda)
print('--------------Pandas---------------')
