# import argparse
# import heapq
# import time
# import timeit
# import resource
# from asyncore import read
# from collections import deque
# from copy import deepcopy
# from heapq import heappush, heappop, heapify
# import itertools
#
#
# # Controls: True or False
# is_print = False
#
# # Start
# initial_state = None
# initial_node = None
# goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# goal_node = None
#
# frontier = None
# nodes_expanded = 0
# max_search_depth = 0
# max_frontier_size = 0
#
# moves = list()
# costs = set()
#
#
#
#
# class Node():
#     def __init__(self, parent_node=None, move=None, state=None, depth=0, g=0):
#         self.parent_node = parent_node
#         self.move = move
#         self.state = state
#         self.depth = depth
#         self.__map()
#         self.g = g
#         self.h = 0
#
#     def __map(self):
#         self.map = ''.join(str(r) for v in self.state for r in v)
#
#     def set_h(self, h):
#         self.h = h
#
#     def set_g(self, g):
#         self.g = g
#
# # generating and returning children of a state
# def expand(parent):
#     parent_state = parent.state
#     parent_depth = parent.depth
#     parent_g = parent.g
#     children = []
#
#     # Get the position of 0
#     row, col = None, None
#     for i in range(0, 3):
#         for j in range(0, 3):
#             if parent_state[i][j] == 0:
#                 row = i
#                 col = j
#                 break
#         if row is not None and col is not None:
#             break
#
#     # For Up
#     if row != 0:
#         derived_state = deepcopy(parent_state)
#         derived_state[row][col] = derived_state[row - 1][col]
#         derived_state[row - 1][col] = 0
#         up_node = Node(parent, "Up", derived_state, parent_depth + 1, parent_g+1)
#         children.append(up_node)
#
#     # For Down
#     if row != 2:
#         derived_state = deepcopy(parent_state)
#         derived_state[row][col] = derived_state[row + 1][col]
#         derived_state[row + 1][col] = 0
#         down_node = Node(parent, 'Down', derived_state, parent_depth + 1, parent_g+1)
#         children.append(down_node)
#
#     # For Left
#     if col != 0:
#         derived_state = deepcopy(parent_state)
#         derived_state[row][col] = derived_state[row][col - 1]
#         derived_state[row][col - 1] = 0
#         left_node = Node(parent, 'Left', derived_state, parent_depth + 1, parent_g+1)
#         children.append(left_node)
#
#     # For Right
#     if col != 2:
#         derived_state = deepcopy(parent_state)
#         derived_state[row][col] = derived_state[row][col + 1]
#         derived_state[row][col + 1] = 0
#         right_node = Node(parent, 'Right', derived_state, parent_depth + 1, parent_g+1)
#         children.append(right_node)
#
#     return children
#
#
# def bfs(start_node):
#     global max_frontier_size, goal_node, max_search_depth, nodes_expanded
#
#     explored, queue = set(), deque(),
#     queue.append(start_node)
#
#     while queue:
#         node = queue.popleft()
#         if is_print == True:
#             print node.state
#         explored.add(node.map)
#
#         if node.state == goal_state:
#             goal_node = node
#             return goal_node
#
#         children = expand(node)
#         nodes_expanded = nodes_expanded + 1
#         for child in children:
#             if child.map not in explored:
#                 queue.append(child)
#                 explored.add(child.map)
#
#                 if child.depth > max_search_depth:
#                     max_search_depth += 1
#
#         if len(queue) > max_frontier_size:
#             max_frontier_size = len(queue)
#
# def dfs(start_node):
#     global max_frontier_size, goal_node, max_search_depth, nodes_expanded
#
#     explored, queue = set(), deque(),
#     queue.append(start_node)
#
#     while queue:
#         node = queue.pop()
#         if is_print == True:
#             print node.state
#         explored.add(node.map)
#
#         if node.state == goal_state:
#             goal_node = node
#             return goal_node
#
#         children = reversed(expand(node))
#         nodes_expanded = nodes_expanded + 1
#         for child in children:
#             if child.map not in explored:
#                 queue.append(child)
#                 explored.add(child.map)
#
#                 if child.depth > max_search_depth:
#                     max_search_depth += 1
#
#         if len(queue) > max_frontier_size:
#             max_frontier_size = len(queue)
#
#
# # a star search
# def ast(start_node):
#
#     global max_frontier_size, goal_node, max_search_depth, nodes_expanded
#     explored, heap, heap_entry, heap_counter, counter = set(), list(), {}, {}, itertools.count()
#
#     count = next(counter)
#     add_heuristics(start_node)
#     heap_tuple = (start_node.g + start_node.h, count, start_node)
#     heappush(heap, heap_tuple)
#     heap_entry[start_node.map] = heap_tuple
#     heap_counter[start_node.map] = count
#
#     while heap:
#         # for item in heap:
#         #     print item[2].map
#         node = heappop(heap)
#         if is_print == True:
#             print node[2].state
#         explored.add(node[2].map)
#         del heap_entry[node[2].map]
#         # print node, node[2].state
#         # raw_input()
#
#         # Check Goal
#         if node[2].state == goal_state:
#             goal_node = node[2]
#             return goal_node
#
#         # If not goal expand and add
#         children = expand(node[2])
#         nodes_expanded = nodes_expanded + 1
#         for child in children:
#             count = next(counter)
#             add_heuristics(child)
#             heap_tuple = (child.g + child.h, count, child)
#             if child.map not in explored:
#                 heappush(heap, heap_tuple)
#                 explored.add(child.map)
#                 heap_entry[child.map] = heap_tuple
#                 if child.depth > max_search_depth:
#                     max_search_depth += 1
#
#             if child.map in heap_entry and (child.g+child.h) <  (heap_entry[child.map][2].g+heap_entry[child.map][2].h):
#                 hindex = heap.index((heap_entry[child.map][2].g+heap_entry[child.map][2].h,
#                                      heap_entry[child.map][1],
#                                      heap_entry[child.map][2]))
#                 heap[int(hindex)] = heap_tuple
#                 heap_entry[child.map] = heap_tuple
#             heapify(heap)
#
#         if len(heap) > max_frontier_size:
#             max_frontier_size = len(heap)
#
#
# # add heuristic data in the node
# def add_heuristics(node):
#     node.set_h(h(node))
#
#
# # returns heuristics of a node
# def h(node):
#     heuristics = 0
#     for i in range(1,9):
#         pos_in_node = index_2d(node.state, i)
#         pos_in_goal = index_2d(goal_state, i)
#         md = (abs(pos_in_node[1]-pos_in_goal[1]) + abs(pos_in_node[0]-pos_in_goal[0]))
#         heuristics += md
#     return heuristics
#
# # supporting function that returns position of 1 number in the 2D matrix as a tuple of (x,y)
# def index_2d(myList, v):
#     for i, x in enumerate(myList):
#         if v in x:
#             return (i, x.index(v))
#
# def simpleh(node):
#     heuristics = 0
#     for i in range(1, 9):
#         pos_in_node = index_2d(node.state, i)
#         pos_in_goal = index_2d(goal_state, i)
#         md = (abs(pos_in_node[1] - pos_in_goal[1]) + abs(pos_in_node[0] - pos_in_goal[0]))
#         heuristics += md
#         print md
#     print heuristics
#
#
# def just_expand(node):
#     nodes = expand(node)
#
# def read(configuration):
#     global board_len, board_side
#     data = map(int, configuration.split(","))
#     return to_matrix(data, 3)
#
# def to_matrix(l, n):
#     return [l[i:i+n] for i in xrange(0, len(l), n)]
#
# def export(reached_goal_node, duration):
#     global nodes_expanded, max_frontier_size, max_search_depth
#
#     moves = []
#     node = reached_goal_node;
#     while node.parent_node is not None:
#         moves.append(node.move)
#         node = node.parent_node
#     moves.reverse()
#
#     file = open('output.txt', 'w')
#     file.write("path_to_goal: " + str(moves))
#     file.write("\ncost_of_path: " + str(len(moves)))
#     file.write("\nnodes_expanded: " + str(nodes_expanded))
#     file.write("\nsearch_depth: " + str(goal_node.depth))
#     file.write("\nmax_search_depth: " + str(max_search_depth))
#     file.write("\nrunning_time: " + format(duration, '.8f'))
#     file.write("\nmax_ram_usage: " + format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000.0, '.8f'))
#     file.close()
#
#
# def main():
#     global initial_state, initial_node
#
#     parser = argparse.ArgumentParser()
#     parser.add_argument('algorithm')
#     parser.add_argument('board')
#     args = parser.parse_args()
#
#     initial_state = read(args.board)
#     initial_node = Node(None, None, initial_state, 0, 0)
#     func = function_map[args.algorithm]
#
#     start = timeit.default_timer()
#     func(initial_node)
#     stop = timeit.default_timer()
#     export(goal_node, stop - start)
#
#
# function_map = {
#     'bfs': bfs,
#     'dfs': dfs,
#     'ast': ast,
#     # 'h': simpleh
# }
#
# if __name__ == '__main__':
#     main()