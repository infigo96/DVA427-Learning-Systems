import numpy as np
import time
from sympy import *

def NewPop(sizePop):
    Pop = np.zeros((3, 5))
    for i in range (0, 3):
        Pop[i,:] = np.random.permutation(5)
    return Pop
np.random.seed(42)

data = np.genfromtxt('./berlin.txt', delimiter=',')
#print(data)

datanew = data[0:10][:]
print(datanew)

parent1 = np.random.permutation(10)
parent2 = np.random.permutation(10)

print('parent1 is: ' + str(parent1))
print('parent2 is: ' + str(parent2))
if parent1.all == parent2.all:
    print('FUCK')
print(NewPop(3))

#a = np.matrix('1 2 3 4; 5 6 7 8; 9 10 11 12')
#print(a)
#np.random.shuffle(a)

#print(a)