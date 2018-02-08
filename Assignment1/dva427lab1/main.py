import numpy as np
import time
from sympy import *
import os

correct = 0
#np.random.seed(0)
#weights = np.array(4,3)
weights = np.reshape((2* np.random.random_sample((1, 16)) - 1),(4,4))
#print(weights)
#weights = 2* np.random.random_sample((1, 3)) - 1

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
#val = np.zeros((4,701))
#-------------------------------------------------------------------------------------------
Outis = sigmoid(np.matmul(data[1500:2201,0:4],np.transpose(weights[0:3,0:4]))) #2202 did not work
Outis = np.append(Outis, np.ones((len(Outis),1)),axis=1)

val = sigmoid(np.matmul(Outis[0:701,:],np.transpose(weights[3:4,0:4]))) #2202 did not work

for i in range(1500,2201):

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

  Outis = sigmoid(np.matmul(data[:1500, 0:4], np.transpose(weights[0:3, 0:4])))  # 2202 did not work
  Outis = np.append(Outis, np.ones((len(Outis), 1)), axis=1)

  Sogmod = sigmoid(np.matmul(Outis[:1500,:], np.transpose(weights[3:4, 0:4])))  # 2202 did not work

  #Sogmod = sigmoid((data[:1500,0:4]).dot(np.transpose(weights[:,0:4])))
  #current = np.sum(np.abs(0.5 - Sogmod))

  #print("Sogmoid" +str(Sogmod))
  delta = (Sogmod-Sogmod*Sogmod)*np.transpose(0.5 + 0.25*(data[:1500,4])-np.transpose(Sogmod))

  Hdelta = ((Outis-Outis*Outis)*delta*weights[3,:])[:,:3]
  #Mdelta[:,3] = 1
  #Idelta = Mdelta*delta*weights[3,:]


  weights =weights + 0.00005*np.transpose(delta[:1500,:]).dot(data[:1500,0:4])
  sizeDelta = np.linalg.norm(delta)
  #print("weights" + str(weights))

  Outis = sigmoid(np.matmul(data[1500:2201, 0:4], np.transpose(weights[0:3, 0:4])))  # 2202 did not work
  Outis = np.append(Outis, np.ones((len(Outis), 1)), axis=1)
  val = sigmoid(np.matmul(Outis[0:701, :], np.transpose(weights[3:4, 0:4])))  # 2202 did not work
  # for i in range(0, 1500):
  #
  #   if data[i, 4] == 1:
  #
  #     if Sogmod[i] >= 0.5:
  #       correct+=1
  #   else:
  #
  #     if Sogmod[i] < 0.5:
  #       correct+=1
  for i in range(1500,2201):

    if data[i,4] == 1:
      alive +=1
      if val[i - 1500] >= 0.5:
        survivedcorrect+=1
    else:
      death+=1
      if val[i - 1500] < 0.5:
        deathcorrect+=1


  #print(correct)
  print("sizeDelta: " + str(sizeDelta/1500) + "  SC: " + str(survivedcorrect / death) + "  DC: " + str(deathcorrect / death) + "  tot: " + str((survivedcorrect + deathcorrect) / (alive + death)))
  #time.sleep(1)

print('Predicted survival rate is')
print(np.sum(np.abs(val))/700)
print('Real survival rate is')
print(str(1-(1502/2224)))

###############
#print("Alive: " + str(survivedcorrect/death) + "  Dead: " + str(deathcorrect/death) + "  TOT: " + str((survivedcorrect+deathcorrect)/(alive+death)))
#print('Accuracy is: ' + str((survivedcorrect+deathcorrect)/700))
#SurvivalrateFancy = sigmoid((data[23,0:4]).dot(np.transpose(weights[:,0:4])))
#print('SurvivalrateFancy: ')
#print(SurvivalrateFancy)