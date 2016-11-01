#!/usr/bin/python
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
"""
exercise 5.12
Study the asymptotic behavior of the following three-dimensional
difference equation model by calculating its eigenvalues and eigenvectors
"""
print("exercise 5.12")
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

print("eigenvectors: \n" + str(eigenvectors) + "\n")

eigenvectors_inverse = np.linalg.inv(eigenvectors)
print("eigenvectors inverse: ")
print(str(eigenvectors_inverse) + "\n")

w_0 = np.matrix([[.0001],
                 [.001],
                 [.01]])
iterations = 30

xs = []
ys = []
zs = []

for n in range(1, iterations + 1):
    lamdas_to_the_nth_power = [eigenval**n for eigenval in eigenvalues]
    diagonal_lamdas = np.diag(lamdas_to_the_nth_power)
    w_n = eigenvectors * diagonal_lamdas * eigenvectors_inverse * w_0
    print("w at " + str(n))
    print(w_n)
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