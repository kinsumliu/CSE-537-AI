__author__ = 'kinsumliu'
import queue
import heapq


class Fringe:
    def __init__(self):
        pass

    def __str__(self):
        repr_str = "The current fringe: \n"
        size = self.q.qsize()
        tempq = queue.Queue()
        for i in range(size):
          repr_str += "<"
          s = self.q.get()
          tempq.put(s)
          vec = s.vec

          for j in range(len(vec)):
            if j == len(vec) - 1:
              repr_str += str(vec[j])
            else:
              repr_str += str(vec[j]) + ","
          repr_str += ">\n"
        self.q = tempq
        return repr_str

    def insert(self, state):
        pass

    def empty(self):
        if self.q.empty():
            return True
        else:
            return False

    def remove_front(self):
        pass

    def insert_all(self, state):
        pass


class FringeQueue(Fringe):
    def __init__(self):
        self.q = queue.Queue()  # Create an empty FIFO queue

    def insert(self, state):
        self.q.put(state)

    def remove_front(self):
        return self.q.get()

    def insert_all(self, states):
        for s in states:
            if s in self.q.queue:
                continue
            else:
                self.q.put(s)


class FringeStack(Fringe):

    def __init__(self):
        self.q = queue.LifoQueue() #create an empty FIFO queue
        self.path_dict = dict()
        self.path_depth = 0

    def insert(self, state):
        self.q.put(state)
        self.path_dict[state.depth] = state

    def remove_front(self):
        s = self.q.get()
        self.path_depth = s.depth
        self.path_dict[s.depth] = s
        return s

    def insert_all(self, states):
        for s in states:
            for i in range(self.path_depth+1):
                if s == self.path_dict[i]:
                    break
            else:
                self.q.put(s)


#Define the fringe for sliding-tile puzzle
class FringePQueue(Fringe):
    heuristic_method = 0

    def __init__(self, h):
        self.hp = []  #initialize an empty heap
        self.heuristic_method = h

    def __str__(self):
        repr_str = "The current fringe: \n"
        for i in range( len(self.hp) ):
            repr_str += "(" + str(self.hp[i][0]) + ", <"
            for j in range( len(self.hp[i][1].vec) ):
                if j == len(self.hp[i][1].vec) - 1:
                    repr_str += str(self.hp[i][1].vec[j])
                else:
                    repr_str += str(self.hp[i][1].vec[j]) + ","
            repr_str += ">)\n"
        return repr_str

    def insert(self, state):
        state.h = self.heuristic(state)
        heapq.heappush(self.hp, (state.path_cost + state.h, state))

    def empty(self):
        if len(self.hp):
            return False
        else:
            return True

    def remove_front(self):
        return heapq.heappop(self.hp)[1]

    def insert_all(self, states):
        for s in states:
            s.h = self.heuristic(s)
            fringe_element = (s.path_cost + s.h, s)
            if not(fringe_element in self.hp):
                heapq.heappush(self.hp, fringe_element)  # if state is not in fringe already

    def heuristic(self, state):
        # h (n) <= h*(n)
        if self.heuristic_method == 1:
            #first heuristic
            vec = state.vec
            first_white = vec.index(1)
            no_black_before_white = 0
            for i in range(first_white):
                if vec[i] == -1:
                    #if it is black
                    no_black_before_white += 1
            return no_black_before_white

        elif self.heuristic_method == 2:
            # Second heuristic
            vec = state.vec
            last_white = 0
            for i in range(len(vec)):
                if vec[i] == 1:
                    #if it is white, update index
                    last_white = i
            return min(abs(last_white - 3), (last_white - 2))

        elif self.heuristic_method == 3:
            vec = state.vec
            last_white = 0
            for i in range(len(vec)):
                if vec[i] == 1:
                    #if it is white, update index
                    last_white = i
            no_black_before_last_white = 0
            for i in range(last_white):
                if vec[i] == -1:
                #if it is black
                    no_black_before_last_white += 1
            return no_black_before_last_white

        else:
            #no heuristic
            return 0