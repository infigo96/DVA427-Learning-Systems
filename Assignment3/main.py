import numpy as np
import os
import time
from sympy import *

popSize = 112 #112 #use multiple of 4 as popSize
numberOfBest = 20
permutationSize = 52 #max 52


def NewPop(sizePop):
    return np.array([np.random.permutation(permutationSize) for i in np.arange(sizePop)])


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
   # print(Individual)
    #print("sak 2 fyt  " + str(Individual[13]))
    lenes = len(np.transpose(Individual))
    #print("sak" + str(Individual))
    #print("lenes " + str(lenes))
    a = np.arange(lenes)
    b = a + 1
    b[lenes - 1] = 0
    return np.sum([DistanceMatrix[Individual[a[i]],Individual[b[i]]] for i in np.arange(lenes)])

def tournament(DistanceMatrix, Population):
    order = np.array([np.random.permutation(popSize) for i in np.arange(1)])
    for i in range(0, len(Population), 4):
        #parents = returnBest(Population[i:i+4,:], DistanceMatrix, 2)
        #Population[i:i+2,:] = crossover(DistanceMatrix, parents)[0:2,:]
        #Population[i + 2:i + 4, :] = NewPop(2)
        #Population[i+2:i+4,:] = crossover(DistanceMatrix, parents)[0:2,:]

        parents = returnBest(Population[order[0, i:i + 4], :], DistanceMatrix, 2)
        Population[order[0, i:i + 2], :] = crossover(DistanceMatrix, parents)[0:2, :]
        Population[order[0, i + 2:i + 4], :] = crossover(DistanceMatrix, parents)[0:2, :]

    return Population

    #how to split into groups of 4 each?


def crossover(DistanceMatrix, parents):

    #parents = returnBest(Population, DistanceMatrix, 2)
    #print(parents)
    #-------- crossover, take out a few from the one and put them in the other
    amount = np.int_(np.ceil(((len(parents[1])-1)/2)* np.random.random_sample() + 2))
    position = np.int_(np.ceil((len(parents[1])-1-amount)* np.random.random_sample() + 1))
    #------take out a part
    toSwitch1 = parents[0,position:position + amount]
    toSwitch2 = parents[1,position:position + amount]
    #-----take out everything but the switch from the oppsite parent
    Cut1 = parents[0,~np.in1d(parents[0], toSwitch2)]
    Cut2 = parents[1,~np.in1d(parents[1], toSwitch1)]
    #----combine the switch with the remaining to create two children
    child1 = np.insert(Cut2, position, toSwitch1)
    child2 = np.insert(Cut1, position, toSwitch2)

    return np.vstack((chernobyl(child1), chernobyl(child2)))
# return

def chernobyl(individual):
    toMutate = individual.ravel()
    if np.random.random_sample() > 0.7:
        rand1 = np.int_(np.ceil((permutationSize-1)*np.random.random_sample()))
        rand2 = np.int_(np.ceil((permutationSize-1)*np.random.random_sample()))
        temp = toMutate[rand1]
        toMutate[rand1] = toMutate[rand2]
        toMutate[rand2] = temp
    return toMutate


            #select 2 random values


#np.random.seed(42)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
data = np.genfromtxt('./berlin.txt', delimiter=',')
distanceMatrix= np.array([[Distance(i, j) for i in data] for j in data])
####################################
oldPop = NewPop(popSize)
print(routeDistance(distanceMatrix, returnBest(oldPop, distanceMatrix, 1).ravel()))
oldBestD = np.inf
lastPlace = 0;
for i in range(0,1000):

    #np.random.shuffle(oldPop)
    newPop = tournament(distanceMatrix, oldPop) #needs to be shuffled at some point
    # elitism, remove x number of worst from population
    best = returnBest(newPop, distanceMatrix, 1)
    bestDist = routeDistance(distanceMatrix,best.ravel())
    if (bestDist <= oldBestD):
        oldBestD = bestDist
        oldBest = best
    else:
        place = np.int_(np.ceil((permutationSize) * np.random.random_sample() + 1))
        newPop[place] = oldBest

    print(oldBestD)
    #newPop = np.vstack([newPop, returnBest(oldPop, distanceMatrix, numberOfBest)])
    #oldPop = killWeak(newPop, distanceMatrix, numberOfBest) # we kill off the weakest
    oldPop = newPop
    #print(routeDistance(distanceMatrix, returnBest(oldPop, distanceMatrix, 1).ravel()))
print(routeDistance(distanceMatrix, returnBest(oldPop, distanceMatrix, 1).ravel()))
print(oldBest)
#end loop

