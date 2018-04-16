class Node:

    def __init__(self, parent_node = None, move=None, state=None, depth=0, g=0):
        self.parent_node = parent_node  # the anccestor of this node
        self.move = move    # Up, Down, Left, Right
        self.state = state  # 2D Array of state
        self.depth = depth
        self.__map()
        self.g = g
        self.heuristics = 0

    def __map(self):
        self.map = ''.join(str(r) for v in self.state for r in v)

    def set_heuristics(self, heuristics):
        self.heuristics = heuristics

    def set_g(self, g):
        self.g = g


    def getEmptyBlockPosition(self):
        for row in range(0, 3):
            for column in range(0, 3):
                if self.state[row][column] == 0:
                    return row, column
        return None,None

