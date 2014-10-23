__author__ = 'kinsumliu'
import random


def min_conflicts(csp, max_step):
    """
    minimum conflicts algorithm for Iterative Improvement
    :param csp:
    :param max_step:
    :return:
    """
    #initialize the current assignment
    current = dict()
    i = 0
    while i < csp.n:
        value = random.randint(0, csp.d-1)
        if value in current.values():
            pass
        else:
            current[i] = value
            i += 1
    current[0] = 0
    current[csp.n-1] = csp.d-1

    #main loop
    for i in range(max_step):
        if csp.consistent(-1,-1,current):
            #if current assignment is a solution
            return current, i
        #var =  a randomly chosen conflicted variable from csp.variables
        var = csp.conflicted(current)
        #value = the value v for var that minimizes conflicts(var, v, current, csp)
        value = csp.minimize_conflicts(var, current)
        #set var with value in current
        current[var] = value
    return False, max_step


def print_distance(assignment, csp):
    """
    helper function for debugging
    :param assignment:
    :param csp:
    :return:
    """
    self = csp
    distance_list = list()
    for i in range(self.n):
        for j in range(self.n - 1 - i):
            b = assignment[self.n - 1 - i]
            a = assignment[(self.n - 1 - i) - (j + 1)]
            distance_list.append(abs(b-a))
    distance_list.sort()
    print(distance_list)