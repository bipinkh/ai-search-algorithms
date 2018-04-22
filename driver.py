import argparse
import timeit

import resource
from ast import A_Star_search
from bfs import breadth_first_search
from  dfs import depth_first_search
from tools import *

from node import Node

function_mapper = {
    'bfs': breadth_first_search,
    'dfs': depth_first_search,
    'ast': A_Star_search
}

def main():
    global initial_state, initial_node

    # let's define a parser to read arguments from CLI
    parser = argparse.ArgumentParser()
    parser.add_argument('search_algorithm')
    parser.add_argument('initial_state')
    args = parser.parse_args()

    initial_state = state_from_string(args.initial_state)
    initial_node = Node(None, None, initial_state, 0, 0)
    func = function_mapper[args.search_algorithm]

    # let's calculate the time of execution
    start = timeit.default_timer()
    result = func(initial_node)
    stop = timeit.default_timer()
    printResult(stop - start , result)


def printResult(duration , result):

    moves = []
    if result['goal_node'] is not None:
        pathNode = result['goal_node']
        while pathNode.parent_node is not None:
            moves.append(pathNode.move)
            pathNode = pathNode.parent_node
        moves.reverse()

        file = open('output.txt', 'w')
        file.write("path_to_goal: " + str(moves))
        file.write("\ncost_of_path: " + str(len(moves)))
        file.write("\nnodes_expanded: " + str(result['number_nodes_expanded']))
        file.write("\nsearch_depth: " + str(result['goal_node'].depth))
        file.write("\nmax_search_depth: " + str(result['max_search_depth']))
        file.write("\nrunning_time: " + format(duration, '.8f'))
        file.write("\nmax_ram_usage: " + format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000.0, '.8f'))
        file.close()



if __name__ == '__main__':
    main()