import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

# define the markers such that the points are circle, the lines are dots, and the color is red
# plt.plot(ypoints, 'o:r')

# define the markers such that the points are circle, the lines are straight-line, and the color is red
# plt.plot(ypoints, 'o-r')

# define the markers such that the points are circle, the lines are hyphen, and the color is red
# plt.plot(ypoints, 'o--r')

# define the markers such that the points are circle, the lines are hyphen plus a dot, and the color is red
plt.plot(ypoints, 'o-.r')

plt.show()