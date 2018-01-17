import numpy as np
import math
from sympy import *

correct = 0
np.random.seed(1)
weights = 2* np.random.random_sample((1, 4)) - 1
print(weights)

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

data = np.genfromtxt('assignment 1 titanic.dat', delimiter=',')
data = np.c_[ data, np.ones(len(data))]
data[:,4] = data[:,3]
data[:,3] = 1
print(data)
#data[1,:] get first row
for i in range(0,1500):
    o1 = sigmoid(np.dot(weights[0,0:4],data[i,0:4]))
    delta = o1*(1-o1)*(0.5 + 0.25*data[i,4]-o1)

    #for j in range (0,4):
    weights =weights + 0.05*delta*data[i,0:4]
    print(i)
print("Fucktard  " + str(o1))
print("Deltatard  " + str(delta))
print(weights)



for i in range(1500,2200):
    val1 = sigmoid(np.dot(weights[0, 0:4], (data[i, 0:4])))
    if val1 >= 0.5 and data[i,4] == 1:
        correct+=1
    elif val1 < 0.5 and data[i, 4] == -1:
        correct+=1
    #print(val1)
    #for j in range (0,4):

print(correct)
print(correct/700)

