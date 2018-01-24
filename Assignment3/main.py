import numpy as np
import os
import time
from sympy import *

def NewPop(sizePop):
    Pop = [np.random.permutation(52) for i in np.arange(sizePop)]
    return Pop

def Distance(a, b):
    return sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
# sqrt((Y-Y0)^2+(X-X0)^2)


def routeDistance(DistanceMatrix, Individual):
    a = np.arange(len(Individual))
    b = a + 1
    b[len(Individual) - 1] = 0
    return np.sum([DistanceMatrix[Individual[a[i],0]][Individual[b[i],0]]for i in np.arange(len(Individual))])

#np.random.seed(42)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
data = np.genfromtxt('./berlin.txt', delimiter=',')
distanceMatrix= [[Distance(i, j) for i in data] for j in data]
#print(distanceMatrix)
hej = routeDistance(distanceMatrix, np.transpose(NewPop(1)))
print(hej)

#Pop = NewPop(1)
#print(Pop)

#a = np.matrix('1 2 3 4; 5 6 7 8; 9 10 11 12')
#print(a)
#np.random.shuffle(a)

#print(a)