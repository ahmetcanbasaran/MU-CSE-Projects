import numpy as np
from random import randrange, uniform

def generate_random_pop(pop_size, number_of_nodes):
  population_array = []
  for i in range(0, pop_size):
    string_i = []
    for j in range(0, number_of_nodes):
      rand = uniform(0, 1)
      if(rand<0.5):
        string_i.append(0)
      else:
        string_i.append(1)
    population_array.append(string_i)
  return population_array

def repair(population_array):
  return population_array

def matching_pool_tournement(population_array, weight_array):
  pop_size = len(population_array)
  matching_array = []
  for i in range(0, pop_size):
    oldfitness = 100000000
    winner = 0
    for j in range(0, 10):
      rand = randrange(0, pop_size)
      fitness = 0
      for k in range(0, len(population_array[rand])):
        fitness += population_array[rand][k]*weight_array[k]
      if oldfitness>fitness:
        oldfitness = fitness
        winner = rand
    matching_array.append(population_array[winner])
  return matching_array

def crossover(matching_array, crossover_prob, number_of_nodes):
  pop_size = len(matching_array)
  crossoverred_array = []
  i = -1
  for j in range(0, pop_size):
    i += 2
    rand = uniform(0, 1)
    if rand<crossover_prob:
      rand2 = randrange(0, number_of_nodes)
      child1 = matching_array[i-1][:rand2] + matching_array[i][rand2:]
      child2 = matching_array[i][:rand2] + matching_array[i-1][rand2:]
      crossoverred_array.append(child1)
      crossoverred_array.append(child2)
    else:
      crossoverred_array.append(matching_array[i-1])
      crossoverred_array.append(matching_array[i])
    if i == pop_size-1:
      break
  return crossoverred_array

def mutate_and_best_fit(crossoverred_array, mutation_prob, number_of_nodes, weight_array):
  pop_size = len(crossoverred_array)
  best_fitness = 10000000
  for i in range(0, pop_size):
    fitness = 0
    for j in range(0, number_of_nodes):
      rand = uniform(0, 1)
      if rand<mutation_prob:
        crossoverred_array[i][j] = 1-crossoverred_array[i][j]
      fitness += crossoverred_array[i][j]*weight_array[j]
    if best_fitness>fitness:
      best_fitness = fitness
  return crossoverred_array, best_fitness

"""
# To get values of variables from the user
file_name = input("Name of the graph file: ")
number_of_gen = eval(input("Number of generations: "))
number_of_pop = eval(input("Population size: "))
crossover_prob = eval(input("Crossover probability: "))
mutation_prob = eval(input("Mutation probability: "))
"""

file_name = "003.txt"
number_of_gen = 100
number_of_pop = 100
crossover_prob = 0.5
mutation_prob = 0.05

i = 0
number_of_nodes = 0  # To keep number of nodes
number_of_edges = 0  # To keep number of edges
weight_array = []  # To keep weight values of vertices
adjacency_matrix = None  # To fill adjacency matrix with zeros

# To get information from the input file
with open("graphs/" + file_name, 'r') as f:
  lines = f.readlines()  # To get all lines from file
  for line in lines:  # To handle input file line by line
    if i == 0:  # Number of nodes is written in the first line
      number_of_nodes = int(line)
      adjacency_matrix = np.zeros((number_of_nodes, number_of_nodes))
    elif i == 1:  # Number of edges is written in the second line
      number_of_edges = int(float(line))
    if 2 <=  i < number_of_nodes+2: # List of node weights is written in the continuation lines
      n = line.split(' ')  # To get node numbers and their weights seperately
      weight_array.append(float((n[1][0]+'.'+n[1][2]+n[1][3])))  # To add them into the weights list
    elif number_of_nodes+2 <= i:
      n = line.split(' ')  # To get node numbers and their adjancent nodes seperately
      adjacency_matrix[int(n[0])][int(n[1])] = 1  # To assign contiguity of nodes with putting 1 into the adj. matrix
    i +=  1

population_array = generate_random_pop(number_of_pop, number_of_nodes)
population_array = repair(population_array)

i = 0
while i !=  number_of_gen:
  matching_array = matching_pool_tournement(population_array, weight_array)
  crosseverred_array = crossover(matching_array, crossover_prob, number_of_nodes)
  mutationed_array, best_fitness = mutate_and_best_fit(crosseverred_array, mutation_prob, number_of_nodes, weight_array)
  population_array = repair(mutationed_array)
  print(best_fitness)
  i +=  1
