#!/usr/bin/python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
"""
Simulate the following continuous-time Lotka-Volterra (predator- prey) model
for 0 <= t < 50 in Python, with x(0) = y(0) = 0.1, a = b = c = d = 1 and t = 0.01.
Visualize the simulation results over time and also in a phase space.
dx / dt = ax - bxy
dy / dt = -cy + dxy

new_x = x + (a*x - b*x*y) * delta_t
new_y = y + (-c*y + d*x*y) * delta_t

-- x is the prey
-- y is the predator
"""
x = y = 0.1
a = b = c = d = 1
max_t = 100
delta_t = 0.01

times = []
xs = []  # prey population fluctuations
ys = []  # predator population fluctuations

the_range = np.arange(start=0, stop=max_t + delta_t, step=delta_t)

for time in the_range:
    dx_dt = a * x - b * x * y
    dy_dt = -c * y + d * x * y
    new_x = x + dx_dt * delta_t
    new_y = y + dy_dt * delta_t
    x, y = new_x, new_y
    xs.append(x)
    ys.append(y)

plt.plot(the_range, xs, c='blue', linewidth=5)
plt.plot(the_range, ys, c='red', linewidth=5)
plt.suptitle("Predator/Prey Population Fluctuations", fontsize=22)
plt.xlabel("Time", fontsize=18)
plt.ylabel("Population", fontsize=18)

prey_patch = mpatches.Patch(color='blue', label='Prey')
predators_patch = mpatches.Patch(color='red', label='Predators')
plt.legend(handles=[prey_patch, predators_patch], loc=2)
plt.show()
