import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

data=pd.read_csv("forestfires.csv")
print(data.head())

y=data.temp
x=data.drop("temp",axis=1)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
print(x_train.head())

x_train.shape
print(x_test.head())

x_test.shape

print(x_train.shape, x_test.shape)
