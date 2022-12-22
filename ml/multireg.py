# import modules
import pandas as pd
from sklearn import linear_model

# read csv
df = pd.read_csv("/Users/qozeemodeniran/Projects/python/w3schools/ml/data.csv")

# define independent and dependent variables, name them x and y, respectively
X = df[['Weight', 'Volume']]
y = df['CO2']

# create linear regression object
regr = linear_model.LinearRegression()
regr.fit(X.values, y)

# predict CO2 emision when car weighs 2300kg, and volume is 1300cm-cube
predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)