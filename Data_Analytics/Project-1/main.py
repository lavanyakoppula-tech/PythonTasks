# =======================================================================================================
#  Project Title: Railway Gauge Data Study
# Using NumPy, Pandas, and Matplotlib for analysis




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Scenario 1: Basic Data Loading & Cleaning Data
"""1. Load the dataset into a Pandas DataFrame. 
2. Display the first 5 rows and column names. 
3. Check for missing values and replace them with 0. 
4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.""" 


data = pd.read_csv("railway_gauges.csv")
print(data.head())

print(data.columns)

# Handle missing values
data.fillna(0, inplace=True)

# Convert columns to numeric except Year
for col in data.columns:
    if col != "Year":
        data[col] = pd.to_numeric(data[col], errors="coerce")

print(data.dtypes)

#Scenario 2: Simple Visualization 
"""1. Extract Year and Total columns. 
2. Plot a line graph showing Total tracks over years. 
3. Add: 
○ Title 
○ X and Y labels 
4. Identify whether the trend is increasing or decreasing.""" 



yrs = data["Year"]
tot_tracks = data["Total"]

plt.plot(yrs, tot_tracks, marker='o')
plt.title("Growth of Total Railway Tracks")
plt.xlabel("Year")
plt.ylabel("Total Length")
plt.tight_layout()
plt.show()

print("Trend is increasing year by year but with some dips in later years")


# Scenario 3: Filter Data & Bar Chart

"""1. Filter the dataset for years after 2000. 
2. Select Broad Gauge, Metre Gauge, and Narrow Gauge. 
3. Plot a grouped bar chart comparing all three gauges. 
4. Add legend and proper labels. 
5. Identify which gauge dominates in recent years."""
# Extract year as integer
data["Year_num"] = data["Year"].str[:4].astype(int)

recent_data = data[data["Year_num"] > 2000]

gauges = recent_data[["Broad Gauge", "Metre Gauge", "Narrow Gauge"]]

positions = np.arange(len(recent_data))

bar_width = 0.2

plt.style.use("ggplot")

plt.bar(positions - bar_width, gauges["Broad Gauge"], width=bar_width, label="Broad")
plt.bar(positions, gauges["Metre Gauge"], width=bar_width, label="Metre")
plt.bar(positions + bar_width, gauges["Narrow Gauge"], width=bar_width, label="Narrow")

plt.xlabel("Year")
plt.ylabel("Gauge Length")
plt.title("Comparison of Gauges After 2000")
plt.xticks(positions, recent_data["Year_num"])
plt.legend()

plt.show()

print("Broad gauge dominented since 2000")

#Scenario 4:  Feature Engineering + Pie Chart
"""1. Calculate total sum of each gauge across all years. 
2. Create a new structure (Series/DataFrame) for totals. 
3. Plot a pie chart showing percentage contribution. 
4. Add percentage labels (autopct). 
5. Interpret which gauge contributes the most. """
totals = pd.Series({
    "Broad": data["Broad Gauge"].sum(),
    "Metre": data["Metre Gauge"].sum(),
    "Narrow": data["Narrow Gauge"].sum()
})

plt.pie(totals,
        labels=["Broad Gauge", "Metre Gauge", "Narrow Gauge"],
        autopct="%1.1f%%",
        startangle=180,
        explode=(0.1, 0, 0))

plt.title("Gauge Contribution Percentage")
plt.show()

print("Broad Gauge contributes the most to the total railway network among all gauge types.")


#Scenario 5:  Advanced Analysis + Multiple Graphs
"""1. Create new columns: 
○ % Broad Gauge 
○ % Metre Gauge 
○ % Narrow Gauge 
2. Use NumPy (np.diff) to calculate yearly growth of Total tracks. 
3. Plot: 
○ Line graph for all gauges 
○ Stacked bar chart showing composition 
4. Highlight: 
○ Years with highest growth 
○ Decline in any gauge 
5. Provide a final conclusion: 
�
�
“Is the railway system shifting towards a single dominant gauge?”"""


# Percentage columns
data["Broad_%"] = (data["Broad Gauge"] / data["Total"]) * 100
data["Metre_%"] = (data["Metre Gauge"] / data["Total"]) * 100
data["Narrow_%"] = (data["Narrow Gauge"] / data["Total"]) * 100

# Growth calculation
growth = np.diff(data["Total"])
data["Growth"] = np.insert(growth, 0, 0)

print(data["Growth"])

# Line graph for gauges
plt.plot(data["Year_num"], data["Broad Gauge"], label="Broad", marker='o')
plt.plot(data["Year_num"], data["Metre Gauge"], label="Metre", marker='o')
plt.plot(data["Year_num"], data["Narrow Gauge"], label="Narrow", marker='o')

plt.xlabel("Year")
plt.ylabel("Gauge Length")
plt.legend()
plt.show()

# Stacked bar chart
plt.bar(data["Year_num"], data["Narrow Gauge"], label="Narrow")
plt.bar(data["Year_num"], data["Metre Gauge"],
        bottom=data["Narrow Gauge"], label="Metre")
plt.bar(data["Year_num"], data["Broad Gauge"],
        bottom=data["Narrow Gauge"] + data["Metre Gauge"], label="Broad")

plt.xlabel("Year")
plt.ylabel("Gauge Length")
plt.legend()
plt.show()

# Highest growth year
max_growth_year = data.loc[data["Growth"].idxmax(), "Year_num"]
print(max_growth_year)

# Decline years
print("Decline years:")
print(data.loc[data["Growth"] < 0, "Year_num"])

print("Yes, the railway system is clearly shifting toward a single dominant gauge that is Broad Gauge.")
