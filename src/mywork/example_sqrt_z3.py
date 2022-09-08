from z3 import *

def sqrt(n) :
    sqrtn = Real('sqrtn')
    s = Solver()
    s.add(n == sqrtn**2) # replace True with required declarative spec
    s.add(sqrtn >= 0)
    isSat = s.check()
    if (isSat) :
        return s.model()
    return -1
    

def neg_sqrt(n) :
    sqrtn = Real('sqrtn')
    s = Solver()
    s.add(n == sqrtn**2) # replace True with required declarative spec
    s.add(sqrtn <= 0)
    isSat = s.check()
    if (isSat) :
        return s.model()
    return -1
    
print(sqrt(9))
print(neg_sqrt(17))