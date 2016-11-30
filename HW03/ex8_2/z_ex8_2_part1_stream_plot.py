#!/usr/bin/python

from pylab import *
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import numpy as np

"""
Exercise 8.1
Conduct a bifurcation analysis of the following dynamical system with parameter r:
dx / dt = ax(1-x)(2x-1)
Note:
p = 0.5
a = 1

equation after substitution:

dx / dt = x(1-x)(2x-1)

solutions:
x = 0
x = 1/2
x = 1
"""

t_min, t_max = -1, 1
x_min, x_max = -1, 2
increment = 0.1

t_values, x_values = meshgrid(arange(t_min, t_max, increment), arange(x_min, x_max, increment))

a = 1

t_dot = np.ones(shape=t_values.shape)
x_dot = a * x_values * (1 - x_values) * (2 * x_values - 1)

streamplot(x=t_values, y=x_values, u=t_dot, v=x_dot)

domain = np.linspace(t_min, t_max, num=200)
plt.plot(domain, [0 for n in domain], color='orange', linewidth=3)
plt.plot(domain, [0.5 for n in domain], color='green', linewidth=3)
plt.plot(domain, [1 for n in domain], color='red', linewidth=3)

plt.title('Stream plot', fontsize=20)
plt.xlabel('t', fontsize=20)
plt.ylabel('x', fontsize=20)

show()
