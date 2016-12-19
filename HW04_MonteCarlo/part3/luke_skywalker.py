#!/usr/bin/python

import math as math
import numpy as np
import random as random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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


# Three tasks:
# 1) Calculate probability of success
# 2) Plot figure of hits, and misses
# 3) Answer this question:
# How many shots will Luke have to take to have a 75% or
# better chance of hitting the target?

hits_xs = []
hits_ys = []
misses_xs = []
misses_ys = []

ITERATIONS = 10000

for iteration in range(0, ITERATIONS):
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

# Part 1
probability_of_success = float(successes) / failures
print("Part 1: Calculate probability of success")
print("P(success): {0:.4f}".format(probability_of_success))

#remove comments to plot the figure
# Part 2
plt.scatter(hits_xs, hits_ys, c="blue", s=30)
plt.scatter(misses_xs, misses_ys, c="red", s=30)

red_patch = mpatches.Patch(color='red', label='Misses or Wall Collisions')
blue_patch = mpatches.Patch(color='blue', label='Hits')
plt.legend(handles=[red_patch, blue_patch],
           loc='upper right')


plt.title("Luke's shots at the bottom of the shaft\n" +
          "iterations: {:d}, hits: {:d}, misses: {:d}"
          .format(ITERATIONS, len(hits_xs), len(misses_xs)),
          fontsize=20)
plt.xlabel("x", fontsize=16)
plt.ylabel("y", fontsize=16)
plt.show()


# one output of program:
# P(success): 0.0124


# Part 3) Calculate the # of times luke must shoot to have a
# 75% chance or better of hitting the target

# to do this, we will calculate the probability of failure and rephrase the question
# How many times do you have to shoot to have a 25% chance or lower of missing all of them
# Equation steps:
# A: 1 - P(failure) ^ n = .75
# B: .25 = P(failure) ^ n
# C: ln(.25) = ln(P(failure) ^ n)
# D: ln(.25) = n * ln(P(failure))
# E: ln(.25) / ln(P(failure)) = n
# F: take the ceil of n; that is the number of times to shoot to have
# a 75% chance or greater of shooting the target.
probability_of_failure = 1 - probability_of_success
n_shots = math.log(.25) / math.log(probability_of_failure)
n_shots = int(math.ceil(n_shots))
print("Number of shots to have a 75% chance or greater of hitting the target: {:d}"
      .format(n_shots))
# one output (for P(success) = 0.0124):
# Number of shots to have a 75% chance or greater of hitting the target: 112
