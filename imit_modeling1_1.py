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
    for i in range(0,r) :
        sum_stat += ((arr_inter[i]-n*arr_prob[i])**2) / (n*arr_prob[i])
    return sum_stat

# Функция распределения
def f(y): 
    return (math.sin(y) + 2 * y) / (4 * math.pi) 

# Функция для построения интервалов вероятности попадания в них для гипотезы согласия
# @param array - случайная величина с заданным распределением
# @param r - число интервалов для разбиения
def create_interval(array, r) : 
    density_arr = [0] * r       # частота попадания в интервал
    probability_arr = [0] * r   # вероятность попадания в интервал
    step = 2 * math.pi / r      # длина интервала

    array = sorted(array)
    
    # рассчёт теоретической вероятности попадения в интервал
    for i in range(0, r) : 
        probability_arr[i] = f(step * (i + 1)) - f(step * (i)) 
        for j in range(0, len(array)) : 
            if array[j] >= step * i and array[j] < step * (i + 1) : 
                density_arr[i] += 1 
    
    return density_arr, probability_arr  

#print(random.random()) 
n = 5000               # размер выборки
r = 100                # число интервалов
M = pf(-(1 / math.pi))
#print("M =", M)

# Получение случайной величины с заданным распределением по методу отбора
# Y - вспомогательная случайная величина с равноерным распределением на промежутке [0; pi]
# U - случайная величина с равномерным распределением на промежутке [0;1]
count = 0 
array = []             # случайная величина с заданным распределением
probability_arr = []   # массив вероятностей попадания в интервал 
while len(array) < n: 
    u = np.random.rand() 
    y = np.random.rand() * 2 * math.pi 
    
    # Проверка значений на подхождения по условию (страница 16 шаг 3)
    if u <= (pf(y) / M * (1 / (2 * math.pi - 0))): 
        array.append(y)

# Получаем массив плотностей (частот попадания в интервал) и вероятность попадания в эти интервалы
density_arr, probability_arr = create_interval(array, r)
print("Статистика Хи квадрат: ", stat(density_arr, probability_arr, n))

if stat(density_arr, probability_arr, n) - n < scipy.stats.chi2.isf(0.1, r-1): 
    print("Попали в доверительный интервал, уровень значимости 0.1 (<", scipy.stats.chi2.isf(0.1, r-1), ")") 
else: 
    print("Не попали в доверительный интервал")
    
r = np.arange(0, 2 * math.pi, 0.1)

array_sorted = sorted(array)
plot = plt.plot(array_sorted, density(array_sorted), color = 'red', linewidth = 3)
