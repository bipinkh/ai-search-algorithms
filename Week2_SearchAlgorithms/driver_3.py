import argparse
from asyncore import read
import timeit
from node_3 import Node
from bfs_3 import breadth_first_search
from  dfs_3 import depth_first_search
from ast_3 import A_Star_search

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

    initial_state = read(args.initial_state)
    initial_node = Node(None, None, initial_state, 0, 0, False)
    func = function_mapper[args.search_algorithm]

    # let's calculate the time of execution
    start = timeit.default_timer()
    func(initial_node)
    stop = timeit.default_timer()
    # export(goal_node, stop - start)


if __name__ == '__main__':
    main()