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
cols=["Broad", "Metre" , "Narrow", " Total"]
for col in cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    else:
        print(f"{col} column not found")

#1.5Check result
print(df.dtypes)
