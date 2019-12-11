#############################################
#                                           #
#     CSE4082 - Artificial Intelligence     #
#                Project #1                 #
#       Oguzhan BOLUKBAS - 150114022        #
#                                           #
#############################################
from copy import deepcopy


class Node:
  def __init__(self, parent, state, depth=0):
    self.state = state  # To keep position of pegs
    self.parent = parent  # To keep parent node
    self.depth = depth  # To keep depth of node. It is fore IDS

walls = []  # To store walls between squares
squares = []  # To store squares of maze
initial_state = []

cost_of_solution = 0
solution_path = None
expanded_nodes = None  # To keep how many node expanded



def read_squares(path):
  fp = open(path, "r")

  for cnt, line in enumerate(fp):  # To read file line by line
    char_list = list(line.strip())  # To get rid of "/n"
    squares.append(char_list)

  fp.close()


def read_walls(path):
  fp = open(path, "r")

  for cnt, line in enumerate(fp):  # To read file line by line
    line = line.strip()  # To get rid of "/n"
    block_lines = line.split("-")
    line_block_list = []

    for blocks in block_lines:
      square_block_list = [blocks[0], blocks[2], blocks[4], blocks[6]]
      line_block_list.append(square_block_list)

    walls.append(line_block_list)

  print(walls[0][0])
  fp.close()


# TODO: Depth First Search
def dfs():
  pass


# TODO: Breadth First Search
def bfs():
  pass


# TODO: Iterative Deepening
def ids():
  pass


# TODO: Uniform Cost Search
def ucs():
  pass


# TODO: Greedy Best First Search
def gbfs():
  pass

# TODO: A* Heuristic Search
def ashs():
  pass


def main():
  input_squares_path = "./inputs/maze_1/squares.txt"
  input_walls_path = "./inputs/maze_1/walls.txt"
  read_squares(input_squares_path)
  read_walls(input_walls_path)

  # WARNING: Order of node expansion should be East, South, West, North
  dfs()
  bfs()
  ids()
  ucs()
  gbfs()
  ashs()


if __name__ == '__main__':
  print("a. Depth First Search\nb. Breadth First Search\nc. Iterative Deepening Search\nd. Depth First Search with Random Selection\ne. Depth First Search with a Node Selection Heuristic")
  method = input("Choose a search method: ")
  if (method == 'a'):
    print("\nSearch method is: Depth First Search")
    node = dfs()

  elif (method == 'b'):
    print("\nSearch method is: Breadth First Search")
    node = bfs()

  elif (method == 'c'):
    print("\nSearch method is: Iterative Deepening Search")
    node = ids()

  elif (method == 'd'):
    print("\nSearch method is: Uniform Cost Search")
    node = ucs()

  elif (method == 'r'):
    print("\nSearch method is: Greedy Best First Search")
    node = gbfs()

  elif (method == 'f'):
    print("\nSearch method is: A* Heuristic Search")
    node = ashs()
