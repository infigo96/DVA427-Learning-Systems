import numpy as np
import math
from sympy import *

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

data = np.genfromtxt('assignment 1 titanic.dat', delimiter=',')
print(data)
#data[1,:] get first row

print(sigmoid(1))