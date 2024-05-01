import numpy as np
from scipy import stats

num_arr = [3,2,45,6,7,8,9,9,6,5,3,2,2,4,5,6,7,6,32,2,4,6,7,7]
mean = np.mean(num_arr)
median = np.nanmean(num_arr)
mode = stats.mode(num_arr)

results = f"The mean, median, and mode of the array {num_arr} is {mean}, {median}, and {mode} respectively"
print(results)
