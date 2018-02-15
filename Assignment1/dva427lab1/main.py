import numpy as np
import time
from sympy import *
import os

correct = 0
#np.random.seed(0)
#weights = np.array(4,3)
weights = np.reshape((2* np.random.random_sample((1, 16)) - 1),(4,4)) #
#print(weights)
#weights = 2* np.random.random_sample((1, 3)) - 1

#print(weights)

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
data = np.genfromtxt('./assignment 1 titanic.dat', delimiter=',')
data = np.c_[ data, np.ones(len(data))] #add a column on the fourth row
data[:,4] = data[:,3] #put label on the 4th position
data[:,3] = 1 #fill with ones on 3rd position
#val = np.zeros((4,701))
#------------------------------------------------------------------------------------------- First validation to see how system is in the start
Outis = sigmoid(np.matmul(data[1500:2201,0:4],np.transpose(weights[0:3,0:4]))) #input -> hidden layer weighst, sets the data in each matrix which will be multiplied with the weights
Outis = np.append(Outis, np.ones((len(Outis),1)),axis=1) # add bias a 1 will be multiplied with the weights for the node bias thus we need a bias of 1

val = sigmoid(np.matmul(Outis[0:701,:],np.transpose(weights[3:4,0:4]))) #From hidden layer -> output weights.

for i in range(1500,2201):

  if val[i-1500] >= 0.5 and data[i,4] == 1:
    correct+=1
  elif val[i-1500] < 0.5 and data[i, 4] == -1:
    correct+=1


  #print(correct)
print(correct/701)
time.sleep(2)
#-------------------------------------------------------------------------------------------- Now starts real training


for j in range(0,1000):
  correct = 0 # initalize correct
  alive = 0
  death = 0
  deathcorrect = 0
  survivedcorrect = 0

  Outis = sigmoid(np.matmul(data[:1500, 0:4], np.transpose(weights[0:3, 0:4])))  #input -> hidden layer weights, sets the data in each matrix which will be multiplied with the weights 1500x4 * 4x3 =1500x3
  Outis = np.append(Outis, np.ones((len(Outis), 1)), axis=1) # add bias a 1 will be multiplied with the weights for the node bias thus we need a bias of 1. Output of hidden layer.

  Sogmod = sigmoid(np.matmul(Outis[:1500,:], np.transpose(weights[3:4, 0:4])))  # 3:4 is to pick the 3rd element. This is the output layers, output of output layer. 1500x4 * 4x1 = 1500x1

  delta = (Sogmod-Sogmod*Sogmod)*np.transpose(0.5 + 0.25*(data[:1500,4])-np.transpose(Sogmod)) #Single value, is the delta for the output sigmod node

  Hdelta = ((Outis-Outis*Outis)*delta*weights[3,:])[:,:3] #3x1  vector, delta for the 3 hidden layer  sigmod nodes
  delta = np.append(Hdelta,delta,axis=1) #add together deltas to one matrix



  weights = weights + 0.0005*np.transpose(delta[:1500,:]).dot(data[:1500,0:4]) #calculates all new weights from delta
  #print("weights" + str(weights))

  # ---------------------------------------here we evaluate the data on the validation data to see the progress of the training. Not linked to the actual training.
  Outis = sigmoid(np.matmul(data[1500:2201, 0:4], np.transpose(weights[0:3, 0:4])))  #input -> hidden layer weights, sets the data in each matrix which will be multiplied with the weights
  Outis = np.append(Outis, np.ones((len(Outis), 1)), axis=1) # add bias a 1 will be multiplied with the weights for the node bias thus we need a bias of 1. Output of hidden layer.
  val = sigmoid(np.matmul(Outis[0:701, :], np.transpose(weights[3:4, 0:4])))  #output layer of the validation data
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
  correct = 0
  for i in range(1500,2201):

    if data[i,4] == 1:
      alive +=1
      if val[i - 1500] >= 0.5:
        survivedcorrect+=1
        correct+=1
    else:
      death+=1
      if val[i - 1500] < 0.5:
        deathcorrect+=1
      else:
        correct+=1


  #print(correct)
  print(" SC: " + str(survivedcorrect / alive) + "  DC: " + str(deathcorrect / death) + "  tot: " + str((survivedcorrect + deathcorrect) / (alive + death)))
  #time.sleep(1)

print('Predicted survival rate is')
print(correct/700)
print('Real survival rate is')
print(str(1-(1502/2224)))
###############
#print("Alive: " + str(survivedcorrect/death) + "  Dead: " + str(deathcorrect/death) + "  TOT: " + str((survivedcorrect+deathcorrect)/(alive+death)))
#print('Accuracy is: ' + str((survivedcorrect+deathcorrect)/700))
#SurvivalrateFancy = sigmoid((data[23,0:4]).dot(np.transpose(weights[:,0:4])))
#print('SurvivalrateFancy: ')
#print(SurvivalrateFancy)