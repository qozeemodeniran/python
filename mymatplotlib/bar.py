import matplotlib.pyplot as plt
import numpy as np

x = np.array(["W", "X", "Y", "Z"])
y = np.array([3, 8, 1, 10])

# vertical bar
# plt.bar(x, y)

# horizontal bar
plt.barh(x, y)
plt.show()