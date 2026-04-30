# ==============================================================================
#  Project Title: Car Data Analysis 
#  Analysing the Car data dataset using Numpy, Pandas and matplotlib
# ==============================================================================

#==============================================================================
#                  Importing the required libraries
#==============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
==================================================================================
                Scenario 1: Data Loading & Basic Cleaning
================================================================================== 
Understand the dataset structure and prepare it for analysis. 
Tasks: 
● Load the dataset using Pandas. 
● Display: 
○ First 5 rows 
○ Last 5 rows 
○ Column names 
○ Shape of dataset 
● Check data types of all columns. 
● Check for missing values in:
○ Selling_Price 
○ Present_Price 
○ Kms_Driven 
○ Fuel_Type 
● Fill missing values: 
○ Selling_Price → mean 
○ Present_Price → mean 
○ Kms_Driven → mean 
○ Fuel_Type → mode 
● Convert numeric columns to proper numeric type if required: 
○ Selling_Price 
○ Present_Price 
○ Kms_Driven 
○ Year 
● Convert Selling_Price and Kms_Driven into NumPy arrays. 
● Use NumPy to calculate: 
○ minimum selling price 
○ maximum selling price 
○ average selling price '''

#Load the dataset using Pandas
df = pd.read_csv("cardata.csv")
#Display: First 5 rows
print(f"Displaying First 5 rows:\n{df.head()}")
print("---------------------------------------------------------------------------------")
print(f"Displaying last 5 rows:\n{df.tail()}") #Last 5 rows
print("---------------------------------------------------------------------------------")
print(f"Column names:\n{df.columns}") #Column names
print()
print(f"Shapes of Dataset:{df.shape}\n") #Shape of dataset
print("---------------------------------------------------------------------------------")
# Checking data types of all columns.
print(df.dtypes) 
print("---------------------------------------------------------------------------------")
#Check for missing values in: Selling_Price, Present_Price, Kms_Driven, Fuel_Type
print("Missing values:")
print(df[["Selling_Price","Present_Price","Kms_Driven","Fuel_Type"]].isnull().sum())

# Fill missing values:
# Selling_Price → mean 
df["Selling_Price"]=df["Selling_Price"].fillna(df["Selling_Price"].mean())
# Present_Price → mean
df["Present_Price"]=df["Present_Price"].fillna(df["Present_Price"].mean())
# Kms_Driven → mean
df["Kms_Driven"]=df["Kms_Driven"].fillna(df["Kms_Driven"].mean())
# Fuel_Type → mode
df["Fuel_Type"]=df["Fuel_Type"].fillna(df["Fuel_Type"].mode()[0])
print("---------------------------------------------------------------------------------")

#Converting numeric columns to proper numeric type: Selling_Price, Present_Price, Kms_Driven, Year 
numeric=["Selling_Price","Present_Price","Kms_Driven","Year"]
df[numeric]=df[numeric].apply(pd.to_numeric,errors='coerce')
print(df.dtypes)

#Convert Selling_Price and Kms_Driven into NumPy arrays.
S_price=df["Selling_Price"].to_numpy()
KMs=df["Kms_Driven"].to_numpy()
print("---------------------------------------------------------------------------------")
# minimum selling price 
min_S_price=S_price.min()
print(f"Minimun Selling Price: {min_S_price}")
# maximum selling price 
max_S_price=S_price.max()
print(f"Maximum Selling Price: {max_S_price}")
# average selling price
avg_S_price=S_price.mean()
print(f"Average Selling Price: {avg_S_price:.2f}")


'''
==================================================================================
                Scenario 2: Data Loading & Basic Cleaning
==================================================================================


Tasks: 
● Select: 
  ○ Car_Name 
  ○ Selling_Price 
● Take the first 10 rows only using Pandas. 
● Convert Selling_Price into a NumPy array. 
● Plot a line graph using Matplotlib: 
  ○ X-axis → row index (0–9) 
  ○ Y-axis → Selling Price 
● Add: 
  ○ title 
  ○ x-axis label 
  ○ y-axis label 
  ○ markers 
● Save the graph with a suitable filename.
'''

import matplotlib.pyplot as plt

# Select required columns and first 10 rows
select_df = df[['Car_Name', 'Selling_Price']].head(10)

# Convert to NumPy array
selling_price = select_df['Selling_Price'].to_numpy()

# Plot
plt.figure(figsize=(8, 5))
plt.plot(range(len(selling_price)), selling_price, marker='o')

# Labels and title
plt.title("Line Graph Of Selling Price Trend (First 10 Cars)")
plt.xlabel("Car Index (0–9)")
plt.ylabel("Selling Price")

# Save and show
plt.savefig("(S2)Line graph Of selling_price_trend.png")
plt.show()

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
plt.savefig("(S3)Bar Graph Of expensive_cars_fueltype_bar.png")

# Optional: show plot
plt.show()

#============================================================================
# Scenario 4
#============================================================================
# 1. Count number of cars in each fuel type
fuel_counts = df['Fuel_Type'].value_counts()

# 2. (Optional) Select top categories
# For pie chart, usually all categories are fine
top_fuels = fuel_counts  # or fuel_counts.head(5)

# 3. Prepare labels and values
labels = top_fuels.index
values = top_fuels.values

# 4. Convert values to NumPy array
import numpy as np
values = np.array(values)

# 5. Plot pie chart
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%')

# 6. Add title
plt.title("Pie Chart Of Distribution of Cars by Fuel Type")

# 7. Save graph
plt.savefig("(S4)Pie Chart Of fuel_type_distribution.png")

# 8. Show plot
plt.show()

#============================================================================
# Scenario 5: Present Price vs Selling Price (Scatter Plot)
#============================================================================

"""Check whether cars with higher present price also have higher selling price. 
Tasks: 
    ● Select: 
        ○ Present_Price 
        ○ Selling_Price 
    ● Remove missing values if any. 
    ● Take a smaller sample (for example first 50 or 100 rows) using Pandas. 
    ● Convert both columns into NumPy arrays. 
    ● Plot a scatter plot using Matplotlib: 
        ○ X-axis → Present_Price 
        ○ Y-axis → Selling_Price 
    ● Add: 
        ○ title 
        ○ x-label 
        ○ y-label 
    ● Observe whether there is a positive relationship. 
    ● Save the graph."""

# Select required columns
data = df[['Present_Price', 'Selling_Price']]
print("(S5)Selecting required coiumns\n", data)
print("====================================================================")

# Replace missing values (NaN) with 0 (or you can use mean instead)
data = data.replace(np.nan, 0)

# Take first 50 rows
data = data.head(50)
print("(S5)Taking smaller sample for 50 rows/n", data)
print("====================================================================")
print("====================================================================")

# Convert to NumPy arrays
present_price = data['Present_Price'].to_numpy()
selling_price = data['Selling_Price'].to_numpy()

# Scatter plot
plt.figure(figsize=(6, 4))
plt.scatter(present_price, selling_price, color='purple')

# Labels and title
plt.title("Scatter Graph Of Present Price vs Selling Price")
plt.xlabel("Present Price")
plt.ylabel("Selling Price")

# Save graph
plt.savefig("(S5)Scatter Graph Of present_vs_selling_price.png")

# Show graph
plt.show()

























