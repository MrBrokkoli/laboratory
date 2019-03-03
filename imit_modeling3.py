import numpy as np
import numpy.random as rnd
import math as m
import matplotlib.pyplot as plt
import scipy
from scipy import optimize
from scipy import stats

## 
# Вариант 2, считается по Нейману
#
def f(x) :
    return (k / l) * (x / l)**(k - 1) * np.exp(-(x / l)**k)

def F(x) :
    return 1 - np.exp(-(x / l)**k)
#l*numpy.random.weibull 
l = 10
k = 5
array_v = list()
n = 10000
#M = f(optimize.fmin(lambda x: -f(x), 0, disp = 0))
#print(M)
#while len(array_v) < n: 
#случ. вел. равномерного распределения 
 #   u_1 = np.random.rand() 
 #   u_2 = np.random.rand()
    
#    x_1 = a + (b - a) * u_1
#    x_2 = M * u_2
    # Проверка значений на подхождения по условию (страница 16 шаг 3)
#    if x_2 <= f(x_1): 
#        array_v.append(x_1)
array_v = l * np.random.weibull(k, n)         
plot = plt.hist(array_v, bins = 50)

#########################################################################################

array_p = list()
for var in array_v :
    if (var < 4) :
        array_p.append(0)
    elif (var < 15) :
        array_p.append(m.cos(var * m.pi / 11 + 7 * m.pi / 11) + 1)
    elif (var < 25) :
        array_p.append(7/4 + var / 30 - (var ** 2) / 900)
    else : 
        array_p.append(0)
plot = plt.hist(array_p, bins = 50)

##########################################################################################

def mean_confidence_interval(data, confidence=0.95): 
    a = 1.0 * np.array(data) 
    n = len(a) 
    m, se = np.mean(a), scipy.stats.sem(a) 
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1) 
    return m, m-h, m+h 

# Рассчёт доверительного интервала
#print(st.norm.interval(0.95, loc=np.mean(array_power), scale=st.sem(array_power))) 
center, left, right = mean_confidence_interval(array_p) 
print(left, center, right)

###########################################################################################

a = 5
b = 10
array_v2 = list()

M = f(optimize.fmin(lambda x: -f(x), 0, disp = 0))
print(M)
while len(array_v2) < n: 
#случ. вел. равномерного распределения 
    u_1 = np.random.rand() 
    u_2 = np.random.rand()
    
    x_1 = a + (b - a) * u_1
    x_2 = M * u_2
    # Проверка значений на подхождения по условию (страница 16 шаг 3)
    if x_2 <= f(x_1): 
        array_v2.append(x_1)

#print(array_v2)
array_p2 = list()
for var in array_v2 :
    if (var < 4) :
        array_p2.append(0)
    elif (var < 15) :
        array_p2.append(m.cos(var * m.pi / 11 + 7 * m.pi / 11) + 1)
    elif (var < 25) :
        array_p2.append(7/4 + var / 30 - (var ** 2) / 900)
    else : 
        array_p2.append(0)
plot = plt.hist(array_p2, bins = 50)
center, left, right = mean_confidence_interval(array_p2) 
print(left, center, right)
