#!/usr/bin/python
import time
import random
import sys


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
            distance = x**2 + y**2
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

iterations = 1000
try:
    if len(sys.argv) >= 2:
        iterations = int(sys.argv[1])
except ValueError:
    iterations = 1000

LCG_approximation = LCGPiApproximator().approximate_pi(iterations=iterations)
good_approximation = GoodPiApproximator().approximate_pi(iterations=iterations)

print('results:')
print('LCG approximation of pi after {0:d} iterations: {1:.6f}'.format(iterations, LCG_approximation))
print('good approximation of pi after {0:d} iterations: {1:.6f}'.format(iterations, good_approximation))
"""
Output of program
Williams-MacBook-Air:part1 Will$ python3 pure_pi_approximator.py 20000
results:
LCG approximation of pi after 20000 iterations: 3.149200
good approximation of pi after 20000 iterations: 3.131400
"""
