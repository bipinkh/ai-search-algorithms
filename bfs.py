from collections import deque

import tools
from tools import *


def breadth_first_search(start_node):

    goal_state = tools.goal_state

    # dictionary instance to hold the result values
    result = result_dict.copy()

    #define data structure
    explored , queue = set(), deque()
    queue.append(start_node)

    while queue:

        # Step 1: Dequeue

        node = queue.popleft()
        explored.add(node.map)

        #Step 2 : Check if it is goal node

        if node.state == goal_state:
            result['goal_node'] = node
            return result

        #Step 3 : expand node

        childNodes =  expand_node(node)
        result['number_nodes_expanded'] += 1

        #check if the child node is already explored. if not, then only add it to the queue

        for childNode in childNodes:
            if childNode.map not in explored:
                queue.append(childNode)
                explored.add(childNode.map)

                # see if the depth of children is the max depth we have covered
                if childNode.depth > result['max_search_depth']:
                    result['max_search_depth'] += 1

        if len(queue) > result['max_frontier_size']:
            result['max_frontier_size'] = len(queue)

    return None