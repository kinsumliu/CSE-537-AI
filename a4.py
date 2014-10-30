__author__ = 'kinsumliu'
import time
from algos import backtrack, min_conflicts
from models.problems.golomb_ruler import Golomb_Ruler
from models.csp import CSP_BT, CSP_BT_MRV, CSP_BT_MRV_FC, CSP_BT_MRV_CP

# The set of Golomb Rulers
# ruler = Golomb_Ruler(4, 6)
# ruler = Golomb_Ruler(5, 11)
ruler = Golomb_Ruler(6, 17)
# ruler = Golomb_Ruler(7, 25)
# ruler = Golomb_Ruler(8, 34)
# ruler = Golomb_Ruler(9, 44)
# ruler = Golomb_Ruler(10, 55)
# ruler = Golomb_Ruler(11, 72)

csp_bt = CSP_BT(ruler)
csp_mrv = CSP_BT_MRV(ruler)
csp_mrv_fc = CSP_BT_MRV_FC(ruler)
csp_mrv_cp = CSP_BT_MRV_CP(ruler)


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('%s function took %0.3f ms' % (f.__name__, (time2 - time1) * 1000.0))
        print("****        end of trace        *****")
        print('\n')
        return ret

    return wrap


@timing
def algoTime(csp):
    print("****        start of trace        *****")
    print("Running " + csp.__class__.__name__ + " algorithm")
    x = backtrack.backtracking_search(csp)
    print("No of consistency checks: "+str(csp.counter))
    if x is not False:
        for i in range(len(x)):
            print("X" + str(i) + ": " + str(x[i]))
    else:
        print("No solution")


@timing
def algoTime_mc(csp, max_step):
    print("****        start of trace        *****")
    (x, steps) = min_conflicts.min_conflicts(csp, max_step)
    print("Running Minimum Conflicts algorithm for Iterative Improvement")
    if x is not False:
        for i in range(len(x)):
            print("X" + str(i) + ": " + str(x[i]))
        print("Steps needed: " + str(steps))
    else:
        print("No solution is found yet")

print("\n")
print("This is the implementation of CSP for the problem Golomb Ruler \n")
print ("Golomb Ruler - M: " + str(ruler.M) + ", L: " + str(ruler.L) + "\n")

algoTime(csp_bt)
algoTime(csp_mrv)
algoTime(csp_mrv_fc)
algoTime(csp_mrv_cp)
algoTime_mc(csp_bt, 100000)

# reference note
# X = {X0, X1, X2, X3}
# D = {D0, D1, D2, D3} Di = {0,1,2,3,4,5,6}
# x3 - x2 = A,
# x3 - x1 = B,
# x3 - x0 = C,
# x2 - x1 = D,
# x2 - x0 = E,
# x1 - x0 = F,
# C = { x1 < x2, x2 < x3, x3 < x4
# A != B, A != C, A != D, A != E, A != F,
# B != C, B != D, B != E, B != F,
# C != D, C != E, C != F,
# D != E, D != F,
# E != F}
# assignment = {Xi = vi, Xj = vj}