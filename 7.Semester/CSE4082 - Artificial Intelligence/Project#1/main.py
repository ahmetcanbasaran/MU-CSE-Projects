#############################################
#                                           #
#     CSE4082 - Artificial Intelligence     #
#                Project #1                 #
#       Oguzhan BOLUKBAS - 150114022        #
#                                           #
#############################################
import queue


class Node:
  def __init__(self, parent, position, depth=0, cost=0):
    self.parent = parent  # To keep parent node
    self.position = position  # To keep position of pegs
    self.depth = depth  # To keep depth of node. It is fore IDS
    self.cost = cost


walls = []  # To store walls between squares
squares = []  # To store squares of maze
goal_positions = []  # To keep positions of "G" letter squares
trap_positions = []  # To keep positions of "T" letter squares
current_position = None  # To keep current position coordinates of agent
maze_length = -1  # To keep row or column length of the maze

cost_of_solution = -1
solution_path = []  # To keep solution path
expanded_nodes = []  # To keep expanded nodes
visited_squares = []  # To keep visited squares


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


def find_square_features():
  global current_position
  r, c = -1, -1
  for row in squares:
    r += 1
    c = -1
    for letter in row:
      c += 1
      if letter == "S":
        current_position = [r, c]
      elif letter == "G":
        goal_positions.append([r, c])
      elif letter == "T":
        trap_positions.append([r, c])


def reset_variables():
  global current_position, cost_of_solution, solution_path, expanded_nodes, visited_squares
  current_position = None  # To keep current position coordinates of agent
  cost_of_solution = -1
  solution_path = []  # To keep solution path
  expanded_nodes = []  # To keep expanded nodes
  visited_squares = []  # To keep visited squares


# To find possible squares the agent can move
def possible_positions(position):
  pos_moves = []
  x, y = position[0], position[1]  # Current coordinates
  if position[1] != maze_length - 1:  # EAST
    if walls[x][y][0] == "O":
      pos_moves.append([position[0], position[1] + 1])
  if position[0] != maze_length - 1:  # SOUTH
    if walls[x][y][1] == "O":
      pos_moves.append([position[0] + 1, position[1]])
  if position[1] != 0:  # WEST
    if walls[x][y][2] == "O":
      pos_moves.append([position[0], position[1] - 1])
  if position[0] != 0:  # NORTH
    if walls[x][y][3] == "O":
      pos_moves.append([position[0] - 1, position[1]])
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
    if is_trap(node.position):
      cost_of_solution += 7
    else:
      cost_of_solution += 1
    solution_path.append([node.position[0] + 1, node.position[1] + 1])
    node = node.parent
  solution_path.reverse()


def print_queue(queue):
  positions = []
  for node in queue:
    positions.append([node.position, node.cost])
  print("\nQueue: ", positions)


def order_frontier_by_cost(parent, priority_queue, p_positions):
  new_priority_queue, new_nodes = [], []
  with_trap, without_trap = [], []

  for position in p_positions:
    if not is_visited(position):
      if is_trap(position):
        child = Node(parent, position, parent.depth + 1, parent.cost + 7)
        with_trap.append(child)
      else:
        child = Node(parent, position, parent.depth + 1, parent.cost + 1)
        without_trap.append(child)

  new_nodes = with_trap + without_trap

  if not priority_queue:
    while new_nodes:
      node = new_nodes.pop()
      new_priority_queue.append(node)
    new_priority_queue.reverse()
    return new_priority_queue

  else:
    if priority_queue:
      old_node = priority_queue.pop()
    else:
      old_node = None

    if new_nodes:
      new_node = new_nodes.pop()
    else:
      new_node = None

    while True:
      if old_node:
        old_node_cost = old_node.cost
      else:
        old_node_cost = 1000
      if new_node:
        new_node_cost = new_node.cost
      else:
        new_node_cost = 1000

      if old_node_cost <= new_node_cost and old_node:
        new_priority_queue.append(old_node)
        if priority_queue:
          old_node = priority_queue.pop()
        else:
          old_node = None

      elif new_node:
        new_priority_queue.append(new_node)
        if new_nodes:
          new_node = new_nodes.pop()
        else:
          new_node = None

      if old_node is None and new_node is None:
        new_priority_queue.reverse()
        return new_priority_queue


# Depth First Search
def dfs():
  global current_position, visited_squares
  frontier = []  # Stack for DFS. Use append() and pop()
  initial_node = Node(None, current_position)
  frontier.append(initial_node)
  while True:
    if not frontier:
      print("Frontier is empty. There is no solution")
      return None
    parent = frontier.pop()
    expanded_nodes.append([parent.position[0] + 1, parent.position[1] + 1])
    if is_goal(parent.position):
      find_solution_path(parent)
      return
    visited_squares.append(parent.position)
    p_positions = possible_positions(parent.position)
    p_positions.reverse()
    for position in p_positions:
      if not is_visited(position):
        child = Node(parent, position, parent.depth + 1)
        frontier.append(child)


# Breadth First Search
def bfs():
  global current_position, visited_squares
  frontier = queue.Queue()  # Stack for DFS. Use append() and pop()
  initial_node = Node(None, current_position)
  frontier.put(initial_node)
  while True:
    if frontier.empty():
      print("Frontier is empty. There is no solution")
      return None
    parent = frontier.get()
    expanded_nodes.append([parent.position[0] + 1, parent.position[1] + 1])
    if is_goal(parent.position):
      find_solution_path(parent)
      return
    visited_squares.append(parent.position)
    p_positions = possible_positions(parent.position)
    for position in p_positions:
      if not is_visited(position):
        child = Node(parent, position, parent.depth + 1)
        frontier.put(child)


# Iterative Deepening Search
def ids():
  global current_position, visited_squares
  initial_node = Node(None, current_position)
  for depth in range(maze_length * maze_length):
    reset_variables()
    frontier = queue.Queue()  # Stack for DFS. Use append() and pop()
    frontier.put(initial_node)
    while not frontier.empty():
      parent = frontier.get()
      expanded_nodes.append([parent.position[0] + 1, parent.position[1] + 1])
      if is_goal(parent.position):
        find_solution_path(parent)
        return
      visited_squares.append(parent.position)
      p_positions = possible_positions(parent.position)
      if parent.depth < depth:
        for position in p_positions:
          if not is_visited(position):
            child = Node(parent, position, parent.depth + 1)
            frontier.put(child)


# Uniform Cost Search
def ucs():
  global current_position
  priority_queue = []  # To keep least cost neighbour squares in IDS
  initial_node = Node(None, current_position)
  priority_queue.append(initial_node)
  while True:
    if not priority_queue:
      print("Frontier is empty. There is no solution")
      return None
    parent = priority_queue.pop()
    expanded_nodes.append([parent.position[0] + 1, parent.position[1] + 1])
    if is_goal(parent.position):
      find_solution_path(parent)
      return
    visited_squares.append(parent.position)
    p_positions = possible_positions(parent.position)
    p_positions.reverse()
    priority_queue = order_frontier_by_cost(parent, priority_queue, p_positions)


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
  find_square_features()

  # WARNING: Order of node expansion should be East, South, West, North
  # dfs()
  # bfs()
  # ids()
  ucs()

  """
  print("a. Depth First Search\n" +
        "b. Breadth First Search\n" +
        "c. Iterative Deepening Search\n" +
        "d. Depth First Search with Random Selection\n" +
        "e. Depth First Search with a Node Selection Heuristic")
  method = input("Choose a search method: ")
  if method == 'a':
    print("\nSearch method is: Depth First Search")
    dfs()
  elif method == 'b':
    print("\nSearch method is: Breadth First Search")
    bfs()
  elif method == 'c':
    print("\nSearch method is: Iterative Deepening Search")
    ids()
  elif method == 'd':
    print("\nSearch method is: Uniform Cost Search")
    ucs()
  elif method == 'r':
    print("\nSearch method is: Greedy Best First Search")
    gbfs()
  elif method == 'f':
    print("\nSearch method is: A* Heuristic Search")
    ashs()
  """

  # To print result
  print("The cost of the solution: \n", cost_of_solution, "\n")
  print("The solution path is: \n", solution_path, "\n")
  print("Expanded nodes are: \n", expanded_nodes, "\n")


if __name__ == '__main__':
  main()
