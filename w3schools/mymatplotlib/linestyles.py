import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 2, 10])

# define linestyle
linestyels = ["solid", "dotted", "dashed", "dashdot", "none"]

for lines in linestyels:
    plt.plot(ypoints, ls=lines)
    plt.show()