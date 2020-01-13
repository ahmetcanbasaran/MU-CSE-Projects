from random import randrange, uniform, sample, randint
import matplotlib.pyplot as plt
import numpy as np

# To keep argument values
file_name = None
number_of_gen = 0
number_of_pop = 0
crossover_prob = 0.0
mutation_prob = 0.0

# To keep graph information
number_of_nodes = 0  # To keep number of nodes
number_of_edges = 0  # To keep number of edges
weight_array = []  # To keep weight values of vertices
adjacency_matrix = None  # To fill adjacency matrix with zeros
average_fit_values = None
fitness_values = None


def is_any_edge(edges):
  for i in range(0, number_of_nodes):
    for j in range(0, number_of_nodes):
      if edges[i][j] == 1:
        return True
  return False


def delete_edges(edges, u):
  deleted = False
  for i in range(0, number_of_nodes):
    if edges[u][i] == 1:
      edges[u][i] = 0
      deleted = True
    if edges[i][u] == 1:
      edges[i][u] = 0
      deleted = True
  return deleted


def generate_random_pop():
  global average_fit_values, fitness_values
  population = np.zeros((number_of_pop, number_of_nodes), dtype=int)
  fit_value = 0
  for i in range(0, number_of_pop):  # To keep offspring number in population
    edges = adjacency_matrix.copy()
    rnd_nodes = sample(range(0, number_of_nodes), number_of_nodes)
    k = 0
    while is_any_edge(edges):  # To check edges if there is any uncovered
      node = rnd_nodes[k]  # To generate a random node
      k += 1
      is_deleted = delete_edges(edges, node)
      if is_deleted:
          population[i][node] = 1
    offspring_fitness = 0
    for m in range(0, number_of_nodes):  # To calculate fitness of the offspring
      offspring_fitness += population[i][m] * weight_array[m]
    fitness_values[i] = offspring_fitness  # To save fitness value of the spring
    fit_value += offspring_fitness
  average_fit_values = [fit_value / number_of_pop]  # To calculate average fit
  return population


def repair(population):
  global fitness_values
  fit_value = 0
  for i in range(0, number_of_pop):  # To process each offspring
    edges = adjacency_matrix.copy()
    for j in range(0, number_of_nodes):  # To check each node one by one
      delete_edges(edges, population[i][j])  # To delete it this node exist in population
    j = 0
    rnd_nodes = sample(range(0, number_of_nodes), number_of_nodes)
    while is_any_edge(edges):  # To check edges if there is any uncovered
      node = rnd_nodes[j]  # To generate a random node
      j += 1
      is_deleted = delete_edges(edges, node)
      if is_deleted:
        population[i][node] = 1
    offspring_fitness = 0
    for m in range(0, number_of_nodes):  # To calculate fitness of the offspring
      offspring_fitness += population[i][m] * weight_array[m]
    fitness_values[i] = offspring_fitness  # To save fitness value of the spring
    fit_value += offspring_fitness
  average_fit = fit_value / number_of_pop  #To calculate average fit
  return average_fit


def mating_pool_tournement(population):
  pop_size = number_of_pop
  mating_pool = []
  for i in range(0, pop_size):  # To iterate until mating pool is filled
    rand1 = randint(0, pop_size-1)
    rand2 = randint(0, pop_size-1)
    while rand2 == rand1:  # To continue until different random numbers obtained
      rand2 = randint(0, pop_size-1)
    if fitness_values[rand1] < fitness_values[rand2]:  # To get lowest cost offspring
      mating_pool.append(population[rand1])
    else:
      mating_pool.append(population[rand2])
  return mating_pool


def crossover(population):
  for i in range(1, number_of_pop+1, 2):
    rand = uniform(0, 1)
    #if random number is smaller than crossover probability make 2 child with 1 point crossover
    if rand < crossover_prob:
      rand2 = randrange(0, number_of_nodes)
      tmp = population[i][:rand2].copy()
      population[i][:rand2], population[i - 1][:rand2] = population[i - 1][:rand2], tmp


def mutate(population):
  for i in range(0, number_of_pop):
    for j in range(0, number_of_nodes):
      #if random number is smaller than mutation probability change the responsible bit as opposite   
      if uniform(0, 1) < mutation_prob:
        population[i][j] = 1 - population[i][j]


def main():
  global file_name, number_of_gen, number_of_pop, crossover_prob, mutation_prob
  global number_of_nodes, number_of_edges, weight_array, adjacency_matrix, fitness_values

  # To get values of variables from the user
  file_name = input("Name of the graph file: ")
  number_of_gen = eval(input("Number of generations: "))
  number_of_pop = eval(input("Population size: "))
  crossover_prob = eval(input("Crossover probability: "))
  mutation_prob = eval(input("Mutation probability: "))
  
  """
  file_name = "003.txt"
  number_of_gen = 10
  number_of_pop = 4
  crossover_prob = 0.9
  mutation_prob = 0.05
  """
  
  i = 0
  # To get information from the input file
  with open("graphs/" + file_name, 'r') as f:
    lines = f.readlines()  # To get all lines from file
    for line in lines:  # To handle input file line by line
      if i == 0:  # Number of nodes is written in the first line
        number_of_nodes = int(line)
        adjacency_matrix = np.zeros((number_of_nodes, number_of_nodes), dtype=int)
      elif i == 1:  # Number of edges is written in the second line
        number_of_edges = int(float(line))
      if 2 <= i < number_of_nodes + 2:  # List of node weights is written in the continuation lines
        n = line.split(' ')  # To get node numbers and their weights seperately
        weight_array.append(float((n[1][0] + '.' + n[1][2] + n[1][3])))  # To add them into the weights list
      elif number_of_nodes + 2 <= i:
        n = line.split(' ')  # To get node numbers and their adjancent nodes seperately
        adjacency_matrix[int(n[0])][int(n[1])] = 1  # To assign contiguity of nodes with putting 1 into the adj. matrix
      i += 1

  fitness_values = np.zeros((number_of_pop, 1))  # To store fitness values
  population = generate_random_pop()  # To produce the first population randommly

  i = 0
  while i != number_of_gen:
    population = mating_pool_tournement(population)    # To form a mating pool with possible parents
    crossover(population)   # To crossover for parents that give child
    mutate(population)     # To mutate some bits in childs
    average_fit = repair(population)    # To repair it and get average fit value
    average_fit_values.append(average_fit)
    i += 1
    print("Generation", i , "is finished")

  print(average_fit_values)

  generation = []
  for i in range(0,len(average_fit_values)):
      generation.append(i)

  plt.plot(generation, average_fit_values)
  plt.xlabel('Generation')
  plt.ylabel('Average Fitness')
  plt.title("File: " + file_name + ", # Generations: " + str(number_of_gen) + ", Pop. Size " + str(number_of_pop) +
            ", Crossover Prob. " + str(crossover_prob) + ", Mutation Prob. " + str(mutation_prob) + ".")
  plt.show()


if __name__ == "__main__":
  main()
