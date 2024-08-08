import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import joblib
from sklearn.metrics import r2_score
# Load data
data = pd.read_csv("/home/unnatikdm/itr/bangalore house price prediction OHE-data.csv")

# Copy data
df = data.copy()
df['size'] = df['size'].str.replace(' BHK', '', regex=False)

# Features and target
X = df[ 'bath', 'balcony', 'price', 'total_sqft_int', 'bhk'
       ]

y = df['price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=589)

# Train model
clf = KNeighborsRegressor(n_neighbors=4)
clf_train = clf.fit(X_train, y_train)

# Save model

# Load the model
joblib.dump(clf_train, '/home/unnatikdm/itr/model_knn.pkl')


# Test prediction (if needed)
pred = clf_train.predict(X_test)
print(f"R2 Score: {r2_score(y_test, pred)}")

print(df.iloc[0])


