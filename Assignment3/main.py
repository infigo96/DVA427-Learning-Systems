import numpy as np
import os
import time
from sympy import *

def NewPop(sizePop):
    Pop = [np.random.permutation(52) for i in np.arange(sizePop)]
    return Pop
def Distance(a, b):
    #assert data is not empty
    return a+b

def initDistanceMatrix(data):
    return 11

def routeDistance(Matrix, Individual):
    #assert Matrix exists
    #Individual is right size
    #Indivudal
    return 1
#np.random.seed(42)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
data = np.genfromtxt('./berlin.txt', delimiter=',')
A = [[Distance(i, j) for i in data for j in data]]

Pop = NewPop(3)
print(Pop)

#a = np.matrix('1 2 3 4; 5 6 7 8; 9 10 11 12')
#print(a)
#np.random.shuffle(a)

#print(a)