import random
import numpy as np
from random import uniform 
n = 10 
m = 10 
list_x = [[round(random.uniform(0, 100)) for x in range(n)] for y in range(m)] 

for i in range(len(list_x)): 
    print(list_x[i]) 

math_value_elem = [] 
min_value_elem = [] 
max_value_elem = [] 
disp_value_elem = [] 

for i in range(len(list_x)): 
    min_value_elem.append(min(list_x[i])) 
    max_value_elem.append(max(list_x[i])) 
    math_value_elem.append(np.mean(list_x[i])) 

for i in range(len(list_x)): 
    disp_value_elem.append(np.var(list_x[i]))
    
print("Мат. ожид. общее", np.mean(list_x))
print("Общая дисп.", np.var(list_x))
print("Общий max", max(max_value_elem)) 
print("Общий min", min(min_value_elem))
print(math_value_elem)
print(min_value_elem)
print(max_value_elem)
print(disp_value_elem)

##############################################################

import random 
from random import randint 
n = 40 
m = 60 
list1 = [round(random.randint(0, 100)) for x in range(n)] 
list2 = [round(random.uniform(0, 100)) for x in range(m)] 
set1 = set(list1) 
set2 = set(list2) 

print(set1.union(set2)) 
print(set1.intersection(set2)) 
print(set1.difference(set2)) 
print(set2.difference(set1)) 
print(set1.symmetric_difference(set2))

##############################################################

import random 
import copy 
def newdic(newlist, farm1, farm2): 
  return {i : [farm1[i][0], farm2[i][0], farm1[i][1], farm2[i][1]] for i in newlist} 

#farm_1 = {'1': [11, 70], '2': [5, 64], '3': [3, 73], '4': [2, 57], '5': [7, 65]} 
farm_1 = {i : [random.randint(1, 12), random.randint(50, 100)] for i in range (5)} 
print(farm_1) 
farm_2 = copy.deepcopy(farm_1) 
del farm_2[3], farm_2[4] 
print(farm_2) 
for i in range (3): farm_2[i][1] = random.randint(50, 100) 
print(farm_2) 
for i in range (3, 5): farm_2[i] = [random.randint(1, 12), random.randint(50, 100)] 
print(farm_2) 
farm_3 = newdic([3, 4], farm_1, farm_2) 
print(farm_3)
