print("Program started")

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("restaurant.csv")   # use your actual dataset name
print("Dataset loaded successfully")

print(df.head())
df = df.dropna(subset=['Cuisines'])

df.fillna({
    'City': 'Unknown',
    'Has Online delivery': 'No',
    'Price range': df['Price range'].median()
}, inplace=True)

print("Missing values handled")
y = df['Cuisines']
X = df[['City', 'Price range', 'Has Online delivery', 'Votes']]
encoder = LabelEncoder()

X = X.copy()
X['City'] = encoder.fit_transform(X['City'])
X['Has Online delivery'] = encoder.fit_transform(X['Has Online delivery'])
y = encoder.fit_transform(y)

print("Categorical data encoded")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Data split into training and testing sets")
model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

print("Model training completed")
y_pred = model.predict(X_test)

print("Predictions generated")
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

