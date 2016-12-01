#!/usr/bin/python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time
import random
import matplotlib.patches as mpatches


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


class LCGConvergenceToPi:

    def __init__(self):
        self.rng = Random0(seed=int(time.time()))
        self.radius = 1

    def generate_convergence_to_pi(self, iterations):
        assert iterations > 0
        total = 0
        convergence_to_pi = []
        items_inside_circle = 0
        for i in range(0, iterations + 1):

            x = self.rng.next_random()
            y = self.rng.next_random()
            distance = np.sqrt(x**2 + y**2)
            items_inside_circle += 1 if distance <= self.radius else 0
            total += 1
            pi_approximation = (float(items_inside_circle) / total) * 4
            convergence_to_pi.append(pi_approximation)
        return convergence_to_pi


class GoodConvergenceToPi:

    def __init__(self):
        self.radius = 1

    def generate_convergence_to_pi(self, iterations):
        assert iterations > 0
        total = 0
        convergence_to_pi = []
        items_inside_circle = 0
        for i in range(0, iterations + 1):
            x = random.random()
            y = random.random()
            distance = x**2 + y**2
            items_inside_circle += 1 if distance <= self.radius else 0
            total += 1
            pi_approximation = (float(items_inside_circle) / total) * 4
            convergence_to_pi.append(pi_approximation)
        return convergence_to_pi


LCG_convergence_generator = LCGConvergenceToPi()
good_convergence_generator = GoodConvergenceToPi()

iterations = 1000
LCG_converge_to_pi_array = LCG_convergence_generator.generate_convergence_to_pi(iterations=iterations)
GOOD_converge_to_pi_array = good_convergence_generator.generate_convergence_to_pi(iterations=iterations)


sns.tsplot(data=LCG_converge_to_pi_array, linewidth=4, color='darkblue', legend=True)
sns.tsplot(data=GOOD_converge_to_pi_array, linewidth=4, color='indianred', legend=True)
array_of_pi = np.array([np.pi for x in range(0, iterations+1)])
sns.tsplot(data=array_of_pi, color='black')

dark_blue_patch = mpatches.Patch(color='darkblue', label='using the random0 LCG RNG')
indian_red_patch = mpatches.Patch(color='indianred', label='using the built-in python RNG')
black_patch = mpatches.Patch(color='black', label='PI')
plt.legend(handles=[dark_blue_patch, indian_red_patch, black_patch],
           loc='lower right')

plt.xlabel('Nth Iteration', fontsize=26)
plt.ylabel('Approximation of Pi', fontsize=26)
plt.title('Convergence of approximation of Pi with increasing iterations in the approximation simulation', fontsize=26)
plt.xlim((0, iterations))
plt.show()
