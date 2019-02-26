import math 
import random 
import numpy as np 
import scipy.stats
import matplotlib.pyplot as plt

# Функция для рассчёта плотности
def pf(y): 
    return (1 / (4 * math.pi)) * (2 + math.cos(y)) 

# Функция для рассчёта статистики хи квадрат для проверки на соответствие выбранному распределению 
def stat(arr_inter, arr_prob, n): 
    sum_stat = 0 
    for i in range(0, r): 
        sum_stat += (arr_inter[i] * arr_inter[i]) / (n * arr_prob[i]) 

    return sum_stat 

# Функция распределения
def f(y): 
    return (math.sin(y) + 2 * y) / (4 * math.pi) 

# Функция для построения интервалов вероятности попадания в них для гипотезы согласия
def create_interval(arr, r): 
    help_arr = [0] * r 
    probability_arr = [0] * r 
    step = 2 * math.pi / r

    arr = sorted(arr) 
    x_min = arr[0] 
    x_max = arr[len(arr) - 1] 
    
    # рассчёт теоретической вероятности попадения в интервал
    for i in range(0, r): 
        probability_arr[i] = f(step * (i + 1)) - f(step * (i)) 
        for j in range(0, len(arr)): 
            if arr[j] >= step * i and arr[j] < step * (i + 1): 
                help_arr[i] = help_arr[i] + 1 
    
    return help_arr, probability_arr  

def density(args):
    result =[]
    for value in args:
        if 0 <= value and value <= 2 * math.pi:
            result.append((2 + math.cos(value)) / (4 * math.pi))
        else:
            result.append(0)
    return result

#print(random.random()) 
n = 5000 # размер выборки
r = 100 # число интервалов
M = pf(-(1 / math.pi))
print("M =", M)

count = 0 
array = [] 
probability = [] 
while len(array) < n: 
#случ. вел. равномерного распределения 
    u = np.random.rand() 
    y = np.random.rand() * 2 * math.pi 
    
    # Проверка значений на подхождения по условию (страница 16 шаг 3)
    if u <= (pf(y) / M * (1 / (2 * math.pi - 0))): 
        array.append(y) 
    else: 
        count += 1 

#print("Полученная выборка с заданным распределением: ", array) 
#print("Общее число не принятых значений", count) 
intervals, probability = create_interval(array, r) 
#print (probability) 
#print(empirical_func(intervals, r)) 
print(stat(intervals, probability, n) - n) 

if stat(intervals, probability, n) - n < scipy.stats.chi2.isf(0.1, r-1): 
    print("Попали в доверительный интервал, уровень значимости 0.1 (<", scipy.stats.chi2.isf(0.1, r-1), ")") 
else: 
    print("Не попали в доверительный интервал")
    
r = np.arange(0, 2 * math.pi, 0.1)

array_sorted = sorted(array)
#print(array_sorted)
#plot = plt.plot(r, density(r), color = 'red', linewidth = 3)
plot = plt.plot(array_sorted, density(array_sorted), color = 'red', linewidth = 3)
