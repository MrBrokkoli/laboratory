import numpy as np 
import scipy.stats as st
from operator import add 
import math


# Получить матрицу С
# Умножить на Y
# Получить Z распределённый как X

G = [
      [2, -1, 0], 
      [-1, 2, -1], 
      [0, -1, 2]
    ]         # матрица ковариаций
mu = [3, -5, 10] # вектор средних

C = np.linalg.cholesky(G) # нижняя треугольная матрица
print(C) 

#np.matmul(C, C.T) 
m = 3         # размерность матрицы ковариаций
n = 10000     # длина вектора
Y = [np.random.normal(0, 1, n) for i in range(m)]  # m векторовов размерности n с нормальным расределением
Z = np.matmul(C, Y) 
Z = list(map(add, Z, mu)) 
#print(Z) 
evaluation = np.cov(Z) # оценка матрицы ковариаций 
print(evaluation)
i = 1 
j = 2 
np.corrcoef(Z[i - 1], Z[j - 1])[1, 0] # проверка гипотезы равенства 

r = np.corrcoef(Z[i], Z[j])[1,0] # эмпирический коэффицент корреляции
print("r =", r)
p = G[i][j] / math.sqrt(G[i][i]*G[j][j])
print("p =", p)

zr = np.arctanh(r)
zp = np.arctanh(p)

#mean = math.log((1 + p) / (1 - p)) / 2
std = 1 / math.sqrt(len(Z[i]) - 3)

# https://www.youtube.com/watch?v=R2bGZreVtDc
stat = (zr - zp) / std
norm_q = st.norm.ppf(0.95)

print("stat:\t" + str(stat) + "- наша статистика")
print("q:\t" + str(norm_q) + "- квантиль нормального распределения")
