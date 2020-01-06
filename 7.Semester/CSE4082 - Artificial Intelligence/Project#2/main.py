import numpy as np  
from random import randrange,uniform

def generateRandomPop(popSize,numberOfNodes):
    populationArray=[]
    for i in range(0,popSize):
        stringI=[]
        for j in range(0,numberOfNodes):
            rand=uniform(0,1)
            if(rand<0.5):
                stringI.append(0)
            else:
                stringI.append(1)
        populationArray.append(stringI)
    return populationArray

def repair(populationArray):
    return populationArray

def matchingPoolTournement(populationArray,weightArray):
    popSize=len(populationArray)
    matchingArray=[]
    for i in range(0,popSize):
        oldfitness=100000000
        winner=0
        for j in range(0,10):
            rand=randrange(0,popSize)
            fitness=0
            for k in range(0,len(populationArray[rand])):
                fitness+=populationArray[rand][k]*weightArray[k]        
            if oldfitness>fitness:
                oldfitness=fitness
                winner=rand
        matchingArray.append(populationArray[winner])        
    return matchingArray

def crossover(matchingArray,crossoverProb,numberOfNodes):
    popSize=len(matchingArray)
    crossoverredArray=[]
    i=-1
    for j in range(0,popSize):
        i+=2
        rand=uniform(0,1)
        if(rand<crossoverProb):
            rand2=randrange(0,numberOfNodes)
            child1=matchingArray[i-1][:rand2] + matchingArray[i][rand2:]
            child2=matchingArray[i][:rand2] + matchingArray[i-1][rand2:]
            crossoverredArray.append(child1)
            crossoverredArray.append(child2)
        else:
            crossoverredArray.append(matchingArray[i-1])
            crossoverredArray.append(matchingArray[i])
        if(i==popSize-1):
            break
    return crossoverredArray

def mutateAndBestfit(crossoverredArray,mutationProb,numberOfNodes,weightArray):
    popSize=len(crossoverredArray)
    bestfitness=10000000
    for i in range(0,popSize):
        fitness=0
        for j in range(0,numberOfNodes):
            rand=uniform(0,1)
            if(rand<mutationProb):
               crossoverredArray[i][j]=1-crossoverredArray[i][j]
            fitness+=crossoverredArray[i][j]*weightArray[j]
        if(bestfitness>fitness):
            bestfitness=fitness
    return crossoverredArray,bestfitness


    
    
fileName="003.txt"
numberOfGen=100
numberOfPop=100
crossoverProb=0.5
mutationProb=0.05

i=0
numberOfNodes=0
numberOfEdges=0
weightArray=[]

with open(fileName,'r') as f:
  x=f.readlines()
  for line in x:
      i+=1
      if(i==1):
        numberOfNodes = int(line) 
      elif(i==2):
        numberOfEdges= float(line)
        break
print(numberOfNodes,numberOfEdges)

i=0
adjacencyMatrix=np.zeros((numberOfNodes,numberOfNodes))
with open(fileName,'r') as f:
  x=f.readlines()
  for line in x:
    i+=1
    if(i>2 and i<=numberOfNodes+2):
      n=line.split(' ')
      weightArray.append(float((n[1][0]+'.'+n[1][2]+n[1][3])))
    elif(i>2 and i>numberOfNodes+2):
      n=line.split(' ')
      adjacencyMatrix[int(n[0])][int(n[1])]=1

populationArray=generateRandomPop(numberOfPop,numberOfNodes)
populationArray=repair(populationArray)
i=0
while(i!=numberOfGen):
    i+=1
    matchingArray=matchingPoolTournement(populationArray,weightArray)
    crosseverredArray=crossover(matchingArray,crossoverProb,numberOfNodes)
    mutationedArray,bestfitness=mutateAndBestfit(crosseverredArray,mutationProb,numberOfNodes,weightArray)
    populationArray=repair(mutationedArray)
    print(bestfitness)

