import pandas as pd

print("Program started")

df = pd.read_csv("restaurant.csv")

print("Dataset loaded successfully")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

# Fill numeric columns with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill text columns with most common value
for col in df.select_dtypes(include='object'):
    df[col] = df[col].fillna(df[col].mode()[0])

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in df.select_dtypes(include='object'):
    df[col] = le.fit_transform(df[col])

X = df.drop("Aggregate rating", axis=1)
y = df["Aggregate rating"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score

print("\nModel Performance:")
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
importance = pd.Series(model.coef_, index=X.columns)
print("\nImportant Features:")
print(importance.sort_values(ascending=False))



