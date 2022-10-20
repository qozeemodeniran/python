import matplotlib.pyplot as plt
import numpy as np

# define multiple points
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

# plot multi-lines graph
plt.plot(x1, y1, ls='dashed')
plt.plot(x2, y2, ls='dotted')
plt.show()