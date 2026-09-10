
# Pandas + Matplotlib (Cleaned & Runnable)


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Create DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, None, 35, 28],
    "City": ["New York", "London", "Paris", "Tokyo", "Berlin"],
    "Salary": [50000, 60000, 55000, 70000, 48000]
}
df = pd.DataFrame(data)
print(df)

# 2. Basic exploration
print(df.dtypes)
print(df.describe())
print(df.head())
print(df.tail(3))
print(df.columns)
print(df.shape)

# 3. Selecting columns & rows
print(df[["Name", "City"]])
print(df[df["Age"] > 28])
print(df.iloc[1:4])
print(df.loc[0:2, ["Name", "Salary"]])

# 4. Insert / Drop columns
df.insert(loc=3, column="Food", value=0)
df.insert(loc=4, column="Equipment", value="Oxygen Cylinder")
print(df)

df.drop(columns=["Food"], inplace=True)   # or axis=1
print(df.head())

# 5. Missing values
print(df.isnull().sum())

mean_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(mean_age)
print(df.isnull().sum())

# 6. Simple Matplotlib plot
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
plt.plot(x, y, color="r", marker="o", linewidth=2)
plt.title("Simple Line Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)
plt.show()

# Bonus: Age vs Salary scatter
plt.figure(figsize=(8, 5))
plt.scatter(df["Age"], df["Salary"], color="teal", s=100)
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid(True, alpha=0.3)
plt.show()

# Bonus: Bar chart of cities
city_counts = df["City"].value_counts()
city_counts.plot(kind="bar", color="coral")
plt.title("People per City")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
