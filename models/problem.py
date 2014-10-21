__author__ = 'kinsumliu'
"""
Interface for a problem
"""


class Problem:

    def __init__(self, initial):
        self.initial_node = initial

    def succ(self, state):
        pass

    def goal_test(self, state):
        pass

    def step_cost(self, state, action, s):
        pass

