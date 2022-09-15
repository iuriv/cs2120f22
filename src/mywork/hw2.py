# Be sure you've done pip install z3-solver
from telnetlib import X3PAD
from z3 import *


# Here's a file you can often copy as a starting 
# point on a working program to solve some problem
# of interest. Here the problem is to compute and
# return a non-negative square root of argument, n 
s = Solver()

def valCheck(number):
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C" + str(number) +" is valid") 
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()

def hw2():
    
    
    # Create z3 variable(s) representing the unknown
    X, Y, Z = Bools('X Y Z')
    
    # 1. X ∨ Y, X ⊢ ¬Y 
    # As proposition in PL: ((X \/ Y) /\ X) -> ~Y
    C1 = Implies(And(Or(X,Y),X),Not(Y))
    
    s.add(Not(C1))
    # I believe it's not valid
    
    valCheck(1)
    
    # 2. X, Y ⊢ X ∧ Y
    # As proposition in PL: (X /\ Y) -> (X /\ Y)
    C2 = Implies(And(X,Y),And(X,Y))
    
    s.add(Not(C2))
    # I believe it's valid
    
    valCheck(2)
    
    # 3. X ∧ Y ⊢ X
    # As proposition in PL: (X /\ Y) -> X
    C3 = Implies(And(X,Y),X)
    
    s.add(Not(C3))
    # I believe it's valid
    
    valCheck(3)
    
    # 4. X ∧ Y ⊢ Y
    # As proposition in PL: (X /\ Y) -> Y
    C4 = Implies(And(X,Y),Y)
    
    s.add(Not(C4))
    # I believe it's valid
    
    valCheck(4)
    
    # 5. ¬¬X ⊢ X
    # As proposition in PL: !(!X) -> X
    C5 = Implies(Not(Not(X)),X)
    
    s.add(Not(C5))
    # I believe it's valid
    
    valCheck(5)
    
    # 6. ¬(X ∧ ¬X)
    # As proposition in PL: !(X /\ !X)
    C6 = Not(And(X,Not(X)))
    
    s.add(Not(C6))
    # I believe it's valid
    
    valCheck(6)
    
    # 7. X ⊢ X ∨ Y
    # As proposition in PL: X -> X \/ Y
    C7 = Implies(X,Or(X,Y))
    
    s.add(Not(C7))
    # I believe it's valid
    
    valCheck(7)


hw2()