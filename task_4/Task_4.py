import pandas as pd
import matplotlib.pyplot as plt

print("Program started")

df = pd.read_csv("restaurant.csv")
print("Dataset loaded successfully")

print(df[['City', 'Latitude', 'Longitude']].head())
plt.figure(figsize=(8,6))
plt.scatter(df['Longitude'], df['Latitude'], alpha=0.3)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Geographical Distribution of Restaurants")
plt.show()
city_counts = df['City'].value_counts().head(10)

print("\nTop 10 Cities with Most Restaurants:")
print(city_counts)

city_counts.plot(kind='bar', figsize=(8,5))
plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.show()

avg_rating_city = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False).head(10)

print("\nTop 10 Cities by Average Rating:")
print(avg_rating_city)

avg_price_city = df.groupby('City')['Price range'].mean().sort_values(ascending=False).head(10)

print("\nTop 10 Cities by Average Price Range:")
print(avg_price_city)

top_cuisines_city = df.groupby('City')['Cuisines'].agg(
    lambda x: x.mode().iloc[0] if not x.mode().empty else "Unknown"
)

print("\nMost Common Cuisine in Each City (sample):")
print(top_cuisines_city.head(10))
