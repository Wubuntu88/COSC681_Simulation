#!/usr/bin/python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time
import random
'''
This script performs repeated Monte Carlo simulations to approximate Pi.
It runs two types of simulations: one using a bad random number generator and
one using the built in random number generator for python.
When viewing the plot, note that each approximation for a given iteration
independent of the other approximations for different iterations.
'''


class Random0:
    def __init__(self, seed):
        self.seed = seed
        self.mod_value = 134456  # (2^3 * 7^5)
        self.multiplier = 8121
        self.increment = 28411
        self.previous = seed

    def next_random(self):
        self.previous = (self.multiplier * self.previous + self.increment) % self.mod_value
        return float(self.previous) / self.mod_value


class LCGPiApproximator:

    def __init__(self):
        self.rng = Random0(seed=int(time.time()))
        self.radius = 1

    def approximate_pi(self, iterations):
        assert iterations > 0
        items_inside_circle = 0
        for i in range(0, iterations + 1):
            x = self.rng.next_random()
            y = self.rng.next_random()
            distance = np.sqrt(x**2 + y**2)
            items_inside_circle += 1 if distance <= self.radius else 0
        pi_approximation = (float(items_inside_circle) / iterations) * 4
        return pi_approximation


class GoodPiApproximator:

    def __init__(self):
        self.radius = 1

    def approximate_pi(self, iterations):
        assert iterations > 0
        items_inside_circle = 0
        for i in range(0, iterations + 1):
            x = random.random()
            y = random.random()
            distance = x ** 2 + y ** 2
            items_inside_circle += 1 if distance <= self.radius else 0
        pi_approximation = (float(items_inside_circle) / iterations) * 4
        return pi_approximation


LCG_pi_approximator = LCGPiApproximator()
good_pi_approximator = GoodPiApproximator()

LCG_approximations = []
good_approximations = []
iteration_range = 1000
the_iterations = [n for n in range(1, iteration_range + 1)]

for iteration in the_iterations:
    LCG_approximation_of_pi = LCG_pi_approximator.approximate_pi(iterations=iteration)
    LCG_approximations.append(LCG_approximation_of_pi)
    good_approximation_of_pi = good_pi_approximator.approximate_pi(iterations=iteration)
    good_approximations.append(good_approximation_of_pi)

sns.tsplot(data=LCG_approximations, linewidth=2, color='red')
sns.tsplot(data=good_approximations, linewidth=2, color='blue')

dark_blue_patch = mpatches.Patch(color='red', label='using the random0 LCG RNG')
indian_red_patch = mpatches.Patch(color='blue', label='using the built-in python RNG')
black_patch = mpatches.Patch(color='black', label='PI')
plt.legend(handles=[dark_blue_patch, indian_red_patch, black_patch],
           loc='upper right')

plt.xlabel('Nth Iteration', fontsize=26)
plt.ylabel('Approximation of Pi', fontsize=26)
plt.title('Approximation of Pi vs. iterations used to calculate Pi', fontsize=32)
plt.xlim((0, max(the_iterations)))

plt.show()

