import numpy as np
val = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

sd = np.std(val)
var = np.var(val)

print(f"The standard deviation and variance of {val} is {sd} and {var} respectfully")