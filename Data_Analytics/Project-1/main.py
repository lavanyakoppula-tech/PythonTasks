""" Basic Data Loading & Cleaning 
You are given a CSV file containing railway gauge data. 

Tasks: 
1. Load the dataset into a Pandas DataFrame. 
2. Display the first 5 rows and column names. 
3. Check for missing values and replace them with 0. 
4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types."""


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#1.1 Load the dataset into a Pandas DataFrame.

df = pd.read_csv('railway_gauges.csv')


#1.2 Display the first 5 rows and column names

print("first five rows:\n",df.head(5))
print("column names:\n",df.columns)


#1.3  Check for missing values and replace them with 0.
print("missing values:\n",df.isnull().sum())

df.fillna(0,inplace=True)

#1.4 Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.
df.columns = df.columns.str.strip()
cols = ["Broad", "Metre", "Narrow", "Total"]
df.columns = df.columns.str.strip().str.replace(" Gauge", "", regex=False)

df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

#1.5Check result
print(df.dtypes)


"""Scenario 2: Simple Visualization 
You want a quick understanding of total railway track growth. 
�
�
Tasks: 
1. Extract Year and Total columns. 
2. Plot a line graph showing Total tracks over years. 
3. Add: 
○ Title 
○ X and Y labels 
4. Identify whether the trend is increasing or decreasing."""


#2.1Extract Year and Total columns
data = df[['Year', 'Total']]
print(data.head())

#2.2 Plot a line graph showing Total tracks over years. 
plt.plot(data['Year'], data['Total'], marker='o')
#2.3 Add:  Title ,X and Y labels

plt.title("Total Railway Track Growth Over Years")
plt.xlabel("Year")
plt.ylabel("Total Tracks")
plt.savefig('Line.png')
plt.show()


#2.4 Identify whether the trend is increasing or decreasing
if data['Total'].iloc[-1] > data['Total'].iloc[0]:
   result = "Trend: Increasing"
else:
    result = "Trend: Decreasing"

print(result)


"""Scenario 3: Filtering + Bar Chart 
You are asked to analyze modern railway expansion. 
�
�
Tasks: 
1. Filter the dataset for years after 2000. 
2. Select Broad Gauge, Metre Gauge, and Narrow Gauge. 
3. Plot a grouped bar chart comparing all three gauges. 
4. Add legend and proper labels. 
5. Identify which gauge dominates in recent years."""


#3.1  Filter the dataset for years after 2000.
df.columns = df.columns.str.strip()
# Convert Year column to numeric
df["Year"] = pd.to_numeric(df["Year"], errors='coerce')
filter_data = df[df["Year"] > 2000]

print(filter_data.head())


#3.2 Select Broad Gauge, Metre Gauge, and Narrow Gauge.
cols = filter_data.columns.intersection(["Broad", "Metre", "Narrow"])

data = filter_data[cols]

print(data.head())

#3.3 Plot a grouped bar chart comparing all three gauges.







