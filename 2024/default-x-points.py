import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])
xpoints = np.array([1, 2, 3, 4, 3, 9])
plt.plot(ypoints, 'o:r')
plt.scatter(xpoints, ypoints)
plt.xlabel("x-values")
plt.ylabel("y-values")
pie_labels = ["apple","banana","guava","mango","kiwi","water melon"]
plt.pie(ypoints, labels=pie_labels)
plt.grid()
plt.show()
plt.close()