from z3 import *

d = Real('x')
y = Real('y')

solve(x**2 + y**2 > 3, x**3 + y < 5)