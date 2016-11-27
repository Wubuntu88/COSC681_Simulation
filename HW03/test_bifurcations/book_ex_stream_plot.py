#!/usr/bin/python

from pylab import *
import matplotlib.pyplot as plt

t_min, t_max = -6, 6
x_min, x_max = -6, 6

tvalues, xvalues = meshgrid(arange(t_min, t_max, 0.1), arange(x_min, x_max, 0.1))

# r = 9.0
r = 0.0

t_dot = np.ones(shape=tvalues.shape)
x_dot = r - xvalues * xvalues

streamplot(x=tvalues, y=xvalues, u=t_dot, v=x_dot)

plt.xlim((t_min, t_max))
plt.ylim((x_min, x_max))

plt.title("Stream plot of dx/dt = r - y^2 ; (r = {0:.2f})".format(r), fontsize=26)
plt.xlabel("t", fontsize=20)
plt.ylabel("x", fontsize=20)

show()
