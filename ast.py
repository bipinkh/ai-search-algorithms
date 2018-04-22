import itertools
from heapq import heappush, heappop, heapify

import tools
from tools import *


def A_Star_search(start_node):

    goal_state = tools.goal_state

    # dictionary instance to hold the result values
    result = result_dict.copy()

    #define data structure
    explored, heap = set(), list()
    heap_entry, heap_counter, counter =  {}, {}, itertools.count()
    count = next(counter)

    #heuristic things
    start_node.set_h(hCalculator(start_node))
    heap_tuple = (start_node.g + start_node.h, count, start_node)
    heappush(heap, heap_tuple)
    heap_entry[start_node.map] = heap_tuple
    heap_counter[start_node.map] = count


    while heap:

        #Step 1: Pop the element from heap

        node = heappop(heap)
        explored.add(node[2].map)
        del heap_entry[node[2].map]

        #Step 2: Check if the node is goal_node
        if node[2].state == goal_state:
            result['goal_node'] = node[2]
            return result

        # Step 3 : expand node

        childNodes = tools.expand_node(node[2])
        result['number_nodes_expanded'] += 1

        #check if the child node is already explored. if not, then only add it to the queue

        for childNode in childNodes:
            count = next(counter)
            childNode.set_h(hCalculator(childNode))
            heap_tuple = (childNode.g + childNode.h, count, childNode)

            if childNode.map not in explored:
                heappush(heap, heap_tuple)
                explored.add(childNode.map)
                heap_entry[childNode.map] = heap_tuple

                # see if the depth of children is the max depth we have covered
                if childNode.depth > result['max_search_depth']:
                    result['max_search_depth'] += 1

            if childNode.map in heap_entry and (childNode.g+childNode.h) <  (heap_entry[childNode.map][2].g+heap_entry[childNode.map][2].h):
                hindex = heap.index((heap_entry[childNode.map][2].g+heap_entry[childNode.map][2].h,
                                     heap_entry[childNode.map][1],
                                     heap_entry[childNode.map][2]))
                heap[int(hindex)] = heap_tuple
                heap_entry[childNode.map] = heap_tuple
            heapify(heap)

        if len(heap) > result['max_frontier_size']:
            result['max_frontier_size'] = len(heap)


    return None

def hCalculator(node):
    heuristics = 0
    for i in range(1, 9):
        pos_in_node = index_2d(node.state, i)
        pos_in_goal = index_2d(tools.goal_state, i)
        md = (abs(pos_in_node[1] - pos_in_goal[1]) + abs(pos_in_node[0] - pos_in_goal[0]))
        heuristics += md
    return heuristics


# supporting function that returns position of 1 number in the 2D matrix as a tuple of (x,y)
def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))
