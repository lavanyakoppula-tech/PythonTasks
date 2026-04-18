import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

# create dataframe
df = pd.DataFrame({"Departments": departments, "Salaries": salaries})

# line graph
plt.subplot(2,3,1)
plt.plot(df["Salaries"])
plt.title("Line Graph")

# bar chart
plt.subplot(2,3,2)
plt.bar(df["Departments"], df["Salaries"])
plt.title("Bar Graph")

# pie chart (department distribution)
dept_counts = df["Departments"].value_counts()
plt.subplot(2,3,3)
plt.pie(dept_counts, labels=dept_counts.index)
plt.title("Pie Chart")

# histogram
plt.subplot(2,3,4)
plt.hist(df["Salaries"])
plt.title("Histogram")

# scatter plot
plt.subplot(2,3,5)
plt.scatter(range(len(df)), df["Salaries"])
plt.title("Scatter Plot")

# fix layout
plt.tight_layout()

# display all in one window
plt.show()
