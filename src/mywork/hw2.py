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
    
    # 8. Y ⊢ X ∨ Y
    # As proposition in PL: Y -> X \/ Y
    C8 = Implies(Y,Or(X,Y))
    
    s.add(Not(C8))
    # I believe it's valid
    
    valCheck(8)
    
    # 9. X → Y, ¬X ⊢ ¬ Y
    # As proposition in PL: (X -> Y) /\ (!X -> !Y)
    C9 = And(Implies(X,Y),Implies(Not(X),Not(Y)))
    
    s.add(Not(C9))
    # I believe it's not valid
    
    valCheck(9)
    
    # 10. X → Y, Y → X ⊢ X ↔ Y 
    # As proposition in PL: ((x -> Y) /\ (Y -> X)) -> (X == Y)
    C10 = Implies(And(Implies(X,Y),Implies(Y,X)),(X == Y))
    
    s.add(Not(C10))
    # I believe it's valid
    
    valCheck(10)
    
    # 11. X ↔ Y ⊢ X → Y
    # As proposition in PL: (X == Y) -> (X -> Y)
    C11 = Implies((X == Y), Implies(X,Y))
    
    s.add(Not(C11))
    # I believe it's valid
    
    valCheck(11)
    
    # 12. X ↔ Y ⊢ Y → X 
    # As proposition in PL: (X == Y) -> (Y -> X)
    C12 = Implies((X == Y), Implies(Y,X))
    
    s.add(Not(C12))
    # I believe it's valid
    
    valCheck(12)
    
    # 13. X ∨ Y, X → Z, Y → Z ⊢ Z
    # As proposition in PL: ((X \/ Y) /\ (X -> Z) /\ (Y -> Z)) -> Z
    C13 = Implies(And(And(Or(X,Y),Implies(X,Z)),Implies(Y,Z)),Z)
    
    s.add(Not(C13))
    # I believe it's valid
    
    valCheck(13)
    
    # 14. X → Y, Y ⊢ X 
    # As proposition in PL: ((X -> Y) /\ Y) -> X
    C14 = Implies(And(Implies(X,Y),Y),X)
    
    s.add(Not(C14))
    # I believe it's not valid
    
    valCheck(14)
    
    # 15. X → Y, X ⊢ Y
    # As proposition in PL: ((X -> Y) /\ X) -> Y
    C15 = Implies(And(Implies(X,Y),X),Y)
    
    s.add(Not(C15))
    # I believe it's valid
    
    valCheck(15)
    
    # 16. X → Y, Y → Z ⊢ X → Z
    # As proposition in PL: ((X -> Y) /\ (Y -> Z)) -> (X -> Z)
    C16 = Implies(And(Implies(X,Y),Implies(Y,Z)),Implies(X,Z))
    
    s.add(Not(C16))
    # I believe it's valid
    
    valCheck(16)
    
    # 17. X → Y ⊢ Y → X
    # As proposition in PL: (X -> Y) -> (Y -> X)
    C17 = Implies(Implies(X,Y), Implies(Y,X))
    
    s.add(Not(C17))
    # I believe it's not valid
    
    valCheck(17)
    
    # 18. X → Y ⊢ ¬Y → ¬X
    # As proposition in PL: (X -> Y) -> (!Y -> !X)
    C18 = Implies(Implies(X,Y), Implies(Not(Y),Not(X)))
    
    s.add(Not(C18))
    # I believe it's valid
    
    valCheck(18)
    
    # 19. ¬(X ∨ Y) ↔ ¬X ∧ ¬Y
    # As proposition in PL: (!(X \/ Y) == (!X /\ !Y))
    C19 = (Not(Or(X,Y)) == (And(Not(X),Not(Y))))
    
    s.add(Not(C19))
    # I believe it's valid
    
    valCheck(19)
    
    # 20. ¬(X ∧ Y) ↔ ¬X ∨ ¬Y
    # As proposition in PL: ((!(X /\ Y) == (!X /\ !Y))
    C20 = (Not(And(X,Y)) == (Or(Not(X),Not(Y))))
    
    s.add(Not(C20))
    # I believe it's not valid
    
    valCheck(20)

hw2()