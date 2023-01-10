# import stats from scipy for further calculations
from scipy import stats
import matplotlib.pyplot as plt


x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)
"""where:
r = relationship between the two variables, x and y, also called coefficient of correlation. This value ranges from (1, -1), where 0=no relationship, and 1 & -1= 100% relationship (+ve or -ve)
p = """

# create a equation as function: y=mx+c which means, the value of 'y' for every value of 'x'
def myfunc(x):
    return slope * x + intercept

# define the linear regression model
mymodel = list(map(myfunc, x))

# plot scatter plot
plt.scatter(x, y)

# draw line through the points
plt.plot(x, mymodel)

# display the graph
plt.show()