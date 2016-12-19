#!/usr/bin/python

import sympy as sy
from sympy.abc import x, y, r

X = sy.Matrix([-x+r*x*y-(x*x),
               y*(1-y)])
print("\nDiff eqs:\n" + str(X[0]) + "\n" + str(X[1]) + "\n")

Y = sy.Matrix([x, y])
print("variables: " + str(Y[0]) + ", " + str(Y[1]) + "\n")

jacobian_matrix = X.jacobian(Y)

print("Jacobian Matrix with r as a symbolic variable:" + str(jacobian_matrix) + "\n")

# Part 1: find all equilibrium points

solutions_to_print = sy.solve(X, Y)
print("equilibrium points (x, y): \n" + str(solutions_to_print) + "\n")

# note that x >= 0, y >=0, and r > 1
# Part 2: Calculate the Jacobian matrix at the equilibrium point
# where x > 0 and y > 0.  (I will make r some concrete value)
value_of_r = 4
X = X.subs([(r, value_of_r)])
jacobian_matrix = X.jacobian(Y)

sols = sy.solve(X, Y)

solutions = []
for sol in sols:
    if sol[0] > 0 and sol[1] > 0:
        solutions.append(sol)

print("solution(s) with x>0, y>0, r={0:d}:".format(value_of_r))
print(str(solutions) + "\n")

print("Jacobian Matrix with r={0:d}".format(value_of_r))
print(str(jacobian_matrix) + "\n")

# Part 3: Calculate the eigenvalues of the matrix obtained above
value_of_x = solutions[0][0]
value_of_y = solutions[0][1]

matrix = jacobian_matrix.subs([(x, value_of_x), (y, value_of_y)])
print("new matrix:")
print(matrix)

eigenvalues = matrix.eigenvals()
print("eigenvalues: " + str(eigenvalues) + "\n")

# Part 4: Comment on the stability of the equilibrium point

dominant_eigen_value = 0
for key in eigenvalues:
    if abs(key) > abs(dominant_eigen_value):
        dominant_eigen_value = key
print("dominan eigen value: " + str(dominant_eigen_value) + "\n")

if dominant_eigen_value > 0:
    print("because the dominant eigenvalue > 0, the equilibrium point is STABLE")
elif dominant_eigen_value < 0:
    print("because the dominant eigenvalue < 0, the equilibrium point is UNSTABLE")
else:
    print("because the dominant eigenvalue == 0, the equilibrium point may be neutral")

"""
Output of program:
ex7_16.py

Diff eqs:
r*x*y - x**2 - x
y*(-y + 1)

variables: x, y

Jacobian Matrix with r as a symbolic variable:Matrix([[r*y - 2*x - 1, r*x], [0, -2*y + 1]])

equilibrium points (x, y):
[(-1, 0), (0, 0), (0, 1), (r - 1, 1)]

solution(s) with x>0, y>0, r=4:
[(3, 1)]

Jacobian Matrix with r=4
Matrix([[-2*x + 4*y - 1, 4*x], [0, -2*y + 1]])

new matrix:
Matrix([[-3, 12], [0, -1]])
eigenvalues: {-3: 1, -1: 1}

dominan eigen value: -3

because the dominant eigenvalue < 0, the equilibrium point is UNSTABLE
"""
