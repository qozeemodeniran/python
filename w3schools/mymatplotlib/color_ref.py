import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

colors = ["r", "g", "b", "c", "m", "y", "k", "w"]
for color in colors:
    # plotting graph in each color from the colors list
    print("I am plotting the graph in {}".format(color))
    plt.plot(ypoints, c=color)

    plt.show()