import numpy as np
import os
import time
from sympy import *

popSize = 40 #use multiple of 4 as popSize
numberOfBest = 2


def NewPop(sizePop):
    return np.array([np.random.permutation(52) for i in np.arange(sizePop)])


def Distance(a, b):
    return sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
# sqrt((Y-Y0)^2+(X-X0)^2)

def killWeak(Pop, DistanceMatrix, numberWeak): #ej testad
    #numberweak < Pop
    #Rremember that elitism must keep the number of numberWeak
    return returnBest(Pop, DistanceMatrix, len(Pop)-numberWeak)

def returnBest(Pop, DistanceMatrix, numberOfBest):
    return np.array(sorted(list(Pop), key=lambda x: routeDistance(DistanceMatrix, x))[:numberOfBest])


def routeDistance(DistanceMatrix, Individual):
    #print("sak 2 fyt  " + str(Individual[13]))
    lenes = len(np.transpose(Individual))
    #print("sak" + str(Individual))
    #print("lenes " + str(lenes))
    a = np.arange(lenes)
    b = a + 1
    b[lenes - 1] = 0
    return np.sum([DistanceMatrix[Individual[a[i]]][Individual[b[i]]] for i in np.arange(lenes)])

def tournament(DistanceMatrix, Population):
    print(Population[3][:])
    for i in range(0, len(Population), 4):
        print(i)
        Population[i:i+3,:] = crossover(DistanceMatrix, Population[i:i+3,:])
    return Population

    #how to split into groups of 4 each?


def crossover(DistanceMatrix, Population):
    parents = returnBest(Population, DistanceMatrix, 4)
    #DO CROSSOVERSHIT
    children = parents # should not work, only 2 elements
    return parents
# return

#def mutate........



#np.random.seed(42)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
data = np.genfromtxt('./berlin.txt', delimiter=',')
distanceMatrix= [[Distance(i, j) for i in data] for j in data]
#print(distanceMatrix)
#test = routeDistance(distanceMatrix, (NewPop(1)))
#print(hej)
####################################
#generate population
oldPop = NewPop(popSize)
#loop start

#Good place for plotting graphics here

#check if to stop
#if routeDistance(DistanceMatrix, returnBest(Pop, DistanceMatrix, 1)) < *GOOD DISTANCE*

#tournament:
#select from population of groups of 4
#from this group save the best 2, then cross them
#mutate children
#after this we will have  nextPop which is the children of the old Population
newPop = tournament(distanceMatrix, oldPop) #needs to be shuffled at some point

# elitism, remove x number of worst from population
#Population = newPop + returnBest(Pop, distanceMatrix, numberOfBest) # we add some of the old pop
#print(returnBest(oldPop, distanceMatrix, numberOfBest))
#print(newPop)
newPop = np.vstack([newPop, returnBest(oldPop, distanceMatrix, numberOfBest)])
oldPop = killWeak(newPop, distanceMatrix, numberOfBest) # we kill off the weakest

#end loop


#####################################


#Pop = NewPop(1)
#print(Pop)

#a = np.matrix('1 2 3 4; 5 6 7 8; 9 10 11 12')
#print(a)
#np.random.shuffle(a)

#print(a)