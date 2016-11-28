#!/usr/bin/python

from pylab import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


"""
dx / dt = ax(1-x)(x-y)

Note: y = 1-x, therefore we can substitute x for y to the the following

dx / dt = ax(1-x)(2x-1)+r(p-x)
"""


def x_eq_0(the_domain):
    return [0.5 for n in the_domain]


def x_eq_1(the_domain, r_value):
    return [0.5 * (1 - np.sqrt(1 - 2 * r_value)) for n in the_domain]


def x_eq_2(the_domain, r_value):
    return [0.5 * (np.sqrt(1 - 2 * r_value) + 1) for n in the_domain]

t_min, t_max = -1, 1
x_min, x_max = -1, 2
increment = 0.1


t_values, x_values = meshgrid(arange(t_min, t_max, increment), arange(x_min, x_max, increment))


a = 1
p = 0.5
r = 0

t_dot = np.ones(shape=t_values.shape)
x_dot = a * x_values * (1 - x_values) * (2 * x_values - 1) + r * (p - x_values)

streamplot(x=t_values, y=x_values, u=t_dot, v=x_dot)
line_domain = np.linspace(t_min, t_max, num=1000)

plt.plot(line_domain, x_eq_0(line_domain), color='black', linewidth=2)
plt.plot(line_domain, x_eq_1(line_domain, r_value=r), color='red', linewidth=2)
plt.plot(line_domain, x_eq_2(line_domain, r_value=r), color='orange', linewidth=2)

eq_0 = x_eq_0([1])[0]
eq_1 = x_eq_1([1], r_value=r)[0]
eq_2 = x_eq_2([1], r_value=r)[0]
print("eq_0: " + str(eq_0))
print("eq_1: " + str(eq_1))
print("eq_2: " + str(eq_2))

blue_patch = mpatches.Patch(color='black', label='x_eq_0:' + '{0:.1f}'.format(eq_0))
red_patch = mpatches.Patch(color='red', label='x_eq_1: ' + '{0:.1f}'.format(eq_1))
green_patch = mpatches.Patch(color='orange', label='x_eq_2: ' + '{0:.1f}'.format(eq_2))

plt.legend(handles=[blue_patch, red_patch, green_patch])

plt.xlim((t_min, t_max - increment))
plt.ylim((x_min, x_max))

plt.title("Stream plot of dx / dt = ax(1-x)(2x-1)+r(p-x)\n(a = {0:.1f}, p = {1:.1f}, r = {2:.1f})".format(a, p, r), fontsize=20)
plt.xlabel("t", fontsize=20)
plt.ylabel("x", fontsize=20)

show()
