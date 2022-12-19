# Test data: 100 customers in a shop and shopping habits

import numpy as np
import matplotlib.pyplot as plt 
from sklearn.metrics import r2_score as r2

np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x 

# split data into train/test: 80% for training, 20% for testing

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

model = np.poly1d(np.polyfit(train_x, train_y, 4))
line = np.linspace(0, 6, 100)

# calculating r2score with training data: help finds relationship bewteen the data set, and how well the model choice fits the dataset
r_squared_train = r2(train_y, model(train_x))

print("R2 score with training data is: ", r_squared_train)

# calculating r2score with testing data: help finds relationship bewteen the data set, and how well the model choice fits the dataset
r_squared_test = r2(test_y, model(test_x))
print("R2 score with testing data is: ", r_squared_test)

# since the data fits both training and testing, we can start predicting: e.g how much will cx spend if he/she uses 5 minutes in the store
print("Customer spends", model(5), " if he/she uses 5 minutes in store.")

# draw scatter plot with training set
plt.scatter(train_x, train_y, color='red')

# display scatter plot with testing set
plt.scatter(test_x, test_y, color='black')

# from plotting the train/test scatter plot, polynomial regression seems to be the best model choice to use

# draw a plynomial regression line through the data points
plt.plot(line, model(line))

plt.show()




