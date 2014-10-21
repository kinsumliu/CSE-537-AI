class Node:
    parent = None
    action = None
    depth = 0
    path_cost = 0

    def __init__(self, vec):
        self.vec = vec
        self.successors = set()

    def __str__(self):
        repr_str = "<"
        for i in range( len(self.vec) ):
          if i == len(self.vec) - 1:
            repr_str += str(self.vec[i])
          else:
            repr_str += str(self.vec[i]) + ","
        repr_str += ">"
        return repr_str

    def __eq__(self, other):
        if not(isinstance(other, Node)):
          return False
        if len(self.vec) == len(other.vec):
          for i in range( len(self.vec) ):
            if self.vec[i] != other.vec[i]:
              return False
          return True
        else:
          return False

    def __hash__(self):
        return hash(self.vec)

    def __lt__(self, other):
        return self.vec < other.vec

    def swap_element(self, i, j):
        t = list(self.vec)
        temp = t[i]
        t[i] = t[j]
        t[j] = temp
        return tuple(t)


# Helper functions for node to trace result

def trace(state):
      print("****       start of trace        ****")
      print("The state is ", end = "")
      print(state)
      print("Depth: "+str(state.depth) + " Path cost: "+str(state.path_cost))
      print("The path from this state to root: ")
      while state.parent is not None:
          print(state, end= "")
          print(" Action: " + state.action)
          state = state.parent
      #print the root
      print(state, end= "")
      print(" Root")
      print("****       end of trace        ****\n")

#Trace result and print heuristic value and #nodes expanded
def trace_h(state, heuristic, counter):
    print("****       start of trace        ****")
    print("The state is ", end = "")
    print(state)
    print("Depth: "+str(state.depth) + " Path cost: "+str(state.path_cost))
    print("#nodes expanded: " + str(counter))
    print("The path from this state to root: ")
    while state.parent is not None:
        print(state, end= "")
        print(" Action: " + state.action, end= "")
        print(" Heuristic: "+ str(heuristic(state)))
        state = state.parent
    #print the root
    print(state, end= "")
    print(" Root")
    print("****       end of trace        ****\n")