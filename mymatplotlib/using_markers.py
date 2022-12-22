# import matplotlib and pyplot
import matplotlib.pyplot as plt

# import numpy
import numpy as np

# define points
# x-points = default x points
ypoints = np.array([3, 8, 1, 10])

# plot the graph using defined markers as 'o' which means dots
# plt.plot(ypoints, marker = 'o')

# or '*' which means star
# plt.plot(ypoints, marker = '*')

# or '+' which means cross
plt.plot(ypoints, marker = '+')

""" other markers can be used
    to define how want the points in our graph look like"""

plt.show()