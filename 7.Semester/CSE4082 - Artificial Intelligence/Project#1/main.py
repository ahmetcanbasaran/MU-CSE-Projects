#############################################
#                                           #
#     CSE4082 - Artificial Intelligence     #
#                Project #1                 #
#       Oguzhan BOLUKBAS - 150114022        #
#                                           #
#############################################


class Node:
  def __init__(self, parent, position, depth=0):
    self.parent = parent  # To keep parent node
    self.position = position  # To keep position of pegs
    self.depth = depth  # To keep depth of node. It is fore IDS


walls = []  # To store walls between squares
squares = []  # To store squares of maze
maze_length = -1

cost_of_solution = -1
solution_path = []
expanded_nodes = []  # To keep how many node expanded
visited_squares = []

current_position = None
goal_positions = []
trap_positions = []


def read_squares(path):
  global maze_length
  fp = open(path, "r")
  for cnt, line in enumerate(fp):  # To read file line by line
    char_list = list(line.strip())  # To get rid of "/n"
    squares.append(char_list)
  maze_length = cnt + 1
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
  fp.close()


def find_inital_position():
  r, c = -1, -1
  for row in squares:
    r += 1
    c = -1
    for letter in row:
      c += 1
      if letter == "S":
        return [r, c]


def find_goal_position():
  r, c = -1, -1
  for row in squares:
    r += 1
    c = -1
    for letter in row:
      c += 1
      if letter == "G":
        goal_positions.append([r, c])


def find_trap_position():
  r, c = -1, -1
  for row in squares:
    r += 1
    c = -1
    for letter in row:
      c += 1
      if letter == "T":
        trap_positions.append([r, c])


def agent_mov(x, y, maze):  # To find all possible movements of an agent in current position
  pass


# To find possible squares the agent can move
def possible_positions(position):
  pos_moves = []
  x, y = position[0], position[1]  # Current coordinates

  if position[0] != 0:  # NORTH
    if walls[x][y][3] == "O":
      pos_moves.append([position[0] - 1, position[1]])

  if position[1] != 0:  # WEST
    if walls[x][y][2] == "O":
      pos_moves.append([position[0], position[1] - 1])

  if position[0] != maze_length - 1:  # SOUTH
    if walls[x][y][1] == "O":
      pos_moves.append([position[0] + 1, position[1]])

  if position[1] != maze_length - 1:  # EAST
    if walls[x][y][0] == "O":
      pos_moves.append([position[0], position[1] + 1])

  return pos_moves


def is_visited(position):
  global visited_squares
  for pos in visited_squares:
    if pos[0] == position[0] and pos[1] == position[1]:
      return True
  return False


def is_goal(position):
  global goal_positions
  for pos in goal_positions:
    if pos[0] == position[0] and pos[1] == position[1]:
      return True
  return False


def is_trap(position):
  global trap_positions
  for pos in trap_positions:
    if pos[0] == position[0] and pos[1] == position[1]:
      return True
  return False


def find_solution_path(node):
  global solution_path, cost_of_solution
  while node:
    if is_trap(node.position): cost_of_solution += 7
    else: cost_of_solution += 1
    solution_path.append(node.position)
    node = node.parent
  solution_path.reverse()

def dfs():
  global current_position, cost_of_solution, visited_squares
  current_position = find_inital_position()
  frontier = []  # Stack for DFS. Use append() and pop()
  initial_node = Node(None, current_position, 0)
  frontier.append(initial_node)

  while True:
    if not frontier:
      print("Frontier is empty. There is no solution")
      return None

    parent = frontier.pop()
    expanded_nodes.append(parent.position)

    if is_goal(parent.position):
      find_solution_path(parent)
      return

    visited_squares.append(parent.position)
    p_positions = possible_positions(parent.position)

    for position in p_positions:
      if not is_visited(position):
        child = Node(parent, position, parent.depth + 1)
        frontier.append(child)


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
  find_goal_position()
  find_trap_position()

  # WARNING: Order of node expansion should be East, South, West, North
  dfs()
  print("The cost of the solution: \n", cost_of_solution, "\n")
  print("The solution path is: \n", solution_path, "\n")
  print("Expanded nodes are: \n", expanded_nodes, "\n")

  """
  print("a. Depth First Search\nb. Breadth First Search\nc. Iterative Deepening Search\nd. Depth First Search with Random Selection\ne. Depth First Search with a Node Selection Heuristic")

  method = input("Choose a search method: ")
  if (method == 'a'):
    print("\nSearch method is: Depth First Search")
    dfs()

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
  """


if __name__ == '__main__':
  main()
