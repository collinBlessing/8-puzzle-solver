import random
# The Node class represents a node in the graph, with a state, parent node, and action.
class Node:
    def __init__(self, state, parent=None, action=None):
        """
        The above function is a constructor for a class that initializes the state, parent, and action
        attributes.

        :param state: The state parameter represents the current state of the object or system that this
        class is modeling. It can be any data or information that is relevant to the object's behavior or
        characteristics
        :param parent: The parent parameter is used to keep track of the parent node in a tree or graph
        structure. It represents the node from which the current node was generated
        :param action: The `action` parameter represents the action that was taken to reach the current
        state. It can be any value that represents the action, such as a string or an integer
        """
        self.state = state
        self.parent = parent
        self.action = action


def breadth_first_search(initial_state):
    """
    The function implements the breadth-first search algorithm to explore a graph starting from an
    initial state.

    :param initial_state: The initial state is the starting point of the search algorithm. It represents
    the state of the problem that needs to be solved. In the context of the breadth-first search
    algorithm, the initial state is the state from which the search begins
    """
    start_node = Node(initial_state)
    frontier = [start_node]
    frontier_set = {tuple(initial_state)}
    explored = set()


    while frontier:
        current_node = frontier.pop(0)
        frontier_set.remove(tuple(current_node.state))
        explored.add(tuple(current_node.state))

# The code block `if current_node.state == [1, 2, 3, 4, 5, 6, 7, 8, 0]: return
# reconstruct_path(current_node)` is checking if the current node's state is equal to the goal state
# of the 8-puzzle problem, which is represented as `[1, 2, 3, 4, 5, 6, 7, 8, 0]`.
        if current_node.state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            return reconstruct_path(current_node)

# This code is responsible for generating the successors of the current node in the
# 8-puzzle problem and adding them to the frontier for further exploration.
        for action, successor_state in get_successors(current_node.state):
            successor_tuple = tuple(successor_state)
# This code is responsible for generating the successors of the current node in the
# 8-puzzle problem and adding them to the frontier for further exploration.
            if successor_tuple not in explored and successor_tuple not in frontier_set:
                frontier.append(Node(successor_state, current_node, action))
                frontier_set.add(successor_tuple)

# The `return None` statement is used to indicate that no solution was found for the puzzle. 
# If the algorithm exhausts all possible states to
# explore and none of them match the goal state, it means that there is no solution. In that case, the
# function returns `None` to indicate the absence of a solution.
    return None



def reconstruct_path(node):
    """
    The function `reconstruct_path` takes a node and returns a list of actions that lead to that node by
    traversing its parent nodes.
    
    :param node: The parameter "node" is referring to a node in a graph or tree data structure. Each
    node typically has properties such as "action" and "parent". The "action" property represents the
    action taken to reach the current node, and the "parent" property represents the parent node from
    which the
    :return: a list of actions that represent the path from the given node to the root node.
    """
    path = []
    while node:
        path.append(node.action)
        node = node.parent
    return path[::-1]


def get_successors(state):
    """
    The function `get_successors` takes a state of a 3x3 puzzle represented as a list and returns a list
    of possible successor states along with the action required to reach each successor state.

    :param state: The `state` parameter represents the current state of the puzzle. It is a list of
    integers representing the tiles on the puzzle board. The empty tile is represented by the integer 0
    :return: The function `get_successors` returns a list of tuples. Each tuple contains an action and a
    successor state.
    """
    successors = []
    empty_tile_index = state.index(0)
    row, col = empty_tile_index // 3, empty_tile_index % 3

# The line `moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]` is creating a list of tuples representing the
# possible moves in the 8-puzzle problem. Each tuple represents a move in the form (row_change,
# col_change), where row_change and col_change represent the change in row and column indices,
# respectively.
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# This code is generating the successors of the current state in the 8-puzzle
# problem. It iterates over the possible moves (up, down, left, right) and checks if the move is valid
# (within the bounds of the puzzle board).
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
# This code is generating the successors of the current state in the 8-puzzle
# problem.
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            successor_state = state[:]
            successor_state[empty_tile_index], successor_state[new_row * 3 +
                                                               new_col] = successor_state[new_row * 3 + new_col], successor_state[empty_tile_index]
            action = f"Move {successor_state[empty_tile_index]} to empty space"
            successors.append((action, successor_state))

    return successors


def in_frontier(frontier, state):
    """
    The function checks if a given state is present in the frontier.

    :param frontier: A list of nodes representing the frontier of a search algorithm. Each node has a
    state attribute that represents the state of the problem
    :param state: The state parameter represents the state of a node. It is used to check if a node with
    the given state is present in the frontier
    :return: a boolean value. It returns True if there is a node in the frontier with the given state,
    and False otherwise.
    """
    return any(node.state == state for node in frontier)


def get_inversion_count(state):
    """
    The function calculates the inversion count of a given state.

    :param state: The "state" parameter is a list representing the current state of a puzzle. It
    contains 9 elements, each representing a number from 1 to 8, and one empty space represented by 0.
    The elements in the list are arranged in a 3x3 grid, where the first
    :return: the inversion count of the given state.
    """
    inversion_count = 0
    for i in range(9):
        #Inversion count is a concept used in determining the solvability of the 8-puzzle problem.
        # The inversion count is the number of pairs of tiles that are in the wrong order. In a solvable state,
        # the inversion  count must be even. If it's odd, the puzzle is not solvable
        for j in range(i+1, 9):
            if state[j] and state[i] and state[i] > state[j]:
                inversion_count += 1
    return inversion_count

def generate_random_state():
    """This function generates a random initial state"""
    numbers = list(range(9))  # Represents the numbers 0 to 8
    random.shuffle(numbers)  # Shuffles the numbers randomly
    return numbers


def main():
    """"This is the entry point of the program"""
        # 8-puzzle problem using the breadth-first search algorithm.
    initial_state = generate_random_state()
    print("Initial State:", initial_state)

    if get_inversion_count(initial_state) % 2 == 1:
        print("This puzzle is not solvable.")
    # Checking if the `steps` variable returned by the
    # `breadth_first_search` function is `None`. If it is `None`, it means that no solution was found for
    # the puzzle. In that case, it prints the message "No solution found."
    else:
        steps = breadth_first_search(initial_state)
        if steps is None:
            print("No solution found.")
    # This code is responsible for printing the steps to solve the puzzle if a solution
    # is found. It iterates over the `steps` list, which contains the actions taken to reach each state in
    # the solution path.
        else:
            for i, step in enumerate(steps):
                if step is not None:  # the first step will be None because it's the initial state
                    print(f"Step {i} -> {step}")
                    
                    
if __name__ == "__main__":
    main()                    
