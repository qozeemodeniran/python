import matplotlib.pyplot as plt
import numpy as np

# generate random array of 250 values
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()