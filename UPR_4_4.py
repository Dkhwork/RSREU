import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as sc

arr = pd.read_csv('StudentsPerformance.csv')

# Построить диаграммы рассеяния (в документе UPR_4)

# Для основных факторов (определил, что это
# reading score and writing score, math score and writing score, math score and reading score)
# определить коэффициент корреляции построить построить корреляционные связи

slope, intercept, r, *__ = sc.stats.linregress(arr['math score'], arr['reading score'])
fig, ax = plt.subplots()
ax.plot(arr['math score'], arr['reading score'], linewidth=0, marker='s', label='Диаграмма рассеяния')
ax.plot(arr['math score'], intercept + slope * arr['math score'], color = 'r', label='Корреляционная связь')
ax.set_xlabel('math score')
ax.set_ylabel('reading score')
ax.legend(facecolor='white')
ax.grid()


slope, intercept, r, *__ = sc.stats.linregress(arr['math score'], arr['writing score'])
fig, ax = plt.subplots()
ax.plot(arr['math score'], arr['writing score'], linewidth=0, marker='s', label='Диаграмма рассеяния')
ax.plot(arr['math score'], intercept + slope * arr['math score'], color = 'r', label='Корреляционная связь')
ax.set_xlabel('math score')
ax.set_ylabel('writing score')
ax.legend(facecolor='white')
ax.grid()

slope, intercept, r, *__ = sc.stats.linregress(arr['reading score'], arr['math score'])
fig, ax = plt.subplots()
ax.plot(arr['reading score'], arr['math score'], linewidth=0, marker='s', label='Диаграмма рассеяния')
ax.plot(arr['reading score'], intercept + slope * arr['reading score'], color = 'r', label='Корреляционная связь')
ax.set_xlabel('reading score')
ax.set_ylabel('math score')
ax.legend(facecolor='white')
ax.grid()



# Определить коэффициент ковариации(через ковариацию)
Std = arr.std()
wm_R = arr["writing score"].cov(arr["math score"]) / (Std["writing score"] * Std["math score"])
wr_R = arr["math score"].cov(arr["reading score"]) / (Std["math score"] * Std["reading score"])
mr_R = arr["reading score"].cov(arr["reading score"]) / (Std["reading score"] * Std["reading score"])
print("Коэффициент корреляции письмо-математика:",round(wm_R,3))
print("Коэффициент корреляции письмо-чтение:",round(wr_R, 3))
print("Коэффициент корреляции чтение-математика:",round(mr_R, 3))

print()
wm_R = arr["writing score"].corr(arr["math score"])
wr_R = arr["writing score"].corr(arr["reading score"])
mr_R = arr["math score"].corr(arr["reading score"])
print("Коэффициент корреляции письмо-математика:",round(wm_R, 3))
print("Коэффициент корреляции письмо-чтение:",round(wr_R, 3))
print("Коэффициент корреляции чтение-математика:",round(mr_R, 3))
print()

#Для наиболее значимых факторов получить корреляционную
#матрицу и найти собственные значения и собственные вектора.
R = arr.corr()
print(R)

print(np.linalg.eig(R))

A = arr['gender']
print(arr.gender.value_counts())

plt.show()

