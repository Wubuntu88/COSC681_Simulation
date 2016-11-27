#!/usr/bin/python

from pylab import *
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


"""
Exercise 8.1
Conduct a bifurcation analysis of the following dynamical system with parameter r:
dx / dt =rx(x+1)x
Find the critical threshold of r at which a bifurcation occurs.
Draw a bifurcation diagram and determine what kind of bifurcation it is.

Solutions to the system:
x_eq1 is 0
x_eq2 is 1/r - 1


"""


def x_eq1(the_domain):
    return np.zeros(shape=the_domain.shape)


def x_eq2(the_domain):
    return 1 / the_domain - 1


domain = linspace(start=-10, stop=10, num=200)
plot(domain, x_eq1(domain), 'b-', linewidth=3)
plot(domain, x_eq2(domain), 'r--', linewidth=3)
plot(domain, [-1 for n in domain], color='black', linewidth=1)

# legend stuff
red_patch = mpatches.Patch(color='red', label='x_eq2: 1/r - 1 (unstable)')
blue_patch = mpatches.Patch(color='blue', label='x_eq1: 0 (stable)')
plt.legend(handles=[red_patch, blue_patch])

# title, axis specification, and making labels
plt.title('bifurcation diagram', fontsize=20)
plt.axis([-6, 6, -6, 6])
plt.xlabel('r', fontsize=20)
plt.ylabel('x_eq', fontsize=20)
plt.show()
