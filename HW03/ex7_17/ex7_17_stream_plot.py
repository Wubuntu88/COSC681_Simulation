#!/usr/bin/python

from pylab import *
import matplotlib.pyplot as plt

x_min, x_max = -1, 3
y_min, y_max = -1, 3
x_values, y_values = meshgrid(arange(x_min, x_max, 0.1), arange(y_min, y_max, 0.1))

a = 1.0
b = 1.0

x_dot = - a * x_values * y_values
y_dot = a * x_values * y_values - b * y_values

streamplot(x=x_values, y=y_values, u=x_dot, v=y_dot)
plt.xlim((x_min, x_max))

plt.xlabel("Susceptible", fontsize=20)
plt.ylabel("Infectious", fontsize=20)
plt.title("Susceptible vs Infectious Stream Plot", fontsize=24)

show()
