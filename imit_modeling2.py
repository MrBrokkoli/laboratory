from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

from scipy import integrate
import scipy.stats as st
import math

K = 1489       # макс страх выплата
N = 500    # число клиентов
V = 500000    # резерв компании
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

array_b = list()
array_p = list()
array_d = list()
array_mean = list()
for i in range(100):
    arr_v = devastation()
    #Сумма выплат
    array_b.append(sum(arr_v))
    array_d.append(np.var(arr_v))
    array_mean.append(np.mean(arr_v))

for i in range(50):
    if (0 <= V - array_b[i]):
        array_p.append(1)
    else: 
        array_p.append(0)
        

mean = np.mean(array_mean)
prob = sum(array_p) / len(array_p)
disp = math.sqrt(np.mean(array_d))
#print(array_b)
#print(array_p)
print(1 - prob)
print(disp)
print(mean)
#print(sum(array_b))
#plot = plt.hist(array_v, bins = 50)

#print(A)
#print("Наш запас: ", V)
#print("Мы выплатили: ", sum_v)
#print("Разница:", V - sum_v)

integrate.quad(lambda x: st.norm.pdf(x, mean, disp), V / N, np.inf)[0]