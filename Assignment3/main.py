import numpy as np
import os
import time
from sympy import *

popSize = 12 #112 #use multiple of 4 as popSize
numberOfBest = 5
permutationSize = 10 #max 52


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
    #print(Population[3][:])
    for i in range(0, len(Population), 4):
        parents = returnBest(Population[i:i+4,:], DistanceMatrix, 2)
        Population[i:i+2,:] = crossover(DistanceMatrix, parents)[0:2,:]
        Population[i+2:i+4,:] = crossover(DistanceMatrix, parents)[0:2,:]

    return Population

    #how to split into groups of 4 each?


def crossover(DistanceMatrix, parents):

    #parents = returnBest(Population, DistanceMatrix, 2)
    #print(parents)
    #-------- crossover, take out a few from the one and put them in the other
    amount = np.int_(np.ceil(((len(parents[1])-1)/3)* np.random.random_sample() + 2))
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

    return np.vstack((child1,child2))
# return

def mutate(population):
    for i  in range(0,len(population)):
        if np.random.random_sample() > 0.8:
            print('hej')
    return population

            #select 2 random values









#np.random.seed(42)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
data = np.genfromtxt('./berlin.txt', delimiter=',')
distanceMatrix= np.array([[Distance(i, j) for i in data] for j in data])
#print(distanceMatrix)
#test = routeDistance(distanceMatrix, (NewPop(1)))
#print(hej)
####################################
#generate population
oldPop = NewPop(popSize)
print(routeDistance(distanceMatrix, returnBest(oldPop, distanceMatrix, 1).ravel()))

for i in range(0,100):
    #loop start #use index to save distance for best in group

    #Good place for plotting graphics here

    #check if to stop
    #if routeDistance(DistanceMatrix, returnBest(Pop, DistanceMatrix, 1)) < *GOOD DISTANCE*

    #tournament:
    #select from population of groups of 4
    #from this group save the best 2, then cross them
    #mutate children
    #after this we will have  nextPop which is the children of the old Population
    #np.random.shuffle(oldPop)
    print(oldPop)
    print('---------------------------------------------------')
    newPop = tournament(distanceMatrix, oldPop) #needs to be shuffled at some point
    # elitism, remove x number of worst from population
    #Population = newPop + returnBest(Pop, distanceMatrix, numberOfBest) # we add some of the old pop
    #print(returnBest(oldPop, distanceMatrix, numberOfBest))
    #print(newPop)
    #newPop = np.vstack([newPop, returnBest(oldPop, distanceMatrix, numberOfBest)])
    #oldPop = killWeak(newPop, distanceMatrix, numberOfBest) # we kill off the weakest
    oldPop = newPop
    print(routeDistance(distanceMatrix, returnBest(oldPop, distanceMatrix, 1).ravel()))
print(routeDistance(distanceMatrix, returnBest(oldPop, distanceMatrix, 1).ravel()))

#end loop


#####################################


#Pop = NewPop(1)
#print(Pop)

#a = np.matrix('1 2 3 4; 5 6 7 8; 9 10 11 12')
#print(a)
#np.random.shuffle(a)

#print(a)