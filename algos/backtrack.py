__author__ = 'kinsumliu'
import copy


def backtracking_search(csp):
    return _backtrack(csp.assignment, csp)


def _backtrack(assignment, csp):
    """
    the general backtrack algorithm for BT, BT_MRV, BT_MRV_FC, BT_MRV_CP
    :param assignment:
    :param csp: the problem instance
    :return: a complete assignment if found or False for failure
    """
    if csp.complete(assignment) and csp.consistent(-1,-1,assignment):
        #if the assignment is complete and valid, return the result
        return assignment
    var = csp.select_unassigned_variable()
    for value in csp.order_domain_values(var, assignment):
        csp.counter += 1 # increase the counter for each consistency check
        if csp.consistent(var, value, assignment):
            #if consistent
            assignment[var] = value
            domain = [[1 for x in range(csp.d)] for x in range(csp.n)]
            csp.deepcopy_domain(domain, csp.domain)
            inferences = csp.inference(var, value)
            if inferences is not False:
                #add inferences to assignment
                for inference in inferences:
                    assignment[inference[0]] = inference[1]
                result = _backtrack(assignment, csp)
                if result is not False:
                    return result
            #remove {var = value} and inferences from assignment, restore the domain
            assignment[var] = None
            csp.deepcopy_domain(csp.domain, domain)
            if inferences is not False:
                for inference in inferences:
                    assignment[inference[0]] = None
    return False


def ac_3(csp, queue):
    """
    Propagate the constraints
    :param csp: the problem instance
    :param queue: the tuples to be checked
    :return:
    """
    while not(queue.empty()):
        (x_i, x_j) = queue.get()
        # if the variable x_i is assigned, we can skip the tuple with certainty
        # because we dont need to change the domain of an assigned variable
        if csp.assignment[x_i] is not None:
            continue
        if _revise(csp, x_i, x_j):
            if csp.domain[x_i].count(1) == 0:
                return False
            s = _neighbors(x_i, csp)
            if x_j in s:
                s.remove(x_j)
            for x_k in s:
                queue.put((x_k, x_i))
    return set() # for consistency of the general backtrack algorithm


def _revise(csp, x_i, x_j):
    """
    returns true iff we _revise the domain of X_i
    :param csp: problem instance
    :param x_i: variable
    :param x_j: variable
    :returns:
    """
    revised = False
    for x in range(len(csp.domain[x_i])):
        #ignore the impossible value
        if csp.domain[x_i][x] == 0:
            continue
        satisfy = False

        #construct the right assignment
        assignment = copy.deepcopy(csp.assignment)
        assignment[x_i] = x
        if csp.assignment[x_j] is not None:
            if csp.consistent(x_j, csp.assignment[x_j], assignment):
                satisfy = True
        else:
            for y in range(len(csp.domain[x_j])):
                # there is some y in D_x_j that satisfy the constraint
                if csp.consistent(x_j, y, assignment):
                    satisfy = True

        if not satisfy:
            #if no value in y in D_j allow (x,y) to satisfy the constraint between X_i and X_j
            csp.domain[x_i][x] = 0
            revised = True

    return revised


def _neighbors(x_i, csp):
    neighbors_set = set()
    for k in range(len(csp.domain)):
        if x_i == k:
            continue
        neighbors_set.add(k)
    return neighbors_set