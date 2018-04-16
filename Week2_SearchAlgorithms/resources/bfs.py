from collections import deque

from resources.tools import *

goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

def breadth_first_search(start_node):

    # dictionary instance to hold the result values
    result = {
        'goal_node': None,
        'max_frontier_size': 0,
        'max_search_depth': 0,
        'number_nodes_expanded': 0,
        'moves': list(),
        'costs': set()
    }

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