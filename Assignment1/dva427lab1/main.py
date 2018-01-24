import numpy as np
import time
from sympy import *
import os

correct = 0
#np.random.seed(0)
weights = 2* np.random.random_sample((1, 4)) - 1
#print(weights)

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
data = np.genfromtxt('./assignment 1 titanic.dat', delimiter=',')
data = np.c_[ data, np.ones(len(data))]
data[:,4] = data[:,3]
data[:,3] = 1

#-------------------------------------------------------------------------------------------
val = sigmoid(np.matmul(data[1500:2201,0:4],np.transpose(weights[:,0:4]))) #2201 did not work
  #print(val)
for i in range(1500,2200):

  #val = sigmoid(np.dot(weights[0, 0:4], (data[i, 0:4])))
  if val[i-1500] >= 0.5 and data[i,4] == 1:
    correct+=1
  elif val[i-1500] < 0.5 and data[i, 4] == -1:
    correct+=1


  #print(correct)
print(correct/700)
time.sleep(2)
#--------------------------------------------------------------------------------------------


for j in range(0,1000):
  correct = 0 # initalize correct
  alive = 0
  death = 0
  deathcorrect = 0
  survivedcorrect = 0


  Sogmod = sigmoid((data[:1500,0:4]).dot(np.transpose(weights[:,0:4])))
  #print("Sogmoid" +str(Sogmod))
  delta = (Sogmod*(1-Sogmod))*np.transpose(0.5 + 0.25*(data[:1500,4])-np.transpose(Sogmod))
  #print("delta" + str(delta))

  weights =weights + 0.00005*np.transpose(delta[:1500,:]).dot(data[:1500,0:4])
  #print("weights" + str(weights))
  #print(weights)


  val = sigmoid(np.matmul(data[1500:2201,0:4],np.transpose(weights[:,0:4]))) #2201 did not work
  #print(val)
  for i in range(0, 1500):

    if data[i, 4] == 1:

      if Sogmod[i] >= 0.5:
        correct+=1
    else:

      if Sogmod[i] < 0.5:
        correct+=1
  for i in range(1500,2200):

    if data[i,4] == 1:
      alive +=1
      if val[i - 1500] >= 0.5:
        survivedcorrect+=1
    else:
      death+=1
      if val[i - 1500] < 0.5:
        deathcorrect+=1


  #print(correct)
  print("ERR: " + str((1500-correct)/1500)+ "  SC: " + str(survivedcorrect / death) + "  DC: " + str(deathcorrect / death) + "  tot: " + str((survivedcorrect + deathcorrect) / (alive + death)))
  #time.sleep(1)

###############
#print("Alive: " + str(survivedcorrect/death) + "  Dead: " + str(deathcorrect/death) + "  TOT: " + str((survivedcorrect+deathcorrect)/(alive+death)))
#print('Accuracy is: ' + str((survivedcorrect+deathcorrect)/700))
#SurvivalrateFancy = sigmoid((data[23,0:4]).dot(np.transpose(weights[:,0:4])))
#print('SurvivalrateFancy: ')
#print(SurvivalrateFancy)