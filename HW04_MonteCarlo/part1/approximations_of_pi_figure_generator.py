#!/usr/bin/python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time
import random


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
            distance = np.sqrt(x ** 2 + y ** 2)
            items_inside_circle += 1 if distance <= self.radius else 0
        pi_approximation = (float(items_inside_circle) / iterations) * 4
        return pi_approximation


LCG_pi_approximator = LCGPiApproximator()
good_pi_approximator = GoodPiApproximator()

LCG_approximations = []
good_approximations = []
iteration_range = 100
the_iterations = [n for n in range(1, iteration_range + 1)]

for iteration in the_iterations:
    LCG_approximation_of_pi = LCG_pi_approximator.approximate_pi(iterations=iteration)
    LCG_approximations.append(LCG_approximation_of_pi)
    good_approximation_of_pi = good_pi_approximator.approximate_pi(iterations=iteration)
    good_approximations.append(good_approximation_of_pi)
'''
last_LCG_approximation = LCG_approximations[-1]
last_good_approximation = good_approximations[-1]

print('results:')
print('LCG approximation of pi after {0:.6f} iterations'.format(last_LCG_approximation))
print('good approximation of pi after {0:.6f} iterations'.format(last_good_approximation))

'''
sns.tsplot(data=LCG_approximations, linewidth=2, color='red')
sns.tsplot(data=good_approximations, linewidth=2, color='blue')

plt.xlabel('Nth Iteration', fontsize=26)
plt.ylabel('Approximation of Pi', fontsize=26)
plt.title('Approximation of Pi vs. iterations used to calculate Pi', fontsize=32)
plt.xlim((0, max(the_iterations)))

plt.show()
