__author__ = 'kinsumliu'
from models.node import Node
from models.problem import Problem


class SlidingTile(Problem):
    black = -1
    white = 1
    empty = 0
    expand_counter = 0

    def __init__(self, initial):
        self.initial_node = initial

    # Problem-specific successors function
    def succ (self, node):
        vec = node.vec
        i = vec.index(0)  # Index of the empty tile

        # Create the set of succ
        successors = set()
        if i > 0:
            successors.add( ("Left" , Node( node.swap_element( i-1, i ) ) ) )
        if i < len(vec)-1:
            successors.add( ("Right" , Node( node.swap_element( i, i+1 ) ) ) )
        if i - 1 > 0:
            successors.add( ("Left1" , Node( node.swap_element( i-2, i ) ) ) )
        if i + 1 < len(vec)-1:
            successors.add( ("Right1" , Node( node.swap_element( i, i+2 ) ) ) )
        if i - 2 > 0:
            successors.add( ("Left2" , Node( node.swap_element( i-3, i ) ) ) )
        if i + 2 < len(vec)-1:
            successors.add( ("Right2" , Node( node.swap_element( i, i+3 ) ) ) )
        return successors

    # Problem-specific goal test
    def goal_test(self, node):
        first_black = node.vec.index(-1)
        for i in range(len(node.vec)):
            if node.vec[i] == self.white and i > first_black:
                return False
        return True

    def step_cost(self, node, action, s):
        if action == "Left":
            return 1
        elif action == "Right":
            return 1
        elif action == "Left1":
            return 1
        elif action == "Right1":
            return 1
        elif action == "Left2":
            return 2
        elif action == "Right2":
            return 2
        else:
            return 0