import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('railway_gauges.csv')

# Display first 5 rows
print(df.head())

# Get row with maximum Total value (alternative method)
max_row = df[df['Total'] == df['Total'].max()]
print("\nRow with maximum Total:\n", max_row)

# plotting data 
df_plot = df.drop('Total', axis=1)
# Plot bar chart 
df_plot.plot.bar(x='Year')

plt.xticks(rotation=70)
plt.xlabel('Year')
plt.ylabel('Count')
plt.title("Number of railway tracks installed per year")

plt.savefig('rail_gauges.png')
plt.show()
