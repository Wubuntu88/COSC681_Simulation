#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import random
print("exercise 5.13")
one_third = 1.0/3.0
mtrx = np.matrix([[one_third, one_third, 0, 0, one_third],
                  [one_third, one_third, one_third, 0, 0],
                  [0, one_third, one_third, one_third, 0],
                  [0, 0, one_third, one_third, one_third],
                  [one_third, 0, 0, one_third, one_third]])
print("matrix:\n" + str(mtrx) + "\n")

the_min = -10000
the_max = 10000
initialOpinions = {
    'a': random.randint(the_min, the_max),
    'b': random.randint(the_min, the_max),
    'c': random.randint(the_min, the_max),
    'd': random.randint(the_min, the_max),
    'e': random.randint(the_min, the_max)
}

initialOpinionMatrix = np.matrix([[initialOpinions['a']],
                                  [initialOpinions['b']],
                                  [initialOpinions['c']],
                                  [initialOpinions['d']],
                                  [initialOpinions['e']]])

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

iterations = 10

a = []
b = []
c = []
d = []
e = []

for n in range(1, iterations + 1):
    lamdas_to_the_nth_power = [eigenval ** n for eigenval in eigenvalues]
    diagonal_lamdas = np.diag(lamdas_to_the_nth_power)
    w_n = eigenvectors * diagonal_lamdas * eigenvectors_inverse * initialOpinionMatrix
    print("w at " + str(n))
    print(w_n)
    a.append(w_n.item(0))
    b.append(w_n.item(1))
    c.append(w_n.item(2))
    d.append(w_n.item(3))
    e.append(w_n.item(4))

"""
Plotting
"""
the_ns = list(range(1, iterations+1))
plt.plot(the_ns, a, c='r', linewidth=3)
plt.plot(the_ns, b, c='g', linewidth=3)
plt.plot(the_ns, c, c='b', linewidth=3)
plt.plot(the_ns, d, c='m', linewidth=3)
plt.plot(the_ns, d, c='c', linewidth=3)

# labels & titles
plt.title("Opinion convergence", fontsize=30)
plt.xlabel("iterations", fontsize=18)
plt.ylabel("opinion level", fontsize=18)
plt.show()
















