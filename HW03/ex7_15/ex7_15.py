#!/usr/bin/python

from pylab import *
import matplotlib.pyplot as plt

x_values, y_values = meshgrid(arange(0, 30, 0.1), arange(0, 14, 0.1))

r = 0.5
k = 10.0

x_dot = np.ones(shape=x_values.shape)
y_dot = r * y_values * (1 - y_values / k)

streamplot(x=x_values, y=y_values, u=x_dot, v=y_dot)

plt.xlabel("t", fontsize=20)
plt.ylabel("x", fontsize=20)
plt.title("Graph of Integral curves for differential equations:\n" +
          "dy/dt = r*y*(1-y/k) ; " +
          "dx/dt = 1 ; " +
          "r = {0:.2f}".format(r) + ", k = {0:.2f}".format(k), fontsize=20)

show()
