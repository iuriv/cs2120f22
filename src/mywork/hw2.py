# Be sure you've done pip install z3-solver
from z3 import *


# Here's a file you can often copy as a starting 
# point on a working program to solve some problem
# of interest. Here the problem is to compute and
# return a non-negative square root of argument, n 


# Create z3 variable(s) representing the unknown
# Here, the unknown, x, is the square root of n.
def hw2():
        X, Y, Z = Bools('X Y Z')
        
        s = Solver()
        
        # 1. X ∨ Y, X ⊢ ¬Y
        # As proposition: (X \/ Y) /\ X -> ~Y
        C1 = Implies(And(Or(X,Y),X),Not(Y))
        s.add(Not(C1))
        # I believe it's not valid
        
        r = s.check()
        
        if (r == unsat):
                print("C1 is valid")
        else :
                print("Here's a counter-example: ", s.model())

hw2()