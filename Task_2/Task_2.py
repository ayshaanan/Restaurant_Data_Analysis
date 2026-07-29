import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

print("Program started")
df = pd.read_csv("restaurant.csv")
print("Dataset loaded successfully")
print(df.head())

df["Cuisines"] = df["Cuisines"].fillna("Unknown")
print("Missing values handled")
features = ["Cuisines", "Price range", "Has Online delivery", "City"]
data = df[features]
print("Selected features:")
print(data.head())

encoder = LabelEncoder()
for col in data.columns:
    data[col] = encoder.fit_transform(data[col])

print("Encoded data:")
print(data.head())
user_preference = {
    "Cuisines": "Italian",
    "Price range": 2,
    "Has Online delivery": "Yes",
    "City": "New Delhi"
}

user_df = pd.DataFrame([user_preference])

for col in user_df.columns:
    user_df[col] = encoder.fit_transform(user_df[col])

print("Encoded user preferences:")
print(user_df)
similarity_scores = cosine_similarity(data, user_df)
df["Similarity Score"] = similarity_scores
recommendations = df.sort_values(by="Similarity Score", ascending=False).head(5)

print("\nRecommended Restaurants:")
print(recommendations[["Restaurant Name", "Cuisines", "City", "Price range"]])

