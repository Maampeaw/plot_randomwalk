# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

import matplotlib.pyplot as plt

from random_walk import RandomWalk

"""Make a random walk"""
rw = RandomWalk()
rw.fill_walk()
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Blues, s=15,)
plt.show()