#!/usr/bin/python

from pylab import *
import matplotlib.pyplot as plt

"""
dx / dt = rx(x+1)-x

Solution for x when:
0 = rx(x+1)-x
Solutions are:
x = 1/r - 1
x = 0

Therefore, when r == -0.5, solutions are:
1/-0.5 - 1 -> -3
AND
0
"""

t_min, t_max = -3, 3
x_min, x_max = -4, 2

t_values, x_values = meshgrid(arange(t_min, t_max, 0.1), arange(x_min, x_max, 0.1))

r = -0.5
# r = 1

t_dot = np.ones(shape=t_values.shape)
x_dot = r * x_values * (x_values + 1) - x_values

streamplot(x=t_values, y=x_values, u=t_dot, v=x_dot)

plt.xlim((t_min, t_max))
plt.ylim((x_min, x_max))

plt.title("Stream plot of dx / dt = rx(x+1)-x ; (r = {0:.1f})".format(r), fontsize=20)
plt.xlabel("t", fontsize=20)
plt.ylabel("x", fontsize=20)

show()
