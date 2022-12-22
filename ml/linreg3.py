# to know how fit is the data is for linear regression:
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

# print(r)

"""
since r = -0.7586, which is a stong negative, shows that there's a relationship 
between the varibales and indicates safety for using linear regression for predicting
future outcomes.
Now, to predict the speed of a ten years old car, we just input 10 into our function
as follows
"""
def myfunc(x):
    return slope * x + intercept

speed_of_ten_years_old_car = myfunc(10)

print(speed_of_ten_years_old_car)

# the above predict 85.59