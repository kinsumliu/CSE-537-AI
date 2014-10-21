"""
It provides different search methods for a data structure that involves nodes.
functions: tree_search, graph_search, depth_limited_search, recursive_dls, iterative_deepening_search
"""


def tree_search(problem, fringe):
    """
    Search for goal state in a tree
    :param problem:
    :param fringe:
    :return: a solution or failure
    """
    fringe.insert(problem.initial_node)
    while True:
        if fringe.empty():
            # Fails to find the goal state
            return False
        s = fringe.remove_front()
        if problem.goal_test(s):
            return s
        fringe.insert_all(_expand(s, problem))


def graph_search(problem, fringe):
    """
    Search for goal state in a graph
    :param problem:
    :param fringe:
    :return: a solution or failure
    """
    closed = set()
    fringe.insert(problem.initial_node)
    while True:
        if fringe.empty():
            # Fails to find the goal state
            return False
        s = fringe.remove_front()
        if problem.goal_test(s):
            return s
        if not (s in closed):
            closed.add(s)  # Avoid loops
            fringe.insert_all(_expand(s, problem))


def depth_limited_search(problem, limit):
    """
    Recursive implementation of depth-limited tree search
    :param problem:
    :param limit:
    :return:
    """
    return _recursive_dls(problem.initial_node, problem, limit)


def _recursive_dls(state, problem, limit):
    cutoff_occurred = False
    if problem.goal_test(state):
        return state
    elif state.depth == limit:
        # nodes at depth limit are treated as if they have no successors
        return problem.cutoff
    else:
        for s in _expand(state, problem):
            result = _recursive_dls(s, problem, limit)
            if result == problem.cutoff:
                cutoff_occurred = True
            elif result is not False:
                return result
    if cutoff_occurred:
        return problem.cutoff
    else:
        return False


def iterative_deepening_search(problem):
    """
    Repeated applies depth limited search
    :param problem:
    :return:
    """
    depth = 0
    while depth < float("infinity"):
        result = depth_limited_search(problem, depth)
        if result != problem.cutoff:
            return result
        depth += 1


def _expand(state, problem):
    """
    Return a set of successor states
    """
    successors = set()
    for (action, result) in _successor_fn(problem, state):
        s = result
        s.parent = state
        s.action = action
        s.path_cost = state.path_cost + problem.step_cost(state, action, s)
        s.depth = state.depth + 1
        successors.add(s)
    if hasattr(problem, 'expand_counter'):
        problem.expand_counter += len(successors)
    return successors


def _successor_fn(problem, state):
    return problem.succ(state)
