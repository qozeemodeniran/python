import pandas as pd
from sklearn import linear_model as lm
from sklearn.preprocessing import StandardScaler as ss

scale = ss()

df = pd.read_csv("/Users/qozeemodeniran/Projects/python/w3schools/ml/data.csv")
X = df[['Weight', 'Volume']]
scaledX = scale.fit_transform(X)

print(scaledX)