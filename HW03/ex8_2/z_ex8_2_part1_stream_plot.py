#!/usr/bin/python

from pylab import *
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

"""
Exercise 8.1
Conduct a bifurcation analysis of the following dynamical system with parameter r:
dx / dt = ax(1-x)(2x-1) + r(p-x)
Note:
p = 0.5
a = 1

equation after substitution:

dx / dt = x(1-x)(2x-1) + r(0.5-x)

solutions in terms of x for equation:
0 = x(1-x)(2x-1) + r(0.5-x)

solutions:

x = 1/2
x = 1/2 * (1 - sqrt(1 - 2*r))
x = 1/2 * (sqrt(1 - 2*r) + 1)


Answer:
The critical threshold of r at which a bifurcation occurs is r = 1/2
It is a super critical pitchfork bifurcation.
Super critical pitchfork bifurcations are when a stable equilibrium point forks
into two stable equilibrium points and a third unstable equilibrium point.
"""


def x_eq_0(the_domain):
    return np.array([0.5 for n in the_domain])


def x_eq_1(the_domain):
    return 0.5 * (1 - np.sqrt(1 - 2 * the_domain))


def x_eq_2(the_domain):
    return 0.5 * (np.sqrt(1 - 2 * the_domain) + 1)


x_min, x_max = -2, 2
y_min, y_max = -2, 3

domain_below_one_half = linspace(start=x_min, stop=0.5, num=500)
domain_above_one_half = linspace(start=0.5, stop=x_max, num=500)
plot(domain_below_one_half, x_eq_0(domain_below_one_half), 'b--', linewidth=5)
plot(domain_above_one_half, x_eq_0(domain_above_one_half), 'b-', linewidth=5)

domain = linspace(start=x_min, stop=x_max, num=2000)
plot(domain, x_eq_1(domain), 'r-', linewidth=5)
plot(domain, x_eq_2(domain), 'g-', linewidth=5)

# legend stuff
x_eq_1_string = '1/2 * (1 - sqrt(1 - 2r))'
x_eq_2_string = '1/2 * (sqrt(1 - 2r) + 1)'

blue_patch = mpatches.Patch(color='blue', label='x_eq_0: 0')
red_patch = mpatches.Patch(color='red', label='x_eq_1: ' + x_eq_1_string)
green_patch = mpatches.Patch(color='green', label='x_eq_2: ' + x_eq_2_string)

plt.legend(handles=[blue_patch, red_patch, green_patch])

# title, axis specification, and making labels
plt.title('bifurcation diagram', fontsize=20)
plt.axis([x_min, x_max, y_min, y_max])
plt.xlabel('r', fontsize=20)
plt.ylabel('x_eq', fontsize=20)

# arrows when r > 0
arrow(x=1, y=2, dx=0, dy=-1.3, width=.03, head_width=0.1, head_length=0.1, color='black')
arrow(x=1, y=-2, dx=0, dy=2.3, width=.03, head_width=0.1, head_length=0.1, color='black')

# arrows when r = 1/2
arrow(x=0.5, y=2, dx=0, dy=-1.3, width=.03, head_width=0.1, head_length=0.1, color='black')
arrow(x=0.5, y=-2, dx=0, dy=2.3, width=.03, head_width=0.1, head_length=0.1, color='black')

# arrows when r < 1/2 (pointing away from x_eq == 0
vertical_offset_1 = 0.3
y_start_1 = 0.6
point_up_at_green_line_at_x_is_neg_1 = x_eq_2(np.array([-1]))[0]
arrow(x=-1, y=y_start_1, dx=0, dy=point_up_at_green_line_at_x_is_neg_1 - 0.5 - vertical_offset_1,
      width=.03, head_width=0.1, head_length=0.1, color='black')
y_start_2 = 0.4
point_down_at_red_line_at_x_is_neg_1 = x_eq_1(np.array([-1]))[0]
arrow(x=-1, y=y_start_2, dx=0, dy=point_down_at_red_line_at_x_is_neg_1 - 0.5 + vertical_offset_1,
      width=.03, head_width=0.1, head_length=0.1, color='black')

# arrows when r < 1/2 (pointing towards x_eq_1 and x_eq_2)
# pointing towards green line
vertical_offset_2 = .2
y_start_1 = 3.0
arrow(x=-1, y=y_start_1, dx=0, dy=point_up_at_green_line_at_x_is_neg_1 - y_start_1 + vertical_offset_2, width=.03,
      head_width=0.1, head_length=0.1, color='black')
y_start_2 = -2.0
arrow(x=-1, y=y_start_2, dx=0, dy=point_down_at_red_line_at_x_is_neg_1 + abs(y_start_2) - vertical_offset_2, width=.03,
      head_width=0.1, head_length=0.1, color='black')

plt.show()
