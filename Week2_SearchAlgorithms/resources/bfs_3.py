from collections import deque

from driver_3 import is_print, goal_state
from resources.tools_3 import *


def breadth_first_search(start_node):

    global max_frontier_size, goal_node, max_search_depth, number_nodes_expanded

    #reset trackers
    number_nodes_expanded = 0
    max_search_depth = 0
    max_frontier_size = 0
    goal_node = None

    #define data structure
    explored , queue = set(), deque()
    queue.append(start_node)

    while queue:

        # Step 1: Dequeue

        node = queue.popleft()
        if is_print == True:
            print(node.state)
        explored.add(node.map)

        #Step 2 : Check if it is goal node

        if node.state == goal_state:
            goal_node = node
            return goal_node

        #Step 3 : expand node

        childNodes =  expand_node(node)
        number_nodes_expanded += 1

        #check if the child node is already explored. if not, then only add it to the queue

        for childNode in childNodes:
            if childNode.map not in explored:
                queue.append(childNode)
                explored.add(childNode.map)

                # see if the depth of children is the max depth we have covered
                if childNode.depth > max_search_depth:
                    max_search_depth += 1

        if len(queue) > max_frontier_size:
            max_frontier_size = len(queue)

    return None