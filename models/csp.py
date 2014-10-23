__author__ = 'kinsumliu'
import queue
import copy
import random
from algos import backtrack


class CSP_BT:
    n = 0  # number of variables
    d = 0  # size of domain (same for every variable for not) d=7 :[0,1,2,3,4,5,6]
    c = 0  # number of constraints
    counter = 0
    consistent_dict = dict()

    def __init__(self, ruler):
        self.n = ruler.M
        self.d = ruler.L + 1
        self.domain = [[1 for x in range(self.d)] for x in range(self.n)]
        self.assignment = dict()
        for i in range(self.n):
            self.assignment[i] = None


    def complete(self, assignment):
        """
        check whether the assignment is complete
        :param assignment: dictionary
        :return: Boolean
        """
        for i in range(self.n):
            if assignment[i] is None:
                return False
        return True

    def select_unassigned_variable(self):
        """
        find an unassigned variable randomly
        :param assginment: current assignment
        :return: an index for the new varaible
        """
        unassigned_variables = list()
        for i in range(self.n):
            # return the first unassigned variable
            if self.assignment[i] is None:
                return i
                # unassigned_variables.append(i)
        # return unassigned_variables[random.randint(0, len(unassigned_variables) - 1)]

    def order_domain_values(self, var, assignment):
        """
        find the possible values in the domain
        :param var: the variable chosen
        :param assignment: partial assignment so far
        :return: the list of possible values for that variable
        """
        possible_values = list()
        for i in range(len(self.domain[var])):
            if self.domain[var][i] != 0:
                #if the domain value is possible
                possible_values.append(i)
        return possible_values

    def consistent(self, var, value, source_assignment):
        """
        check whether the new assignment is consistent
        :param var: the variable chosen
        :param value: the new value for the variable
        :param assignment: partial assignment so far
        :return: Boolean for consistency
        """
        # create a temporary assignment that includes assigment[var] = value
        assignment = dict()
        for i in range(0, len(source_assignment)):
            if i == var:
                assignment[i] = value
            else:
                assignment[i] = source_assignment[i]

        if tuple(assignment.items()) in self.consistent_dict:
            return self.consistent_dict[tuple(assignment.items())]

        # checking constraints x1 < x2, x2 < x3, x3 < x4, ...
        for i in range(1, len(assignment)):
            if assignment[i] is None or assignment[i - 1] is None:
                continue
            if not (assignment[i] > assignment[i - 1]):
                self.consistent_dict[tuple(assignment.items())] = False
                return False

        # store all the pairwise distances into a list
        distance_list = list()
        for i in range(self.n):
            for j in range(self.n - 1 - i):
                b = assignment[self.n - 1 - i]
                a = assignment[(self.n - 1 - i) - (j + 1)]
                if b is None or a is None:
                    continue
                distance_list.append(b-a)
        distance_list.sort()
        temp = None
        for i in range(len(distance_list)):
            if distance_list[i] == temp:
                #there is duplicate element in the sorted list
                self.consistent_dict[tuple(assignment.items())] = False
                return False
            temp = distance_list[i]

        # checking by direct comparison
        # for i in range(self.n):
        #     for j in range(self.n - 1 - i):
        #         b = assignment[self.n - 1 - i]
        #         a = assignment[(self.n - 1 - i) - (j + 1)]
        #         if b is None or a is None:
        #             continue
        #         for k in range(self.n):
        #             for l in range(self.n - 1 - k):
        #                 if i == k and j == l or k < i or ( k == i and j > l ):
        #                     continue
        #                 d = assignment[self.n - 1 - k]
        #                 c = assignment[(self.n - 1 - k) - (l + 1)]
        #                 if d is None or c is None:
        #                     continue
        #                 if d - c == b - a:
        #                     self.consistent_dict[tuple(assignment.items())] = False
        #                     return False

        self.consistent_dict[tuple(assignment.items())] = True
        return True

    def conflicted(self, assignment):
        """
        find out all conflicted variables and return one randomly
        :param assignment: current assignment
        :return: one conflicted variable
        """
        conflicted_variables = list() # store all the variables that impose conflicts
        conflicted_values = list() # store all the values that impose conflicts

        # store all the pairwise distances into a list
        distance_list = list()
        for i in range(self.n):
            for j in range(self.n - 1 - i):
                b = assignment[self.n - 1 - i]
                a = assignment[(self.n - 1 - i) - (j + 1)]
                distance_list.append(abs(b-a))
                if not b > a:
                    # checking constraints x1<x2<x3<...<...
                    if not self.n - 1 - i in conflicted_variables:
                        conflicted_variables.append(self.n - 1 - i)
                    if not (self.n - 1 - i) - (j + 1) in conflicted_variables:
                        conflicted_variables.append((self.n - 1 - i) - (j + 1))
        distance_list.sort()

        temp = None
        for i in range(len(distance_list)):
            if distance_list[i] == temp:
                # there is duplicate element in the sorted list
                if not i in conflicted_values:
                    conflicted_values.append(distance_list[i])
            temp = distance_list[i]

        for i in range(self.n):
            for j in range(self.n - 1 - i):
                b = assignment[self.n - 1 - i]
                a = assignment[(self.n - 1 - i) - (j + 1)]
                if abs(b-a) in conflicted_values:
                    if not self.n - 1 - i in conflicted_variables:
                        conflicted_variables.append(self.n - 1 - i)
                    if not (self.n - 1 - i) - (j + 1) in conflicted_variables:
                        conflicted_variables.append((self.n - 1 - i) - (j + 1))

        # we dont want to change the first and last variable
        if 0 in conflicted_variables:
            conflicted_variables.remove(0)
        if len(assignment)-1 in conflicted_variables:
            conflicted_variables.remove(len(assignment)-1)

        return conflicted_variables[random.randint(0, len(conflicted_variables)-1)]

    def inference(self, var, value):
        """
        find out the inference for the new assignment
        :param var:
        :param value:
        :returns: a list of (var, value) tuples
        """
        temp = set()
        return temp

    def deepcopy_domain(self, domain, other):
        for i in range(len(other)):
            for j in range(len(other[i])):
                domain[i][j] = other[i][j]


    def minimize_conflicts(self, var, current):
        """
        find out the value that minimize the number of conflicts
        :param var: variable that we are looking at
        :param current:  current assignment
        :return: value
        """
        min_conflict = None
        conflict_dict = dict()
        assignment = copy.deepcopy(current)

        for d_i in range(self.d):
            if d_i == current[var]:
                continue
            assignment[var] = d_i
            conflicts_counter = 0

            # checking constraints x1 < x2, x2 < x3, x3 < x4, ...
            for i in range(1, len(assignment)):
                if not assignment[i] > assignment[i-1]:
                    conflicts_counter += 1

            # checking conflicts for equal distance
            distance_list = list()
            for i in range(self.n):
                for j in range(self.n - 1 - i):
                    b = assignment[self.n - 1 - i]
                    a = assignment[(self.n - 1 - i) - (j + 1)]
                    distance_list.append(abs(b-a))
            distance_list.sort()
            temp = None
            for i in range(len(distance_list)):
                if distance_list[i] == temp:
                    #there is duplicate element in the sorted list
                    conflicts_counter += 1
                temp = distance_list[i]

            if min_conflict is None or conflicts_counter < min_conflict:
                min_conflict = conflicts_counter

            conflict_dict[d_i] = conflicts_counter

        # store the values that minimize #conflicts in a list
        values = list()
        for d_i in range(self.d):
            if d_i == current[var]:
                continue
            if conflict_dict[d_i] == min_conflict:
                values.append(d_i)
        return values[random.randint(0, len(values)-1)]


class CSP_BT_MRV(CSP_BT):
    def __init__(self, ruler):
        self.n = ruler.M
        self.d = ruler.L + 1
        self.domain = [[1 for x in range(self.d)] for x in range(self.n)]

        #node consistency
        for i in range(self.n):
            if i == 0:
                temp_list = [0 for x in range(self.d)]
                temp_list[0] = 1
                self.domain[i] = temp_list
            elif i == self.n-1:
                temp_list = [0 for x in range(self.d)]
                temp_list[self.d-1] = 1
                self.domain[i] = temp_list
            else:
                temp_list = [1 for x in range(self.d)]
                for j in range(i + 1, self.n):
                    temp_list[self.d - self.n + j] = 0
                self.domain[i] = temp_list

        #initialize the assignment
        self.assignment = dict()
        for i in range(self.n):
            self.assignment[i] = None

    def select_unassigned_variable(self):
        """
        find an unassigned variable based on minimum-remaining-values / most constrained variable
        :param assginment: current assignment
        :return: an index for the new varaible
        """
        index = -1
        counter = self.d + 1
        domain = [[1 for x in range(self.d)] for x in range(self.n)]
        self.deepcopy_domain(domain, self.domain)

        # update the domain temporarily
        for i in range(len(domain)):
            if self.assignment[i] is not None:
                #already assigned
                continue
            for j in range(len(domain)):
                if domain[i][j] == 0:
                    continue
                if not(self.consistent(i,j, self.assignment)):
                    domain[i][j] = 0

        #MRV
        for i in range(self.n):
            if self.assignment[i] is None and domain[i].count(1) < counter:  # minimum remaining values in the domain[i]
                counter = domain[i].count(1)
                index = i
        return index


class CSP_BT_MRV_FC(CSP_BT_MRV):
    def inference(self, var, value):
        """
        find out the inference for the new assignment
        :param var:
        :param value:
        :returns: a list of (var, value) tuples
        """
        inferenced = set()
        for i in range(len(self.domain)):
            if i == var or self.assignment[i] is not None:
                #already assigned
                continue
            for j in range(len(self.domain[i])):
                if self.domain[i][j] == 0:
                    continue
                if not(self.consistent(i, j, self.assignment)):
                    self.domain[i][j] = 0
            if self.domain[i].count(1) == 0:
                #no possible value for variable X_i
                return False
            elif self.domain[i].count(1) == 1:
                #only one possible value, add it to assignment soon
                inferenced.add((i, self.domain[i].index(1)))
        return inferenced


class CSP_BT_MRV_CP(CSP_BT_MRV):
    def inference(self, var, value):
        q = queue.Queue()
        for j in range(len(self.domain)):
            # neighbors and unassigned
            if j != var and self.assignment[j] is None:
                q.put((j, var))
        #contraint propagation
        return backtrack.ac_3(self, q)