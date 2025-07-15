'''import pandas as pd
data = pd.read_csv("melb_data.csv")
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]
y = data.Price
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Imputer
my_pipeline = make_pipeline(Imputer(), RandomForestRegressor())
from sklearn.model_selection import cross_val_score
scores = cross_val_score(my_pipeline, X, y, scoring='neg_mean_absolute_error')
print(scores)'''

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer  # ✅ Corrected import
from sklearn.model_selection import cross_val_score

# Load dataset
data = pd.read_csv("melb_data.csv")

# Select features and target
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]
y = data.Price

# Build pipeline with SimpleImputer and RandomForestRegressor
my_pipeline = make_pipeline(
    SimpleImputer(),                #Replaced Imputer with SimpleImputer
    RandomForestRegressor()
)

# Perform cross-validation
scores = cross_val_score(my_pipeline, X, y, scoring='neg_mean_absolute_error')

# Print the scores
print(scores)


#SimpleImputer() handles missing values
#cross_val_score(..., scoring='neg_mean_absolute_error'): returns negative MAE, so you'll usually multiply it by -1 to interpret the actual error.
