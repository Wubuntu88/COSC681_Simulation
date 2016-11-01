#!/usr/bin/python
import matplotlib.pyplot as plt
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

time_range = np.arange(start=0, stop=900 + Dt, step=Dt)
for t in time_range:
    resources_pop.append(resource)
    zombies_pop.append(zombies)
    zombie_goosies_pop.append(zombie_goosies)

    #resource += r * resource * (1 - resource / 200) * Dt \
    resource += 30 \
                - .1 * zombies \
                - .05 * zombie_goosies
    zombies += .001 * resource - .01
    zombie_goosies += .002 * resource - .03
    print("change: " + str(r * resource * (1 - resource / 200) * Dt))

plt.plot(time_range, resources_pop)
plt.plot(time_range, zombies_pop)
plt.plot(time_range, zombie_goosies_pop)
plt.show()

