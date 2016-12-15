#!/usr/bin/python

import numpy as np
import random as random
import matplotlib.pyplot as plt
import seaborn as sns


def simulate_shot():
    """
    Simulates one shot the Luke makes.
    :return: a tuple containing:
    1:  Tuple:
            the (x,y) pair where the laser hit the bottom of the shaft
            or where it hit the side of the shaft.
    2:  Boolean:
        true if it hit the target at the bottom
        false if it hits outside the target or a wall
    """
    cylinder_radius = 0.5
    cylinder_radius_squared = cylinder_radius**2
    target_radius = 0.1
    target_radius_squared = target_radius**2

    deltas = np.array([0.0, 0.0])  # dx, dy
    positions = np.array([0.0, 0.0])  # x, y

    time_step = 0.1
    time_steps = np.linspace(start=0, stop=2, num=int(2/time_step) + 1)

    # k will be the probability that the dx or dy gravity will fluctuate
    k = 1.0 / 5.0

    for t_step in time_steps:
        x_will_change = random.random()
        y_will_change = random.random()
        if x_will_change < k:
            rand_x = (random.random() / 10) - 0.05
            deltas[0] += rand_x
        if y_will_change < k:
            rand_y = (random.random() / 10) - 0.05
            deltas[1] += rand_y

        positions += deltas

        # check if laser hit wall
        dist_away_from_center_squared = positions[0]**2 + positions[1]**2
        if dist_away_from_center_squared > cylinder_radius_squared:  # hit wall
            return (positions[0], positions[1]), False
    dist_away_from_center_squared = positions[0]**2 + positions[1]**2
    if dist_away_from_center_squared > target_radius_squared:  # missed target
        return (positions[0], positions[1]), False
    else:  # hit target
        return (positions[0], positions[1]), True


# Two tasks:
# 1) Calculate probability of success
# 2) Plot figure of hits, and misses


hits_xs = []
hits_ys = []
misses_xs = []
misses_ys = []

for iteration in range(0, 5000):
    result = simulate_shot()
    x, y = result[0]
    if result[1]:  # if result was a hit
        hits_xs.append(x)
        hits_ys.append(y)
    else:
        misses_xs.append(x)
        misses_ys.append(y)

successes = len(hits_xs)
failures = len(misses_xs)

probability_of_success = float(successes) / failures
print("P(success): {0:.4f}".format(probability_of_success))

'''
plt.scatter(hits_xs, hits_ys, c="blue", s=30)
plt.scatter(misses_xs, misses_ys, c="red", s=30)

plt.title("Luke's shots at the bottom of the shaft", fontsize=20)
plt.xlabel("x", fontsize=16)
plt.ylabel("y", fontsize=16)
plt.show()
'''
