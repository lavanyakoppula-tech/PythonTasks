#Project Title: ign
# Using NumPy, Pandas, and Matplotlib for analysis
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#Scenario 1: Data Loading & Preprocessing 
"""Tasks: 
1. Load the dataset using Pandas. 
2. Display: 
○ First 5 rows (head()) 
○ Last 5 rows (tail()) 
○ Shape of dataset 
3. Remove the unnecessary column: 
○ "Unnamed: 0" (index column) 
4. Check for missing values in: 
○ score, genre, platform 
5. Handle missing values: 
○ Fill numeric column score with mean 
○ Fill categorical column genre with mode 
6. Ensure correct data types: 
○ score → float 
○ release_year, release_month, release_day → integer """

df = pd.read_csv("ign.csv")
print(df.head())
print(df.tail())
print(df.shape)
df = df.drop(columns=["Unnamed: 0"])
print("unnecessary columns:",df)
print("missing values:\n",df[["score", "genre", "platform"]].isnull().sum())
df["score"] = df["score"].fillna(df["score"].mean())
df["genre"] = df["genre"].fillna(df["genre"].mode()[0])
#print("handling missing values:\n",df["score"],df["genre"])
print("handling missing values:",df[["score", "genre"]].head())
df["score"] = df["score"].astype(float)
df["release_year"] = df["release_year"].astype(int)
df["release_month"] = df["release_month"].astype(int)
df["release_day"] = df["release_day"].astype(int)
print(df[["score","release_year","release_month","release_day"]])


#Scenario 2: Line Graph (Score Trend) + Save
"""1. Group data by release_year. 
2. Calculate average score per year using Pandas. 
3. Convert results into NumPy arrays. 
4. Plot a line graph: 
○ X-axis → release_year 
○ Y-axis → average score 
5. Add: 
○ Title: "Average Game Score Over Years" 
○ Axis labels 
6. Save the graph: plt.savefig("avg_score_trend.png")"""

yearly_avg = df.groupby("release_year")["score"].mean()

# Convert to NumPy arrays
years = yearly_avg.index.to_numpy()
avg_scores = yearly_avg.values

# Plot line graph
plt.figure(figsize=(10, 5))
plt.plot(years, avg_scores, marker='o', linestyle='-')
plt.title("Average Game Score Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.grid(True)
plt.show()

#Scenario 3: Filtering + Bar Chart + Save
"""1. Filter dataset where: 
○ score > 7 
2. Count number of high-rated games per platform. 
3. Select

→ count of games 
6. Rotate x-axis labels for readability. 
Save the graph: plt.savefig("top_platforms_bar.png") """

high_rated = df[df["score"] > 7]

# Count number of games per platform
platform_counts = high_rated["platform"].value_counts()
top_platforms = platform_counts.head(10)

# Convert to NumPy arrays
platforms = top_platforms.index.to_numpy()
counts = top_platforms.values

# Plot bar chart
plt.figure(figsize=(10, 5))
plt.bar(platforms, counts, color='skyblue')

# Add title and labels
plt.title("Top 10 Platforms with High-Rated Games")
plt.xlabel("Platform")
plt.ylabel("Number of Games")
plt.xticks(rotation=45)
#plt.savefig("top_platforms_bar.png")
plt.show()


#Scenario 4: Aggregation + Pie Chart + Save

"""1. Count the number of games per genre. 
2. Select top 5 genres using Pandas. 
3. Prepare labels and values. 
4. Plot a pie chart: 
○ Labels → genre 
○ Values → count 
5. Add percentage labels (autopct). 
Save the graph: plt.savefig("genre_distribution.png")"""


genre_counts = df["genre"].value_counts()

# Select top 5 genres
top_genres = genre_counts.head(5)

# Prepare labels and values
labels = top_genres.index.to_numpy()
values = top_genres.values
plt.figure(figsize=(8, 8))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Top 5 Game Genres Distribution")
#plt.axis('equal')
plt.show()



#Scenario 5: Advanced Analysis + Multiple Graphs

"""�
�
Part 1: Feature Engineering 
1. Create a new column: 
○ score_category: 
■ score >= 9 → "Excellent" 
■ 7 <= score < 9 → "Good" 
■ < 7 → "Average" 
2. Convert editors_choice: 
○ Y → 1, N → 0 """


df["score_category"] = np.where(
    df["score"] >= 9, "Excellent",
    np.where(df["score"] >= 7, "Good", "Average")
)

# Convert editors_choice to numeric
df["editors_choice"] = df["editors_choice"].map({"Y": 1, "N": 0})

# Display updated columns
print("updated_coluns:\n",df[["score", "score_category", "editors_choice"]].head())


"""Part 2: NumPy Analysis 
3. Use NumPy to: 
○ Calculate yearly score growth using np.diff() on average yearly scores"""

yearly_avg = df.groupby("release_year")["score"].mean().sort_index()

# Convert to NumPy arrays
years = yearly_avg.index.to_numpy()
avg_scores = yearly_avg.values

# Calculate yearly score growth using np.diff()
score_growth = np.diff(avg_scores)

# Display results
print("Years:\n", years)
print("Average Scores:\n", avg_scores)
print("Yearly Score Growth:\n", score_growth)


"""Part 3: Visualizations 
�
�
Line Graph 
4. Plot trend of: 
○ Average score per release_year 
�
�
Stacked Bar Chart 
5. Show count of: 
○ score_category per release_year
Histogram 
6. Plot distribution of: 
○ score"""



# -------- Line Graph: Average Score per Year --------
yearly_avg = df.groupby("release_year")["score"].mean()

years = yearly_avg.index.to_numpy()
avg_scores = yearly_avg.values

plt.figure(figsize=(10, 5))
plt.plot(years, avg_scores, marker='o')

plt.title("Average Score Trend Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.grid(True)

plt.show()


# -------- Stacked Bar Chart: score_category per Year --------
category_counts = df.groupby(["release_year", "score_category"]).size().unstack(fill_value=0)

category_counts.plot(kind="bar", stacked=True, figsize=(12, 6))

plt.title("Score Category Distribution per Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Games")
plt.xticks(rotation=45)

plt.show()


# -------- Histogram: Score Distribution --------
plt.figure(figsize=(8, 5))
plt.hist(df["score"], bins=20, color='orange', edgecolor='black')

plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.show()

