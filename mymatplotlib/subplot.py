import matplotlib.pyplot as plt
import numpy as np

# first plot
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1) # figure with one row, two columns, and is the first plot
# OR
# plt.subplot(2, 1, 1) # figure with two rows, one column, and is the first plot
plt.plot(x, y)
plt.title("TEST")

# second plot
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2) # one row, 2 columns and is the second plot
# OR
# plt.subplot(2, 1, 2) # figure with two rows, one column, and is the second plot
plt.plot(x, y)
plt.title("CONTROL")

plt.suptitle("COVID'19")
plt.show()