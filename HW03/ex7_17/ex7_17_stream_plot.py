#!/usr/bin/python

from pylab import *
import matplotlib.pyplot as plt

x_min, x_max = -1, 30
y_min, y_max = 0, 30
xvalues, yvalues = meshgrid(arange(x_min, x_max, 0.1), arange(y_min, y_max, 0.1))

a = 0.5
b = 2.0

xdot = - a * xvalues * yvalues
ydot = a * xvalues * yvalues - b * yvalues

streamplot(x=xvalues, y=yvalues, u=xdot, v=ydot)
plt.xlim((x_min, x_max))

plt.xlabel("Susceptible", fontsize=20)
plt.ylabel("Infectious", fontsize=20)
plt.title("Susceptible vs Infectious Stream Plot", fontsize=24)

show()
