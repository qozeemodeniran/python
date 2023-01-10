import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# read data into data frame
df = pd.read_csv("data.csv")

# change string values into numerical values
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

# separate feature(columns that we try to predict from) from the target(the column with the values we try to predict)
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

# create decision tree
dt = DecisionTreeClassifier()

# convert X values to array
dt = dt.fit(X.values, y)

# Example: Should I go see a show starring a 40 years old American comedian, with 10 years of experience, and a comedy ranking of 7?
decision = dt.predict([[40, 10, 6, 1]])
if decision == [1]:
    print("Yes, you should go!")
else:
    print("No, do not go!")


# result interpretation here: https://www.w3schools.com/python/python_ml_decision_tree.asp
tree.plot_tree(dt, feature_names=features)
plt.show()