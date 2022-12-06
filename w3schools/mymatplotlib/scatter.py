# import matplotlib and pyplot
import matplotlib.pyplot as plt

# import numpy
import numpy as np

# define x and y axis using array
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

# plot scatter graph using the scatter(function)
plt.scatter(x, y)

# give each axis a label name
plt.xlabel("age of cars")
plt.ylabel("speed of cars")
plt.show()