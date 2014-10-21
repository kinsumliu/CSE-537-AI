from algos import search
from models.node import Node, trace_h
from models.problems.sliding_tile import SlidingTile
from models.fringe import FringePQueue

#Initialize the problem
problem = SlidingTile(Node((-1,-1,-1, 0, 1, 1, 1)))
problem1 = SlidingTile(Node((-1,-1,-1, 0, 1, 1, 1)))
problem2 = SlidingTile(Node((-1,-1,-1, 0, 1, 1, 1)))
problem3 = SlidingTile(Node((-1,-1,-1, 0, 1, 1, 1)))

#Initialize the fringe
#The parameter for the fringe defines which heuristic function to use
fringe_h0 = FringePQueue(0)
fringe_h1 = FringePQueue(1)
fringe_h2 = FringePQueue(2)
fringe_h3 = FringePQueue(3)

#Apply the general tree search algorithm
goal_state_h0 = search.tree_search(problem, fringe_h0)
goal_state_h1 = search.tree_search(problem1, fringe_h1)
goal_state_h2 = search.tree_search(problem2, fringe_h2)
goal_state_h3 = search.tree_search(problem3, fringe_h3)

#Trace result
print("Tracing the result of h0")
trace_h(goal_state_h0, fringe_h0.heuristic, problem.expand_counter)
print("Tracing the result of h1")
trace_h(goal_state_h1, fringe_h1.heuristic, problem1.expand_counter)
print("Tracing the result of h2")
trace_h(goal_state_h2, fringe_h2.heuristic, problem2.expand_counter)
print("Tracing the result of h3")
trace_h(goal_state_h3, fringe_h3.heuristic, problem3.expand_counter)