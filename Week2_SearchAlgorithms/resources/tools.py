from copy import deepcopy

from resources.node import Node


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
