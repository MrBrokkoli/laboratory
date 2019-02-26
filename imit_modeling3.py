import numpy as np
import numpy.random as rnd
import math as m
import matplotlib.pyplot as plt
import scipy
from scipy import optimize

## 
# Вариант 2, считается по Нейману
#
def f(x) :
    l = 10
    k = 5
    return (k / l) * (x / l)**(k - 1) * np.exp(-(x / l)**k)

array_v = list()
a = 0
b = 10
n = 10000
M = f(optimize.fmin(lambda x: -f(x), 0, disp = 0))
print(M)
while len(array_v) < n: 
#случ. вел. равномерного распределения 
    u_1 = np.random.rand() 
    u_2 = np.random.rand()
    
    x_1 = a + (b - a) * u_1
    x_2 = M * u_2
    # Проверка значений на подхождения по условию (страница 16 шаг 3)
    if x_2 <= f(x_1): 
        array_v.append(x_1)
        
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
