# import matplotlib and pyplot
import matplotlib.pyplot as plt

# import numpy
import numpy as np

# define coordinates
# xpoints - would be left undefined and would be automatically assigned values 0, 1, 2, 3 etc., depending on the length of ypoints
ypoints = np.array([3, 8, 1, 10, 5, 7])

# plot the graph
plt.plot(ypoints)

# show graph
plt.show()