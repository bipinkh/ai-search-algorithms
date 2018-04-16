from copy import deepcopy

from node import Node

# final goal state
goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# format for result
result_dict = {
        'goal_node' : None,
        'max_frontier_size' : 0,
        'max_search_depth' : 0,
        'number_nodes_expanded' : 0,
        'moves' : list(),
        'costs' : set()
}


def state_from_string(configuration):
    global board_len, board_side
    data = [ int(i) for i in configuration.split(",") ]
    return to_matrix(data, 3)

def to_matrix(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


# generating and returning children of a state
# the move order is UDLR (Up, Down, Left, Right)

def expand_node(node):
    successors = []

    # Get the position of 0
    row, col = node.getEmptyBlockPosition()

    # expand child node after Up Move
    if row != 0:
        child_state = deepcopy(node.state)
        child_state[row][col] = child_state[row - 1][col]
        child_state[row - 1][col] = 0
        up_node = Node(node, "Up", child_state, node.depth + 1, node.g+1)
        successors.append(up_node)

    # expand child node after Down Move
    if row != 2:
        child_state = deepcopy(node.state)
        child_state[row][col] = child_state[row + 1][col]
        child_state[row + 1][col] = 0
        down_node = Node(node, 'Down', child_state, node.depth + 1, node.g+1)
        successors.append(down_node)

    # expand child node after Left Move
    if col != 0:
        child_state = deepcopy(node.state)
        child_state[row][col] = child_state[row][col - 1]
        child_state[row][col - 1] = 0
        left_node = Node(node, 'Left', child_state, node.depth + 1, node.g+1)
        successors.append(left_node)

    #  # expand child node after Right Move
    if col != 2:
        child_state = deepcopy(node.state)
        child_state[row][col] = child_state[row][col + 1]
        child_state[row][col + 1] = 0
        right_node = Node(node, 'Right', child_state, node.depth + 1, node.g+1)
        successors.append(right_node)

    return successors
