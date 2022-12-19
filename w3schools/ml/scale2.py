import pandas as pd
from sklearn import linear_model as lm
from sklearn.preprocessing import StandardScaler as ss
scale = ss()

df = pd.read_csv("/Users/qozeemodeniran/Projects/python/w3schools/ml/data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = lm.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)
