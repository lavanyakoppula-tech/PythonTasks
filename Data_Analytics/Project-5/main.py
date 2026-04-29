import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#Scenario 3: Expensive Cars Analysis (Filtering + Bar) 
#Find which fuel types are most common among expensive cars. 
"""
Tasks: 
● Filter cars where: 
○ Selling_Price > 10 
● Group the filtered data by: 
○ Fuel_Type 
● Count number of cars in each fuel type. 
● Convert: 
○ fuel type labels 
○ counts 
into NumPy arrays. 
● Plot a bar chart using Matplotlib: 
○ X-axis → Fuel Type 
○ Y-axis → Count of expensive cars 
● Add: 
○ title 
○ x-label 
○ y-label 
● Save the graph."""

# 1. Load the dataset
df = pd.read_csv("cardata.csv")

# 1. Filter cars where Selling_Price > 10
expensive_cars = df[df['Selling_Price'] > 10]
print("(S3) Filtering cars with Selling_Price > 10\n", expensive_cars)
print("========================================================")

# 2. Count number of cars per Fuel_Type
fuel_counts = expensive_cars['Fuel_Type'].value_counts()
print("(S3) Count of cars per Fuel_Type\n", fuel_counts)
print("========================================================")

# 3. (Optional) Select top fuel types if needed (e.g., top 5)
top_fuel_types = fuel_counts.head(5)

# 4. Convert results to NumPy arrays
fuel_types = top_fuel_types.index.to_numpy()
counts = top_fuel_types.values

# 5. Plot bar chart
plt.figure(figsize=(8, 5))
plt.bar(fuel_types, counts)

plt.xlabel("Fuel Type")
plt.ylabel("Count of Expensive Cars")
plt.title("Bar Graph of Fuel Types (Selling Price > 10)")

# 6. Rotate labels if needed
plt.xticks(rotation=45)

# 7. Save graph
#plt.savefig("expensive_cars_fueltype_bar.png")

# Optional: show plot
plt.show()
