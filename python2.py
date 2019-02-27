import string
import random
import sys

def generator_function(n, k):
    for _ in range(n):
        yield ''.join(random.choices(string.ascii_letters, k=k))
        
N = 5
list1 = [''.join(random.choices(string.ascii_letters, k=N)) for _ in range(1000)]
list2 = list()
#list2 = generator_function(1000, 5)

for i in generator_function(1000, 5):
    list2.append(i)

#for i in list2:
#    print(i)
print(list1[:2], list2[:2])
print(sys.getsizeof(list1), sys.getsizeof(generator_function))
