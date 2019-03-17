from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

from scipy import integrate
import scipy.stats as st
import math

K = 1489       # макс страх выплата
N = 500        # число клиентов
V = 500000     # резерв компании
A = 1 / integrate.quad(lambda x: (x ** 3)*(K-x), 0, K)[0]

a = 0
b = K

def f(x) :
    return A*(x**3)*(K-x)

M = f(optimize.fmin(lambda x: -f(x), 0, disp = 0))

def devastation() :
    array_v = []
    while len(array_v) < N: 
    #случ. вел. равномерного распределения 
        u_1 = np.random.rand() 
        u_2 = np.random.rand()
    
        x_1 = a + (b - a) * u_1
        x_2 = M * u_2
        # Проверка значений на подхождения по условию (страница 16 шаг 3)
        if x_2 <= f(x_1): 
            array_v.append(x_1)
    #sum_v = sum(array_v)
    #print(sum_v)
    #Выплаты
    return array_v
    #if (0 <= V - array_b[i]):
    #    return 1
    #else:
    #    return 0

array_b = list()      # массив сумм выплат для каждого испытания
array_p = list()      # массив исходов (1 - не разорились, 0 - разорились)
array_d = list()      # массив дисперсий
array_mean = list()   # массив средних одиночный выплат для каждого испытания
O = 1000 # число испытаний
for i in range(O):
    arr_v = devastation()
    #Сумма выплат
    array_b.append(sum(arr_v))
    array_d.append(np.var(arr_v))
    array_mean.append(np.mean(arr_v))

for i in range(O):
    if (0 <= V - array_b[i]):
        array_p.append(1)
    else: 
        array_p.append(0)
        

mean = np.mean(array_mean)            # средняя выплата для всех испытаний
prob = sum(array_p) / len(array_p)    # эмпирическая вероятность не разориться
disp = math.sqrt(np.var(array_mean))  # общая дисперсия для испытаний

print(disp, "\t- дисперсия")
print(mean, "\t- средняя выплата для 1 человека")
print(1 - prob, "\t\t\t- эмпирическая вероятность разориться")
#print(sum(array_b))
#plot = plt.hist(array_v, bins = 50)

#print(A)
#print("Наш запас: ", V)
#print("Мы выплатили: ", sum_v)
#print("Разница:", V - sum_v)

# вероятность разорения по ЦПТ
theory_p = integrate.quad(lambda x: st.norm.pdf(x, mean, np.std(array_mean)), V / N, np.inf)[0]
print(theory_p, "\t- вероятность разорения по ЦПТ")
hist = plt.hist(array_mean)

#https://math.semestr.ru/math/expectation-continuous.php
A = 1 / integrate.quad(lambda x: x ** 3 * (K - x), 0, K)[0]
mean = integrate.quad(lambda x: x * f(x), 0, K)[0]
var = integrate.quad(lambda x: x ** 2 * f(x), 0, K)[0] - mean ** 2
std = math.sqrt(var)
#print(mean)
#print(std)
#1 - st.norm.cdf(V / N, mean, std)
#1 - integrate.quad(lambda x: density((V - N * mean) / (std * math.sqrt(N)), K))[0]
X = (V - N * mean) / (std * math.sqrt(N))
#print(X)
print(1 - st.norm.cdf(X, 0, 1))
