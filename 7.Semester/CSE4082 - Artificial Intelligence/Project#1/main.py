#############################################
#                                           #
#     CSE4082 - Artificial Intelligence     #
#                Project #1                 #
#       150114022 - Oguzhan BOLUKBAS        #
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
starting_position = None
maze_length = -1  # To keep row or column length of the maze

cost_of_solution = -1
solution_path = []  # To keep solution path
expanded_nodes = []  # To keep expanded nodes
visited_squares = []  # To keep visited squares


# To read squares of the maze from input file
def read_squares(path):
  global maze_length
  fp = open(path, "r")
  for cnt, line in enumerate(fp):  # To read file line by line
    char_list = list(line.strip())  # To get rid of "/n"
    squares.append(char_list)
  maze_length = cnt + 1
  fp.close()


# To read walls of the maze from input file
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


# To define square types of the maze from input file
def find_square_features():
  global current_position, starting_position
  r, c = -1, -1  # r keeps row, c keeps column index
  for row in squares:
    r += 1
    c = -1
    for letter in row:
      c += 1
      if letter == "S":  # Starting position
        current_position = [r, c]
        starting_position = [r, c]
      elif letter == "G":  # Goal positions
        goal_positions.append([r, c])
      elif letter == "T":  # Trap posiitons
        trap_positions.append([r, c])


# To find possible squares the agent can move
def possible_positions(position):
  pos_moves = []  # To store possible moves
  x, y = position[0], position[1]  # Current coordinates
  if position[1] != maze_length - 1:  # EAST
    if walls[x][y][0] == "O":  # 'O' means there is no wall between current position and EAST side square
      pos_moves.append([position[0], position[1] + 1])  # To add possible movement to the EAST direction from the current position
  if position[0] != maze_length - 1:  # SOUTH
    if walls[x][y][1] == "O":  # 'O' means there is no wall between current position and SOUTH side square
      pos_moves.append([position[0] + 1, position[1]])  # To add possible movement to the SOUTH direction from the current position
  if position[1] != 0:  # WEST
    if walls[x][y][2] == "O":  # 'O' means there is no wall between current position and WEST side square
      pos_moves.append([position[0], position[1] - 1])  # To add possible movement to the WEST direction from the current position
  if position[0] != 0:  # NORTH
    if walls[x][y][3] == "O":  # 'O' means there is no wall between current position and NORTH side square
      pos_moves.append([position[0] - 1, position[1]])  # To add possible movement to the NORTH direction from the current position
  return pos_moves


# To check whether this position is visited or not
def is_visited(position):
  global visited_squares
  for pos in visited_squares:
    if pos[0] == position[0] and pos[1] == position[1]:  # To check whether this square is visited or not
      return True  # Yes, visited before
  return False  # No, never visited


# To check whether this position is goal or not
def is_goal(position):
  global goal_positions
  for pos in goal_positions:
    if pos[0] == position[0] and pos[1] == position[1]:  # To check whether this square is goal or not
      return True  # Yes, it is goal position
  return False  # No, not goal


# To check whether this position is trap or not
def is_trap(position):
  global trap_positions
  for pos in trap_positions:
    if pos[0] == position[0] and pos[1] == position[1]:  # To check whether this square is trap or not
      return True  # Yes, this square is trapped
  return False  # No, it is safe


# To print solution path when program ends
def find_solution_path(node):
  global solution_path, cost_of_solution
  while node:
    if is_trap(node.position):
      cost_of_solution += 7  # Trap square cost
    else:
      cost_of_solution += 1  # Normal square cost
    solution_path.append([node.position[0] + 1, node.position[1] + 1])
    node = node.parent
  solution_path.reverse()


# To print a queue for visualization
def print_queue(queue):
  positions = []
  for node in queue:
    positions.append([node.position, node.cost])
  print("Queue: ", positions, "\n")


# This method is used by IDS()
def reset_variables():
  global current_position, cost_of_solution, solution_path, expanded_nodes, visited_squares
  current_position = starting_position  # To keep current position coordinates of agent
  cost_of_solution = -1
  solution_path = []  # To keep solution path
  expanded_nodes = []  # To keep expanded nodes
  visited_squares = []  # To keep visited squares


# This method used by UCS()
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


# This methos is used by GBFS()
def find_distance_to_goals(position):
  global maze_length
  total_distance_to_goals = 0
  for x in range(maze_length):
    for y in range(maze_length):
      if is_goal([x, y]):
        total_distance_to_goals += abs(x - position[0]) + abs(y - position[1])
  return total_distance_to_goals


# This method is used by A* Heuristic Search
def order_for_a_star(parent, priority_queue, p_positions, position_and_distances):
  new_priority_queue, new_nodes = [], []
  with_trap, without_trap = [], []

  for position in p_positions:
    if not is_visited(position):
      if is_trap(position):
        child = Node(parent, position, parent.depth + 1, parent.cost + 7 + find_distance_to_goals(position))
        with_trap.append(child)
      else:
        child = Node(parent, position, parent.depth + 1, parent.cost + 1 + find_distance_to_goals(position))
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


"""---------------------------------Search Algorithms---------------------------------"""


# Depth First Search
def dfs():
  global current_position, visited_squares  # To keep current position of the agent in the maze and visited squares' positions
  frontier = []  # Stack for DFS. Use append() and pop()
  initial_node = Node(None, current_position)
  frontier.append(initial_node)
  while True:
    parent = frontier.pop()
    expanded_nodes.append([parent.position[0] + 1, parent.position[1] + 1])
    if is_goal(parent.position):  # To check whether this position is goal or not
      find_solution_path(parent)
      return
    visited_squares.append(parent.position)
    p_positions = possible_positions(parent.position)  # To get all possible positions for the current position
    p_positions.reverse()
    for position in p_positions:
      if not is_visited(position):  # To check whether this square is visited or not
        child = Node(parent, position, parent.depth + 1)
        frontier.append(child)


# Breadth First Search
def bfs():
  global current_position, visited_squares  # To keep current position of the agent in the maze and visited squares' positions
  frontier = queue.Queue()  # Queue for BFS. Use put() and get()
  initial_node = Node(None, current_position)
  frontier.put(initial_node)
  while True:
    parent = frontier.get()
    expanded_nodes.append([parent.position[0] + 1, parent.position[1] + 1])
    if is_goal(parent.position):  # To check whether this position is goal or not
      find_solution_path(parent)
      return
    visited_squares.append(parent.position)
    p_positions = possible_positions(parent.position)  # To get all possible positions for the current position
    for position in p_positions:
      if not is_visited(position):  # To check whether this square is visited or not
        child = Node(parent, position, parent.depth + 1)
        frontier.put(child)


# Iterative Deepening Search
def ids():
  global current_position, visited_squares  # To keep current position of the agent in the maze and visited squares' positions
  initial_node = Node(None, current_position)
  for depth in range(maze_length * maze_length):  # To traverse in all depth with increasing depth one by one
    reset_variables()  # To reset all stored knowledge for previous depth level
    frontier = [initial_node]
    while frontier:
      parent = frontier.pop()
      expanded_nodes.append([parent.position[0] + 1, parent.position[1] + 1])
      if is_goal(parent.position):  # To check whether this position is goal or not
        find_solution_path(parent)
        return
      visited_squares.append(parent.position)
      p_positions = possible_positions(parent.position)  # To get all possible positions for the current position
      p_positions.reverse()
      if parent.depth < depth:
        for position in p_positions:
          if not is_visited(position):  # To check whether this square is visited or not
            child = Node(parent, position, parent.depth + 1)
            frontier.append(child)


# Uniform Cost Search
def ucs():
  global current_position  # To keep current position of the agent in the maze
  priority_queue = []  # To keep least cost neighbour squares in IDS
  initial_node = Node(None, current_position)
  priority_queue.append(initial_node)
  while True:
    parent = priority_queue.pop()
    expanded_nodes.append([parent.position[0] + 1, parent.position[1] + 1])
    if is_goal(parent.position):  # To check whether this position is goal or not
      find_solution_path(parent)
      return
    visited_squares.append(parent.position)
    p_positions = possible_positions(parent.position)  # To get all possible positions for the current position
    p_positions.reverse()
    priority_queue = order_frontier_by_cost(parent, priority_queue, p_positions)  # To order the frontier list in order to get low cost movement in the next movement


# Greedy Best First Search
def gbfs():
  global current_position, visited_squares  # To keep current position of the agent in the maze and visited squares' positions
  frontier = []  # Stack for GBFS
  initial_node = Node(None, current_position)
  frontier.append(initial_node)
  find_distance_to_goals(starting_position)
  while True:
    parent = frontier.pop()
    expanded_nodes.append([parent.position[0] + 1, parent.position[1] + 1])
    if is_goal(parent.position):  # To check whether this position is goal or not
      find_solution_path(parent)
      return
    visited_squares.append(parent.position)
    p_positions = possible_positions(parent.position)  # To get all possible positions for the current position
    p_positions.reverse()
    position_and_distances = []
    for position in p_positions:
      if not is_visited(position):  # To check whether this square is visited or not
        distance = find_distance_to_goals(position)
        position_and_distances.append([position, distance])
    for dist in range(1000, 0, -1):  # This for loop appends the new nodes to frontier according to their cost
      for pos_and_dist in position_and_distances:
        if dist == pos_and_dist[1]:
          child = Node(parent, pos_and_dist[0], parent.depth + 1)
          frontier.append(child)


# A* Heuristic Search
def ashs():
  global current_position  # To keep current position of the agent in the maze
  priority_queue = []  # To keep least cost neighbour squares in IDS
  initial_node = Node(None, current_position)
  priority_queue.append(initial_node)
  while True:
    parent = priority_queue.pop()
    expanded_nodes.append([parent.position[0] + 1, parent.position[1] + 1])
    if is_goal(parent.position):  # To check whether this position is goal or not
      find_solution_path(parent)
      return
    visited_squares.append(parent.position)
    p_positions = possible_positions(parent.position)  # To get all possible positions for the current position
    p_positions.reverse()
    position_and_distances = []
    for position in p_positions:
      if not is_visited(position):  # To check whether this square is visited or not
        distance = find_distance_to_goals(position)
        position_and_distances.append([position, distance])
    priority_queue = order_for_a_star(parent, priority_queue, p_positions, position_and_distances)


def main():
  input_squares_path = "./inputs/maze_1/squares.txt"  # Path of the square.txt filewhich stores square letters
  input_walls_path = "./inputs/maze_1/walls.txt"  # Path of the walls.txt file which stores walls between squares
  read_squares(input_squares_path)  # To read a file which contains square letters
  read_walls(input_walls_path)    # To read a file which contains wall positions
  find_square_features()  # To understand which letter means what like G means Goal, when it reach the program ends succesfully

  print("\nChoose a search method from below:\n" +
        "a. Depth First Search\n" +
        "b. Breadth First Search\n" +
        "c. Iterative Deepening Search\n" +
        "d. Uniform Cost Search\n" +
        "e. Greedy Best First Search\n" +
        "f. A* Heuristic Search\n")
  method = input("Choose a search method: ")
  if method == 'a':
    print("\nSearch method is: Depth First Search")
    dfs()  # To run DFS Algorithm
  elif method == 'b':
    print("\nSearch method is: Breadth First Search")
    bfs()  # To run BFS Algorithm
  elif method == 'c':
    print("\nSearch method is: Iterative Deepening Search")
    ids()  # To run IDS Algorithm
  elif method == 'd':
    print("\nSearch method is: Uniform Cost Search")
    ucs()  # To run UCS Algorithm
  elif method == 'e':
    print("\nSearch method is: Greedy Best First Search")
    gbfs()  # To run GBFS Algorithm
  elif method == 'f':
    print("\nSearch method is: A* Heuristic Search")
    ashs()  # To run A*HS Algorithm

  # To print result
  print("Cost of the solution: \n", cost_of_solution, "\n")
  print("Solution path: \n", solution_path, "\n")
  print("Expanded nodes: \n", expanded_nodes, "\n")


if __name__ == '__main__':
  main()