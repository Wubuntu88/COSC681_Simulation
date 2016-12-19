#!/usr/bin/python
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def print_asymptotic_behaviour_given_dominant_eigenvalue(the_eigen_val):
    if the_eigen_val > -.0001 or the_eigen_val < .0001:
        print("Given |{0:.2f}| = 1; the system is stable and may converge to a non-zero equilibrium\n"
              .format(the_eigen_val))
    elif the_eigen_val > 1.0:
        print("Given |{0:.2f}| > 1; the system is unstable and diverges to infinity\n"
              .format(the_eigen_val))
    elif the_eigen_val < 1.0:
        print("Given |{0:.2f}| < 1; the system is stable and converges to the origin\n"
              .format(the_eigen_val))
    else:
        print("Error, this code should not be reached\n")

"""
exercise 5.12
Study the asymptotic behavior of the following three-dimensional
difference equation model by calculating its eigenvalues and eigenvectors
"""
print("exercise 5.12")
# mtrx is the three dimensional difference equation model in matrix form
mtrx = np.matrix([[1, -1, 0],
                  [-1, -3, 1],
                  [0, 1, 1]])
print("matrix:\n" + str(mtrx) + "\n")

eigenvalues, eigenvectors = np.linalg.eig(mtrx)
print("eigenvalues: \n" + str(eigenvalues) + "\n")

abs_val_eigenvalues = abs(eigenvalues)
print("absolute values of eigenvalues: \n" + str(abs_val_eigenvalues) + "\n")
index_of_dominant_eigenvalue = abs_val_eigenvalues.argmax()
print("dominant eigenvalue: " +
      str(eigenvalues[index_of_dominant_eigenvalue]) + "\n")

dom_eig_val = eigenvalues[index_of_dominant_eigenvalue]
print_asymptotic_behaviour_given_dominant_eigenvalue(dom_eig_val)

print("eigenvectors: \n" + str(eigenvectors) + "\n")

eigenvectors_inverse = np.linalg.inv(eigenvectors)
print("eigenvectors inverse: ")
print(str(eigenvectors_inverse) + "\n")

# initial values of the matrix
w_0 = np.matrix([[.0001],
                 [.001],
                 [.01]])
ITERATIONS = 30

xs = []
ys = []
zs = []

for n in range(1, ITERATIONS + 1):
    lamdas_to_the_nth_power = [eigenval**n for eigenval in eigenvalues]
    diagonal_lamdas = np.diag(lamdas_to_the_nth_power)
    w_n = eigenvectors * diagonal_lamdas * eigenvectors_inverse * w_0
    # print("w at " + str(n))
    # print(w_n)
    xs.append(w_n.item((0, 0)))
    ys.append(w_n.item((1, 0)))
    zs.append(w_n.item((2, 0)))

"""
Plotting
"""
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(xs, ys, zs, c='g', marker='o', s=150)

plt.title('Asymptotic Behavior as t -> inf', fontsize=25)
ax.set_xlabel('X Label', fontsize=18)
ax.set_ylabel('Y Label', fontsize=18)
ax.set_zlabel('Z Label', fontsize=18)
plt.show()
"""
Output of program:
exercise 5.12
matrix:
[[ 1 -1  0]
 [-1 -3  1]
 [ 0  1  1]]

eigenvalues:
[-3.44948974  1.          1.44948974]

absolute values of eigenvalues:
[ 3.44948974  1.          1.44948974]

dominant eigenvalue: -3.44948974278

Given |-3.45| = 1; the system is stable and may converge to a non-zero equilibrium
eigenvectors:
[[  2.14186495e-01  -7.07106781e-01  -6.73887339e-01]
 [  9.53020614e-01   1.33504240e-17   3.02905447e-01]
 [ -2.14186495e-01  -7.07106781e-01   6.73887339e-01]]
eigenvectors inverse:
[[  2.14186495e-01   9.53020614e-01  -2.14186495e-01]
 [ -7.07106781e-01  -6.57399882e-17  -7.07106781e-01]
 [ -6.73887339e-01   3.02905447e-01   6.73887339e-01]]
"""