__author__ = 'kinsumliu'
from models.node import Node
from models.problem import Problem


class JarFilling(Problem):
    #setting
    cap_x = 4
    cap_y = 3
    goal = 2
    cutoff = 20

    def succ(self, state):
        x = state.vec[0]
        y = state.vec[1]
        cap_x = self.cap_x
        cap_y = self.cap_y

        #create the set of succ
        successors = {
          ("EmptyX" , Node(( 0     ,y))),
          ("EmptyY" , Node(( x     ,0))),
          ("FillX"  , Node(( cap_x ,y))),
          ("FillY"  , Node(( x     ,cap_y))),
        }

        if x+y < cap_y:
            successors.add( ("X->Y", Node((0, x+y))) ) # add all x into y
        else:
            successors.add( ("X->Y", Node((x-(3-y), cap_y))) ) # fill up y with some x

        if x+y < cap_x:
            successors.add( ("Y->X", Node((x+y, 0))) ) # add all y into x
        else:
            successors.add( ("Y->X", Node((cap_x, y-(4-x)))) ) # fill up x with some y

        return successors

    def goal_test(self, state):
        if state.vec[0] == self.goal:
            return True
        else:
            return False

    def step_cost(self, state, action, s):
        return 1