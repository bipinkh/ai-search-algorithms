import argparse
import timeit

from resources.ast_3 import A_Star_search
from resources.bfs_3 import breadth_first_search
from  resources.dfs_3 import depth_first_search
from resources.tools_3 import *
from resources.node_3 import Node

# Controls: True or False
is_print = False

# Start
initial_state = None
initial_node = None
goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
goal_node = None

frontier = None
nodes_expanded = 0
max_search_depth = 0
max_frontier_size = 0

moves = list()
costs = set()


function_mapper = {
    'bfs': breadth_first_search,
    'dfs': depth_first_search,
    'ast': A_Star_search,
}

def main():
    global initial_state, initial_node

    # let's define a parser to read arguments from CLI
    parser = argparse.ArgumentParser()
    parser.add_argument('search_algorithm', 'initial_state')
    args = parser.parse_args()

    initial_state = state_from_string(args.initial_state)
    initial_node = Node(None, None, initial_state, 0, 0)
    func = function_mapper[args.search_algorithm]

    # let's calculate the time of execution
    start = timeit.default_timer()
    func(initial_node)
    stop = timeit.default_timer()
    printResult(goal_node, stop - start)


def printResult(reached_goal_node, duration):
    global nodes_expanded, max_frontier_size, max_search_depth

    moves = []
    node = reached_goal_node;
    while node.parent_node is not None:
        moves.append(node.move)
        node = node.parent_node
    moves.reverse()

    file = open('output.txt', 'w')
    file.write("path_to_goal: " + str(moves))
    file.write("\ncost_of_path: " + str(len(moves)))
    file.write("\nnodes_expanded: " + str(nodes_expanded))
    file.write("\nsearch_depth: " + str(goal_node.depth))
    file.write("\nmax_search_depth: " + str(max_search_depth))
    file.write("\nrunning_time: " + format(duration, '.8f'))
    # file.write("\nmax_ram_usage: " + format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000.0, '.8f'))
    file.close()



if __name__ == '__main__':
    main()