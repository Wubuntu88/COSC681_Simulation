#!/usr/bin/python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

"""
The resource will have a logistic growth model
The resource is represented as x; The change at each step is the following:
dx / dt = r * x (1 - x / K) - g - z

dg / dt = alpha * x - 3
dz / dt = alpha * x - 2
"""
r = 0.2
K = 1.0
Dt = 1

alpha = .5

resource = 30
zombie_goosies = 4.0
zombies = 2.0

resources_pop = []
zombie_goosies_pop = []
zombies_pop = []
stop_limit = 300
time_range = np.arange(start=0, stop=stop_limit + Dt, step=Dt)
for t in time_range:
    resources_pop.append(resource)
    zombies_pop.append(zombies)
    zombie_goosies_pop.append(zombie_goosies)
    # resource += r * resource * (1 - resource / 200) * Dt - \
    resource += 30 - (.1 * zombies + .05 * zombie_goosies)
    if resource < 0:
        resource = 0
    zombies += .001 * resource - .01 * zombies  # .7
    zombie_goosies += .002 * resource - .01 * zombie_goosies  # 1.5
    print("change: " + str(r * resource * (1 - resource / 200) * Dt))

plt.plot(time_range, resources_pop, linewidth=3, c='green')
plt.plot(time_range, zombies_pop, linewidth=3, c='orange')
plt.plot(time_range, zombie_goosies_pop, linewidth=3, c='red')

# labels & titles
plt.title("Two species competing for a resource", fontsize=20)
plt.xlabel("Time", fontsize=18)
plt.ylabel("Population", fontsize=18)

# legend
resource_patch = mpatches.Patch(color='green', label='Resource')
zombies_patch = mpatches.Patch(color='orange', label='Zombies')
zombies_goosies_patch = mpatches.Patch(color='red', label='Zombie goosies')
plt.legend(handles=[resource_patch, zombies_patch, zombies_goosies_patch], loc=1)

plt.show()
