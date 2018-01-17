import numpy as np
import math
from sympy import *


np.random.seed(1)
weights = 2* np.random.random_sample((1, 4)) - 1
print(weights)

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

data = np.genfromtxt('assignment 1 titanic.dat', delimiter=',')
#np.c_[ da, np.ones(N) ]
print(data)
#data[1,:] get first row
for i in range(0,1):
#O0 = sigmoid(data[0,0]*weights[0,0]+data[0,1]*weights[0,1]+data[0,2]*weights[0,2]+ weights[0,3])
    o1 = sigmoid(np.dot(weights[0,0:3],data[i,0:3]) + weights[0,3])
    delta = o1*(1-o1)*(0.5 + 0.25*data[i,3]-o1)
    print("Fucktard  " + str(o1))
    print("Deltatard  " + str(delta))

    #for j in range (0,4):
    weights =[0.05*delta*data[i,0:3],0.05*delta]
    print(weights)

