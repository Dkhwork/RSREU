import matplotlib.pyplot as plt
import math

Fn = 'Данила'
ln = 'Хохлов'
Var = 22
N = len(Fn) + len(ln)
xi = [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
pi = [0.1, 0.15, 0.02, 0.15, 0.05, 0.01, 0.06, 0.1, 0.2, 0.06, 0.03, 0.07]
print(xi)
print(pi)
print(N)
#Проверяем верно ли все вывелось
s = sum(pi)
print(s)
if len(xi) == len(pi) and (sum(pi) == 1):
   print('размерность массивов одинакова')
   print('сумма вероятностей = 1')

M = sum([pi[i] * xi[i] for i in range(N)])
print('Матожидание', M)
D= sum([pi[i] * (xi[i] ** 2) for i in range(N)])- M ** 2
print('Дисперсия', D)
CKO = math.sqrt(D)
print('СКО', CKO)

fig, ax = plt.subplots(1) # от числа зависит сколько будет окон
plt.plot(xi,pi) # собственно откладываем по разным осям точки
plt.xlabel('xi') # называем оси
plt.ylabel('pi')
moda = max(pi)
Me = round(len(xi) / 2)
print('Мода распределения', moda)
print('медиана', Me)
plt.vlines(Me + Var, 0, pi[Me])
plt.vlines(pi.index(moda) + Var, 0, moda) #index показывает какой по счету будет величайшее число
plt.show()
fig. savefig('hohlov_UIR1/Функция плотности распределения.jpg')

a = []

#for i in range(0, len(xi)):
 # a.append(pi[n] + pi[i])
#fig, ax = plt.subplots(1) # от числа зависит сколько будет окон
#plt.plot(xi,a) # собственно откладываем по разным осям точки
#plt.xlabel('xi') # называем оси
#plt.ylabel('a')