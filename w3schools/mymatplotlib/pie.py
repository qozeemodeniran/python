import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

# define labels
plabels = ["IT", "CSC", "MPH", "Engineering"]

# make wedge(s) standout
pexplode = [0.2, 0, 0, 0]

plt.pie(y, labels=plabels, explode=pexplode)

# add explanation for each wedge
plt.legend()

plt.show()