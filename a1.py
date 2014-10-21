from algos import search
from models.node import Node, trace
from models.problems.jar_filling import JarFilling
from models.fringe import FringeQueue, FringeStack

#Initialize the problem
problem = JarFilling(Node((0, 0)))

#Apply the general tree search algorithms
goal_state_BFS = search.graph_search(problem, FringeQueue())
goal_state_DFS = search.tree_search(problem, FringeStack())
goal_state_IDS = search.iterative_deepening_search(problem)

#Trace result
print("Tracing the result of BFS")
trace(goal_state_BFS)
print("Tracing the result of DFS")
trace(goal_state_DFS)
print("Tracing the result of IDS")
trace(goal_state_IDS)