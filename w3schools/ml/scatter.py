import numpy as np
import matplotlib.pyplot as plt

# generate 1000 random numbers where mean=5.0, sd=1.0
x = np.random.normal(5.0, 1.0, 1000);

# generate 1000 random numbers where mean=10.0, sd=2.0
y = np.random.normal(10.0, 2.0, 1000);

plt.scatter(x, y)
plt.show()