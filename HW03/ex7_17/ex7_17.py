#!/usr/bin/python

"""
Note This calculates the Jacobian Matrix correctly, but I was not able to get it to
solve for S and I.  It turns out that the equilibrium points are I = 0 and S = c (any constant).
Perhaps S equaling any constant makes it difficult for Sympy to find.
"""

import sympy as sy
from sympy.abc import a, b, S, I

X = sy.Matrix([-a*S*I,
               a*S*I - b*I])
print("\nDiff eqs:\n" + str(X[0]) + "\n" + str(X[1]) + "\n")

Y = sy.Matrix([S, I])
print("variables: " + str(Y[0]) + ", " + str(Y[1]) + "\n")

jacobian_matrix = X.jacobian(Y)

print("Jacobian Matrix with a, b as a symbolic variables: \n" + str(jacobian_matrix) + "\n")

# Part 1: find all equilibrium points

solutions_to_print = sy.solve(X, Y)
print("equilibrium points (x, y): \n" + str(solutions_to_print) + "\n")

# Part 2: Calculate the Jacobian matrix at the equilibrium point
# where x > 0 and y > 0.  (I will make a and b some concrete value)
value_of_a = 1.0
value_of_b = 1.0
X = X.subs([(a, value_of_a), (b, value_of_b)])
jacobian_matrix = X.jacobian(Y)

print("Jacobian Matrix with a, b as literals: \n" + str(jacobian_matrix) + "\n")


sols = sy.solve(X, Y)

print("solution(s) (a={0:.2f}, b={1:.2f}):".format(value_of_a, value_of_b))
print(str(sols) + "\n")


'''
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
'''