import numpy as np
from sympy import *



row1 = np.array([-1,-1,1])
row2 = np.array([ 1, 0, 1])
row3 = np.array([0, 1, 1])

a = np.matrix([row1,row2,row3])
print(a)
row1 = np.array([ -1, -1, 1])
row2 = np.array([ 1, -1, 1])
row3 = np.array([0, 2, 1])
b = np.matrix([row1,row2,row3])
print(b)

row1 = np.array([ -1/sqrt(2), 1/sqrt(2), 0])
row2 = np.array([ 0, 1/sqrt(6), 0])
row3 = np.array([0, 0, 1/sqrt(3)])
fix = np.matrix([row1,row2,row3])


print("\n This is c:")
print(b)


test = b*a
print("\n This is test:")
print(test)


data = np.genfromtxt('assignment 1 titanic.dat', delimiter=',')
print(data)
