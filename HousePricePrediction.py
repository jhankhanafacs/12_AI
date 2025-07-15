from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
# load dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.csv'
dataframe = read_csv(url, header=None)
#dataframe=pd.read_csv(‘housing.csv’)
data = dataframe.values
# split into inputs and outputs
'''Explanation:
🔹 data[:, :-1] → This selects all rows (:) and all columns except the last one (:-1).
This is your input features (independent variables).
It becomes X, your features matrix.
🔹 data[:, -1] → This selects all rows (:) and only the last column (-1).
This is your target variable (dependent variable).
It becomes y, your labels vector.
'''
X, y = data[:, :-1], data[:, -1] #data[:, :-1] → This selects all rows (:) and all columns except the last one (:-1) , data[:, -1] → This selects all rows (:) and only the last column (-1)
print(X.shape, y.shape)
# split into train test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
# fit the model
model = RandomForestRegressor(random_state=1)
model.fit(X_train, y_train)
# make predictions
yhat = model.predict(X_test)
# evaluate predictions
mae = mean_absolute_error(y_test, yhat)
print('MAE: %.3f' % mae)
