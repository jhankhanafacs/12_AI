import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#reading the data
"""
here the directory of my code and the headbrain6.csv file is same make sure both the files are stored in
same folder or directory
"""
data=pd.read_csv('headbrain6.csv')
data.head()
x=data.iloc[:,2:3].values
y=data.iloc[:,3:4].values
#splitting the data into training and test
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import cross_val_score, KFold

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/4,random_state=0)
#fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
#predict the test result
y_pred=regressor.predict(x_test)
#to see the relationship between the training data values
plt.scatter(x_train,y_train,c='red')
plt.show()
#to see the relationship between the predicted
#brain weight values using scattered graph
plt.plot(x_test,y_pred)
plt.scatter(x_test,y_test,c='red')
plt.xlabel('headsize')
plt.ylabel('brain weight')
#errorin each value
for i in range(0,60):
    print("Error in value number",i,(y_test[i]-y_pred[i]))
    time.sleep(1)
#combined rmse value
rss=((y_test-y_pred)**2).sum()
mse=np.mean((y_test-y_pred)**2)
print("Final rmse value is =",np.sqrt(np.mean((y_test-y_pred)**2)))
