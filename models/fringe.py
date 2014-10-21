__author__ = 'kinsumliu'
import queue


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