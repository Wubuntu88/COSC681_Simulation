#!/usr/bin/python

from pylab import *
import matplotlib.pyplot as plt

xvalues, yvalues = meshgrid(arange(0, 30, 0.1), arange(0, 14, 0.1))

r = 0.5
k = 10.0

xdot = np.ones(shape=xvalues.shape)
ydot = r * yvalues * (1 - yvalues / k)

streamplot(x=xvalues, y=yvalues, u=xdot, v=ydot)

plt.xlabel("t", fontsize=20)
plt.ylabel("x", fontsize=20)
plt.title("Graph of Integral curves for differential equations:\n" +
          "dy/dt = r*y*(1-y/k) ; " +
          "dx/dt = 1 ; " +
          "r = {0:.2f}".format(r) + ", k = {0:.2f}".format(k), fontsize=20)

show()
