# import matplotlib and pyplot
import matplotlib.pyplot as plt

# import numpy
import numpy as np

# define coordinates
xcords = np.array([1, 5])
ycords = np.array([2, 9])

# plot graph without line
plt.plot(xcords, ycords, 'o')

# show graph
plt.show()