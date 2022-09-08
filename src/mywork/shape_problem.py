# Be sure you've done pip install z3-solver
from z3 import *


# Here's a file you can often copy as a starting 
# point on a working program to solve some problem
# of interest. Here the problem is to compute and
# return a non-negative square root of argument, n 


# Create z3 variable(s) representing the unknown
# Here, the unknown, x, is the square root of n.
triangle, square, circle = Reals('triangle square circle')

s = Solver()

C = And(
        triangle + square + circle == 10,
        circle + square - triangle == 6,
        circle + triangle - square == 4)

s.add(C)

if (s.check() == sat) :
    print(s.model())